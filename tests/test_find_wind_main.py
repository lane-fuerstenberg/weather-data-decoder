import src.main as main


def test_pass_in_observation_with_34013G16KT_in_it():
    assert main.find_wind_in_observation(
        "METAR KGNT 121815Z AUTO 34013G16KT 10SM CLR 12/M04 A3043 RMK AO2 T01231040=") == "34013G16KT"


def test_pass_in_observation_with_33007G15KT_in_it():
    assert main.find_wind_in_observation(
        "METAR KJSO 121815Z AUTO 33007G15KT 10SM CLR 18/10 A3019 RMK AO2 T01910098=") == "33007G15KT"
