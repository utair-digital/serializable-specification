from specification import AttributeSpecification
from tests.fixtures.expected_result import in_result, in_2_result, in_3_result
from tests.fixtures.fixtures import generated_data


def test_in():
    """
    Cars names start with A B C
    """
    cars_start_with_abc = list(
        set(i.car for i in generated_data if i.car.startswith(("A", "B", "C")))
    )
    specification = AttributeSpecification("car", "in", cars_start_with_abc)
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == in_result


def test_in_2():
    """
    Cars names contains W
    """
    cars_contains_w = list(
        set(i.car for i in generated_data if (i.car.upper().find("W") != -1))
    )
    specification = AttributeSpecification("car", "in", cars_contains_w)
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == in_2_result


def test_in_3():
    """
    Power in 0-35
    """
    specification = AttributeSpecification("power", "in", range(0, 35))
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == in_3_result
