from specification import NotSpecification, AttributeSpecification
from tests.fixtures.expected_result import (
    specification_12_result, specification_13_result, specification_14_result)
from tests.fixtures.fixtures import generated_data


def test_specification_9():
    """
    NOT telephone +7(9**)***-**-**
    """
    specification = NotSpecification(
        AttributeSpecification("buyer.telephone", "eq", "+7(9**)***-**-**")
    )
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_12_result


def test_specification_10():
    """
    NOT age<=65
    """
    specification = NotSpecification(
        AttributeSpecification("buyer.age", "le", 65)
    )
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_13_result


def test_specification_11():
    """
    NOT power<=900
    """
    specification = NotSpecification(
        AttributeSpecification("power", "le", 900)
    )
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_14_result


