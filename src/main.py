import re


def find_icao_in_observation(observation):
    x = re.match("(METAR|SPECI)?( COR)? ?([A-Z]{4})", observation)
    return x.group(3)
