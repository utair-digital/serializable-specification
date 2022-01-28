from conftest import *


def test_spec_from_example(test_transports, test_spec):
    assert str(list(filter(test_spec.is_satisfied_by,
                           test_transports))) == \
           "[Moto(model='bmw', speed=190, gearbox={'type': 'sequential', 'gears': []}), Moto(model='bmw', speed=210, gearbox={'type': 'sequential', 'gears': []}), Car(model='bmw', speed=220, gearbox={'type': 'sequential', 'gears': []})]"


def test_specification_jeep_and_subaru_price_10000_230():
    assert list(filter(specification_jeep_and_subaru_price_10000_230.is_satisfied_by, generated_data)) == \
           test_specification_jeep_and_Subaru_price_10000_230_result


def test_specification_jeep_price_48000_and_subaru_power_230():
    assert list(filter(specification_jeep_price_48000_and_subaru_power_230.is_satisfied_by, generated_data)) == \
           test_specification_jeep_price_48000_and_subaru_power_230_result


def test_specification_audi_not_power_900():
    assert list(filter(specification_audi_not_power_900.is_satisfied_by, generated_data)) == \
           test_specification_audi_not_power_900_result


def test_specification_daewoo_bmw():
    assert list(filter(specification_daewoo_bmw.is_satisfied_by, generated_data)) == \
           test_specification_daewoo_bmw_result


def test_specification_age_18():
    assert list(filter(specification_age_18.is_satisfied_by, generated_data)) == \
           test_specification_age_18_result

