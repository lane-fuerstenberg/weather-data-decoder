import pytest
from src.main import find_icao_in_observation


def check_find_icao_in_observation(metar, expected_icao):
    found_icao = find_icao_in_observation(metar)
    assert found_icao == expected_icao


def test_pass_in_observation_with_SPECI_in_it():
    check_find_icao_in_observation(
        "SPECI KBXK 121815Z AUTO 19003KT 10SM 25/02 A3014 RMK A01=", "KBXK")


def test_pass_in_observation_with_LWIS_in_it():
    check_find_icao_in_observation(
        "LWIS KBXK 121815Z AUTO 19003KT 10SM 25/02 A3014 RMK A01=", "KBXK")


def test_pass_in_observation_with_icao_KGNT():
    check_find_icao_in_observation(
        "METAR KGNT 121815Z AUTO 34013G16KT 10SM CLR 12/M04 A3043 RMK AO2 T01231040=", "KGNT")


def test_pass_in_observation_with_icao_KGXF():
    check_find_icao_in_observation(
        "METAR KGXF 121758Z AUTO 36007KT 9SM CLR 25/M04 A3011 RMK AO2 SLP188 T02481036 10248 20092 50006=", "KGXF")


def test_pass_in_observation_with_icao_KBXK_and_with_COR_in_it():
    check_find_icao_in_observation(
        "METAR COR KBXK 121815Z AUTO 19003KT 10SM 25/02 A3014 RMK A01=", "KBXK")


def test_pass_in_observation_with_no_report_code():
    check_find_icao_in_observation(
        "KGNT 121815Z AUTO 34013G16KT 10SM CLR 12/M04 A3043 RMK AO2 T01231040=", "KGNT")


def test_pass_in_observation_with_no_icao():
    check_find_icao_in_observation(
        "METAR 121815Z AUTO 19003KT 10SM 25/02 A3014 RMK A01=", "None")
