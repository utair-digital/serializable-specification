from specification import AndSpecification, AttributeSpecification
from tests.fixtures.expected_result import (
    specification_6_result, specification_7_result, specification_8_result)
from tests.fixtures.fixtures import generated_data


def test_specification_6():
    """
    Jeep AND price>=48000
    """
    specification = AndSpecification(
        AttributeSpecification("car", "eq", "Jeep"),
        AttributeSpecification("price", "ge", 48000),
    )
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_6_result


def test_specification_7():
    """
    age=18 AND Lamborghini
    """
    specification = AndSpecification(
        AttributeSpecification("buyer.age", "eq", 18),
        AttributeSpecification("car", "eq", "Lamborghini"),
    )
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_7_result


def test_specification_8():
    """
    age=18 AND Lamborghini
    """
    specification = AndSpecification(
        AttributeSpecification("buyer.full_name", "eq", "Sixta Goodman"),
        AttributeSpecification("car", "eq", "Mini"),
    )
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_8_result
