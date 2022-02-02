from specification import AndSpecification, OrSpecification, AttributeSpecification, NotSpecification
from tests.fixtures.expected_result import (
    specification_1_result, specification_2_result, specification_3_result, specification_4_result,
    specification_5_result)
from tests.fixtures.fixtures import generated_data


def test_specification_1():
    """
    (Jeep price>=48000) OR (Subaru power>=840)
    """
    specification = OrSpecification(
        AndSpecification(
            AttributeSpecification("car", "eq", "Jeep"),
            AttributeSpecification("price", "ge", 48000)
        ),
        AndSpecification(
            AttributeSpecification("car", "eq", "Subaru"),
            AttributeSpecification("power", "ge", 840)
        )
    )
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_1_result


def test_specification_2():
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
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_2_result


def test_specification_3():
    """
    Audi NOT power>900
    """
    specification = AndSpecification(
        AttributeSpecification("car", "eq", "Audi"),
        NotSpecification(
            AttributeSpecification("power", "gt", "900")
        )
    )
    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_3_result


def test_specification_4():
    """
    Daewoo AND Bmw
    """
    specification = AndSpecification(
        OrSpecification(
            AttributeSpecification("car", "eq", "Daewoo"),
            AttributeSpecification("car", "eq", "Bmw"),
        ),
    )

    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_4_result


def test_specification_5():
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

    assert list(filter(specification.is_satisfied_by, generated_data)) == \
           specification_5_result

