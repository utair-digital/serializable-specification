from specification import AttributeSpecification
from tests.fixtures.expected_result import (
    not_in_result,
    not_in_2_result,
    not_in_3_result,
)
from tests.fixtures.fixtures import generated_data


def test_not_in():
    """
    Price not in 11000-49000
    """
    specification = AttributeSpecification("price", "not_in", range(11000, 49000))
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == not_in_result


def test_not_in_2():
    """
    Price not in 11000-49000
    """
    specification = AttributeSpecification("buyer.age", "not_in", range(19, 66))
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == not_in_2_result


def test_not_in_3():
    """
    Cars without A and E in name
    """
    cars_contains_ae = list(
        set(
            i.car
            for i in generated_data
            if (i.car.upper().find("A") != -1) or (i.car.upper().find("E") != -1)
        )
    )
    specification = AttributeSpecification("car", "not_in", cars_contains_ae)
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == not_in_3_result
