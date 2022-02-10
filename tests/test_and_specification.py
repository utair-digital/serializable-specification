from specification import AndSpecification, AttributeSpecification
from tests.fixtures.expected_result import (
    and_eq_ge_result,
    and_eq_eq_result,
    and_eq_eq_2_result,
)
from tests.fixtures.fixtures import generated_data


def test_and_eq_ge():
    """
    Jeep AND price>=48000
    """
    specification = AndSpecification(
        AttributeSpecification("car", "eq", "Jeep"),
        AttributeSpecification("price", "ge", 48000),
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == and_eq_ge_result


def test_and_eq_eq():
    """
    age=18 AND Lamborghini
    """
    specification = AndSpecification(
        AttributeSpecification("buyer.age", "eq", 18),
        AttributeSpecification("car", "eq", "Lamborghini"),
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == and_eq_eq_result


def test_and_eq_eq_2():
    """
    age=18 AND Lamborghini
    """
    specification = AndSpecification(
        AttributeSpecification("buyer.full_name", "eq", "Sixta Goodman"),
        AttributeSpecification("car", "eq", "Mini"),
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == and_eq_eq_2_result
