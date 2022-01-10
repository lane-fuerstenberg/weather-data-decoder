import re


def find_icao_in_observation(observation):
    if re.match("(METAR|SPECI|LWIS)?( COR)? ?([A-Z]{4} )", observation):
        x = re.match("(METAR|SPECI|LWIS)?( COR)? ?([A-Z]{4} )", observation)
        icao = x.group(3).strip()
    else:
        icao = "None"

    return icao


def find_modifier_in_observation(observation):
    if " AUTO " in observation:
        modifier = "AUTO"
    elif " COR " in observation:
        modifier = "COR"
    else:
        modifier = "None"

    return modifier
