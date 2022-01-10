from src.main import find_modifier_in_observation


def check_find_modifier_in_observation(observation, expected_modifier):
    found_modifier = find_modifier_in_observation(observation)
    assert found_modifier == expected_modifier


def test_pass_in_metar_with_modifier():
    check_find_modifier_in_observation(
        "METAR KGNT 121815Z AUTO 34013G16KT 10SM CLR 12/M04 A3043 RMK AO2 T01231040=", "AUTO")


def test_pass_in_speci_with_modifier():
    check_find_modifier_in_observation(
        "SPECI KBXK 121815Z AUTO 19003KT 10SM 25/02 A3014 RMK A01=", "AUTO")


def test_pass_in_lwis_with_modifier():
    check_find_modifier_in_observation(
        "LWIS KBXK 121815Z AUTO 19003KT 10SM 25/02 A3014 RMK A01=", "AUTO")


def test_pass_in_observation_with_cor_modifier():
    check_find_modifier_in_observation(
        "METAR KGNT 121815Z COR 34013G16KT 10SM CLR 12/M04 A3043 RMK AO2 T01231040=", "COR")


def test_return_none_when_there_is_no_modifier():
    check_find_modifier_in_observation(
        "METAR KGNT 121815Z 34013G16KT 10SM CLR 12/M04 A3043 RMK AO2 T01231040=", "None")
