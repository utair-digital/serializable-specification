from specification import (
    AndSpecification,
    OrSpecification,
    AttributeSpecification,
    NotSpecification,
)
from tests.fixtures.expected_result import (
    composit_or_and_result,
    composit_and_or_result,
    composit_and_not_result,
    composit_and_or_2_result,
    composit_and_or_3_result,
)
from tests.fixtures.fixtures import generated_data


def test_composit_or_and():
    """
    (Jeep price>=48000) OR (Subaru power>=840)
    """
    specification = OrSpecification(
        AndSpecification(
            AttributeSpecification("car", "eq", "Jeep"),
            AttributeSpecification("price", "ge", 48000),
        ),
        AndSpecification(
            AttributeSpecification("car", "eq", "Subaru"),
            AttributeSpecification("power", "ge", 840),
        ),
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == composit_or_and_result


def test_composit_and_or():
    """
    (Jeep OR Subaru) AND price>10000 AND max_speed>230
    """
    specification = AndSpecification(
        OrSpecification(
            AttributeSpecification("car", "eq", "Jeep"),
            AttributeSpecification("car", "eq", "Subaru"),
        ),
        AttributeSpecification("price", "gt", 10000),
        AttributeSpecification("max_speed", "gt", 230),
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == composit_and_or_result


def test_composit_and_not():
    """
    Audi NOT power>900
    """
    specification = AndSpecification(
        AttributeSpecification("car", "eq", "Audi"),
        NotSpecification(AttributeSpecification("power", "gt", "900")),
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == composit_and_not_result


def test_composit_and_or_2():
    """
    Daewoo AND Bmw
    """
    specification = AndSpecification(
        OrSpecification(
            AttributeSpecification("car", "eq", "Daewoo"),
            AttributeSpecification("car", "eq", "Bmw"),
        ),
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == composit_and_or_2_result


def test_composit_and_or_3():
    """
    age = 18 AND (car Lamborghini OR car Bmw)
    """
    specification = AndSpecification(
        AttributeSpecification("buyer.age", "eq", 18),
        OrSpecification(
            AttributeSpecification("car", "eq", "Lamborghini"),
            AttributeSpecification("car", "eq", "Bmw"),
        ),
    )
    result = list(filter(specification.is_satisfied_by, generated_data))
    assert result == composit_and_or_3_result
