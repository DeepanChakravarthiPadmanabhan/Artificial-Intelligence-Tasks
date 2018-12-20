import TravellingSalesPerson
import City
import SimpleHillClimbing
import SteepestAscendHillClimbing
import SimulatedAnnealing
import Config

import datetime

#filename = './Cities/49_cities.txt'
filename = Config.filename
Restart_Count = Config.Restart_Count
Time_To_Execute_Min = Config.Time_To_Execute_Min
Time_To_Execute_Sec = Time_To_Execute_Min * 60

TSP = TravellingSalesPerson.TravellingSalePerson()

with open(filename) as file:
    next(file)
    for line in file:
        city, lat, lon = line.strip('\n').split(',')
        TSP.AddCity(City.City(city, float(lat), float(lon)))

start_time = datetime.datetime.now()

if(Config.Algorithm == Config.Algorithm_Options[0]):
    tsp = SimpleHillClimbing.SimpleHillClimbingWithRestart(TSP, Restart_Count)
elif (Config.Algorithm == Config.Algorithm_Options[1]):
    tsp = SteepestAscendHillClimbing.SteepestAscendHillClimbingWithRestart(TSP, Restart_Count)
elif (Config.Algorithm == Config.Algorithm_Options[2]):
    tsp = SimulatedAnnealing.SimulatedAnnealing(TSP, Time_To_Execute_Sec)

stop_time = datetime.datetime.now()

print('Start Time: ' + str(start_time))
print('Stop Time: ' + str(stop_time))
print('Time Taken: ' + str(stop_time - start_time))

print('Orignal Cost : ' + str(TSP.get_hn()))
print('New Cost : ' + str(tsp.get_hn()))
tsp.PlotPath()
