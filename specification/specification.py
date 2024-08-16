import operator
import typing

from .exceptions import SpecificationError
from .base import BaseSpecification


class Specification(BaseSpecification):
    op: str = None

    def and_specification(self, candidate: 'Specification') -> 'AndSpecification':
        raise NotImplementedError()

    def or_specification(self, candidate: 'Specification') -> 'OrSpecification':
        raise NotImplementedError()

    def not_specification(self) -> 'NotSpecification':
        raise NotImplementedError()

    def attribute_specification(
            self,
            attribute: typing.Union[str, typing.Callable[[typing.Callable], object]],
            op: str,
            value: object,
            aggregation: str = None,
            discover_attribute: bool = True
    ) -> 'AttributeSpecification':
        """
        :param attribute: path to attribute
        :param op: comparison operator
        :param value: attribute value
        :param aggregation: the name of the aggregate function that will be applied to the value before comparison
        :param discover_attribute:
            If True - allows you to pass a complex path
            to an attribute of the form 'my.path.to.attribute.value'.
            False - the complex key will be treated as a single one.
        """
        return AttributeSpecification(attribute, op, value, aggregation, discover_attribute)

    def serialize(self) -> dict:
        if isinstance(self, AttributeSpecification):
            simple_op_dict = {
                'lt': 'lt',
                'le': 'le',
                'eq': 'eq',
                'ne': 'ne',
                'ge': 'ge',
                'gt': 'gt',
                'in': 'in',
                'not_in': 'not_in',
                'not': 'not',
            }
            if self.aggregation not in list(AttributeSpecification.__aggregation_dict__.keys()):
                raise SpecificationError('Custom aggregation functions are not supported for serialize')
            if callable(self.attribute):
                raise SpecificationError('Callable attribute getters are not supported for serialize')
            return {
                'key': "{}".format(self.attribute),
                'op': simple_op_dict[self.op],
                'value': self.value,
                'aggregation': self.aggregation,
                'discover_attribute': self.discover_attribute
            }
        elif isinstance(self, AndSpecification):
            return {
                'and': [x.serialize() for x in self.expression_list]
            }
        elif isinstance(self, OrSpecification):
            return {
                'or': [x.serialize() for x in self.expression_list]
            }
        elif isinstance(self, NotSpecification):
            return {
                'not': self._wrapped.serialize()
            }

    @classmethod
    def deserialize(cls, raw_specification: dict) -> 'Specification':

        def __op_by_alias__(raw_op):
            op_aliases_map = {
                "gte": "ge",
                "lte": "le",
                "nin": "not_in"
            }
            return op_aliases_map.get(raw_op, raw_op)

        def __key_value_to_spec__(_raw_specification):
            keys = list(_raw_specification.keys())
            if all(['key' in keys, 'value' in keys, 'op' in keys]):
                return AttributeSpecification(
                    _raw_specification['key'],
                    __op_by_alias__(_raw_specification['op']),
                    _raw_specification['value'],
                    _raw_specification.get('aggregation'),
                    _raw_specification.get('discover_attribute')
                )
            else:
                for key, value in _raw_specification.items():
                    if key == 'or':
                        return OrSpecification(*[__key_value_to_spec__(x) for x in value])
                    elif key == 'and':
                        return AndSpecification(*[__key_value_to_spec__(x) for x in value])
                    elif key == 'not':
                        return NotSpecification(AttributeSpecification(
                            value['key'],
                            __op_by_alias__(value['op']),
                            value['value'],
                            value.get('aggregation'),
                            value.get('discover_attribute'))
                        )
                    else:
                        raise SpecificationError('Unknown specification type')

        return __key_value_to_spec__(raw_specification)


class CompositeSpecification(Specification):
    op: str = None

    def and_specification(self, candidate: 'Specification') -> 'AndSpecification':
        return AndSpecification(self, candidate)

    def or_specification(self, candidate) -> 'OrSpecification':
        return OrSpecification(self, candidate)

    def not_specification(self) -> 'NotSpecification':
        return NotSpecification(self)


class AndSpecification(CompositeSpecification):
    op: str = 'and'

    def __init__(self, *args: Specification):
        self.expression_list = args

    def is_satisfied_by(self, candidate) -> bool:
        """Checking whether an object satisfies a specification"""
        satisfied_list = []
        for row in self.expression_list:
            if isinstance(row, Specification):
                satisfied_list.append(row.is_satisfied_by(candidate))
            else:
                satisfied_list.append(bool(row))
        return all(satisfied_list)


class OrSpecification(CompositeSpecification):
    op: str = 'or'

    def __init__(self, *args: Specification):
        self.expression_list = args

    def is_satisfied_by(self, candidate) -> bool:
        """Checking whether an object satisfies a specification"""
        satisfied_list = []
        for row in self.expression_list:
            if isinstance(row, Specification):
                satisfied_list.append(row.is_satisfied_by(candidate))
            else:
                satisfied_list.append(bool(row))
        return any(satisfied_list)


class NotSpecification(CompositeSpecification):
    op: str = 'not'
    _wrapped: 'Specification' = Specification()

    def __init__(self, wrapped: 'Specification'):
        self._wrapped: 'Specification' = wrapped

    def is_satisfied_by(self, candidate) -> bool:
        """Checking whether an object satisfies a specification"""
        return bool(not self._wrapped.is_satisfied_by(candidate))


class AttributeSpecification(CompositeSpecification):
    @staticmethod
    def __in__(attribute_value: object, value: list) -> bool:
        return attribute_value in value

    @staticmethod
    def __not_in__(attribute_value: object, value: list) -> bool:
        return attribute_value not in value

    @staticmethod
    def __fake_aggregation__(attribute_value: object) -> object:
        """
        False aggregation function. Because AttributeSpecification is always executed when calling is_satisfied_by
        aggregating function over the value - a fake function is required that does nothing with the value,
        if the spec does not require aggregation
        """
        return attribute_value

    # dictionary of available aggregation functions. Because the ability to serialize the specification - is its
    # inherent part - it is necessary to use a dictionary of possible aggregating functions - for their subsequent
    # serialization, for example in SQL request, HTTP request, etc. Likewise for the functions __in__, __not_in__

    __aggregation_dict__ = {
        'len': len,
        'upper': str.upper,
        'lower': str.lower,
        'max': max,
        'min': min,
        None: __fake_aggregation__.__func__,    # noqa
    }

    def __init__(self,
                 attribute: typing.Union[str, typing.Callable[[typing.Callable], object]],
                 op: str,
                 value: object,
                 aggregation: str = None,
                 discover_attribute: bool = True):
        super().__init__()

        self.op_dict = {
            'lt': operator.lt,
            'le': operator.le,
            'eq': operator.eq,
            'ne': operator.ne,
            'ge': operator.ge,
            'gt': operator.gt,
            'not': operator.not_,
            'in': self.__in__,
            'not_in': self.__not_in__,
        }

        if op not in self.op_dict.keys():
            raise SpecificationError('{} is not supported operator'.format(str(op)))
        if aggregation not in self.__aggregation_dict__.keys():
            raise SpecificationError('{} is not supported aggregation function'.format(str(op)))
        self.aggregation = aggregation
        self.value: object = value
        self.attribute: typing.Union[str, typing.Callable] = attribute
        self.op: str = op
        self.discover_attribute = discover_attribute

    @staticmethod
    def __get_attribute_value__(_candidate, _attribute) -> object:
        try:
            if callable(_attribute):
                return _attribute(_candidate)
            elif issubclass(type(_candidate), dict):
                return _candidate.get(_attribute)
            elif issubclass(type(_candidate), list):
                try:
                    return _candidate[int(_attribute)]
                except ValueError:
                    return _candidate
            else:
                return getattr(_candidate, _attribute)
        except Exception:   # noqa
            return None

    def is_satisfied_by(self, candidate) -> bool:
        """Checking whether an object satisfies a specification"""

        if not self.discover_attribute:
            attribute_value = self.__get_attribute_value__(candidate, self.attribute)
        else:
            attribute_value = candidate
            for index, key in enumerate(self.attribute.split('.')):
                if issubclass(type(attribute_value), list) and not key.isnumeric():
                    segment = ".".join(self.attribute.split('.')[index:])
                    return any([
                        AttributeSpecification(
                            attribute=segment,
                            aggregation=self.aggregation,
                            value=self.value,
                            op=self.op,
                            discover_attribute=self.discover_attribute,
                        ).is_satisfied_by(x) for x in attribute_value
                    ])
                else:
                    attribute_value = self.__get_attribute_value__(attribute_value, key)
        try:
            return self.op_dict[self.op](
                self.__aggregation_dict__[self.aggregation](
                    attribute_value
                ),
                self.value
            )
        except Exception:   # noqa
            return False
