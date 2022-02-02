from specification import OrSpecification, AttributeSpecification
from tests.fixtures.expected_result import (
    specification_9_result, specification_10_result, specification_11_result)
from tests.fixtures.fixtures import generated_data


def test_specification_9():
    """
    Jeep OR price>=48000
    """
    specification = OrSpecification(
        AttributeSpecification("car", "eq", "Jeep"),
        AttributeSpecification("price", "ge", 48000),
    )
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_9_result


def test_specification_10():
    """
    age=18 OR Lamborghini
    """
    specification = OrSpecification(
        AttributeSpecification("buyer.age", "eq", 18),
        AttributeSpecification("car", "eq", "Lamborghini"),
    )
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_10_result


def test_specification_11():
    """
    Sixta Goodman OR Mini
    """
    specification = OrSpecification(
        AttributeSpecification("buyer.full_name", "eq", "Sixta Goodman"),
        AttributeSpecification("car", "eq", "Mini"),
    )
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_11_result


