from specification import AttributeSpecification, AndSpecification
from tests.fixtures.expected_result import (
    not_in_result,
    and_eq_ge_result,
    not_le_result,
)
from tests.fixtures.fixtures import generated_data


def test_not_in_alias():
    """
    Price not in 11000-49000
    """
    specification = AttributeSpecification.deserialize(
        {
            "aggregation": None,
            "discover_attribute": True,
            "key": "price",
            "op": "nin",
            "value": range(11000, 49000),
        }
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == not_in_result


def test_ge_alias():
    """
    Jeep AND price>=48000
    """
    specification = AndSpecification.deserialize(
        {
            "and": [
                {
                    "aggregation": None,
                    "discover_attribute": True,
                    "key": "car",
                    "op": "eq",
                    "value": "Jeep",
                },
                {
                    "aggregation": None,
                    "discover_attribute": True,
                    "key": "price",
                    "op": "gte",
                    "value": 48000,
                },
            ]
        }
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == and_eq_ge_result


def test_le_alias():
    """
    NOT age<=65
    """
    specification = AttributeSpecification.deserialize(
        {
            "not": {
                "aggregation": None,
                "discover_attribute": True,
                "key": "buyer.age",
                "op": "lte",
                "value": 65,
            }
        }
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == not_le_result
