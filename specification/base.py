from abc import ABCMeta
from abc import abstractmethod
import typing


class BaseSpecificationError(Exception):
    pass


class BaseSpecification(metaclass=ABCMeta):
    op: str = None

    @abstractmethod
    def and_specification(self, candidate: 'BaseSpecification') -> 'BaseSpecification':
        raise NotImplementedError()

    @abstractmethod
    def or_specification(self, candidate: 'BaseSpecification') -> 'BaseSpecification':
        raise NotImplementedError()

    @abstractmethod
    def not_specification(self) -> 'BaseSpecification':
        raise NotImplementedError()

    @abstractmethod
    def attribute_specification(
            self,
            attribute: typing.Union[str, typing.Callable[[typing.Callable], object]],
            op: str,
            value: object,
            aggregation: str = None,
            discover_attribute: bool = True
    ) -> 'BaseSpecification':
        raise NotImplementedError()

    def is_satisfied_by(self, candidate: typing.Any) -> bool:
        """Checking whether an object satisfies a specification"""
        return True

    @abstractmethod
    def serialize(self) -> dict:
        raise NotImplementedError()

    @classmethod
    def deserialize(cls, raw_specification: dict) -> 'BaseSpecification':
        raise NotImplementedError()
