import re


class FindIcao:
    def __init__(self, observation):
        self.observation = observation

    def find_icao_in_observation(self):
        if re.match("(METAR|SPECI|LWIS)?( COR)? ?([A-Z]{4} )", self.observation):
            x = re.match(
                "(METAR|SPECI|LWIS)?( COR)? ?([A-Z]{4} )", self.observation)
            icao = x.group(3).strip()
        else:
            icao = "None"

        return icao
