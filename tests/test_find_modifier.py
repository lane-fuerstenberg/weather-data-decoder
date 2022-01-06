from src.find_modifier import FindModifier


def test_pass_in_observation_with_modifier():

    assert FindModifier(
        "METAR KGNT 121815Z AUTO 34013G16KT 10SM CLR 12/M04 A3043 RMK AO2 T01231040=").find_modifier_in_observation() == "AUTO"


def test_return_none_when_there_is_no_modifier():
    assert FindModifier(
        "METAR KGNT 121815Z 34013G16KT 10SM CLR 12/M04 A3043 RMK AO2 T01231040=").find_modifier_in_observation() == "None"
