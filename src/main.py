from find_icao import FindIcao

observation_file = open("", "r")
observation = observation_file.read()

icao = FindIcao(observation).find_icao_in_observation()
