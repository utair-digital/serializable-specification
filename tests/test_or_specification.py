from specification import OrSpecification, AttributeSpecification
from tests.fixtures.expected_result import (
    or_eq_ge_result,
    or_eq_eq_result,
    or_eq_eq_2_result,
)
from tests.fixtures.fixtures import generated_data


def test_or_eq_ge():
    """
    Jeep OR price>=48000
    """
    specification = OrSpecification(
        AttributeSpecification("car", "eq", "Jeep"),
        AttributeSpecification("price", "ge", 48000),
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == or_eq_ge_result


def test_or_eq_eq():
    """
    age=18 OR Lamborghini
    """
    specification = OrSpecification(
        AttributeSpecification("buyer.age", "eq", 18),
        AttributeSpecification("car", "eq", "Lamborghini"),
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == or_eq_eq_result


def test_or_eq_eq_2():
    """
    Sixta Goodman OR Mini
    """
    specification = OrSpecification(
        AttributeSpecification("buyer.full_name", "eq", "Sixta Goodman"),
        AttributeSpecification("car", "eq", "Mini"),
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == or_eq_eq_2_result
