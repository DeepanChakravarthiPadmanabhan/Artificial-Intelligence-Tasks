import TravellingSalesPerson
import City
import SimpleHillClimbing
import SteepestAscendHillClimbing

import datetime

filename = './Cities/49_cities.txt'
Restart_Count = 5

TSP = TravellingSalesPerson.TravellingSalePerson()

with open(filename) as file:
    next(file)
    for line in file:
        city, lat, lon = line.strip('\n').split(',')
        TSP.AddCity(City.City(city, float(lat), float(lon)))

start_time = datetime.datetime.now()

# tsp = SimpleHillClimbing.SimpleHillClimbingWithRestart(TSP, Restart_Count)
tsp = SteepestAscendHillClimbing.SteepestAscendHillClimbingWithRestart(TSP, Restart_Count)

stop_time = datetime.datetime.now()

print('Start Time: ' + str(start_time))
print('Stop Time: ' + str(stop_time))
print('Time Taken: ' + str(stop_time - start_time))

print('Orignal Cost : ' + str(TSP.get_hn()))
print('New Cost : ' + str(tsp.get_hn()))
tsp.PlotPath()
