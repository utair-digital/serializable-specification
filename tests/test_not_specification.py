from specification import NotSpecification, AttributeSpecification
from tests.fixtures.expected_result import (
    not_eq_result,
    not_le_result,
    not_le_2_result,
)
from tests.fixtures.fixtures import generated_data


def test_not_eq():
    """
    NOT telephone +7(9**)***-**-**
    """
    specification = NotSpecification(
        AttributeSpecification("buyer.telephone", "eq", "+7(9**)***-**-**")
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == not_eq_result


def test_not_le():
    """
    NOT age<=65
    """
    specification = NotSpecification(AttributeSpecification("buyer.age", "le", 65))
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == not_le_result


def test_not_le_2():
    """
    NOT power<=900
    """
    specification = NotSpecification(AttributeSpecification("power", "le", 900))
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == not_le_2_result
