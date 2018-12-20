
import datetime
import math
import random

def SimulatedAnnealing(tsp, time_to_execute):
    best_solution = tsp
    best_cost = tsp.get_hn()
    current_tsp = tsp
    current_tsp_cost = current_tsp.get_hn()
    iteration = 1

    dE = 0

    start_time = datetime.datetime.now()

    while True:
        Temperature = getTemperature(dE, time_to_execute)
        # newTSP = current_tsp.GetNewTSP()
        # newTSP.Randomize()
        newTSP = current_tsp.GetRightSuccessorAt(iteration%current_tsp.GetCityCount())
        #newTSP_list = current_tsp.GetAllSuccessors(iteration%current_tsp.GetCityCount())
        #newTSP = newTSP_list[random.randint(0, current_tsp.GetCityCount() - 2)]
        #newTSP = min(newTSP_list, key=lambda s:s.get_hn())
        newTSP_cost = newTSP.get_hn()
        dE = newTSP_cost - current_tsp_cost
        # dE = current_tsp_cost - newTSP_cost

        try:
            # prob = math.exp(-1/(time_to_execute-(datetime.datetime.now() - start_time)))
            prob = math.exp(-datetime.timedelta(seconds=time_to_execute)/(datetime.timedelta(seconds=time_to_execute)-(datetime.datetime.now() - start_time)))
            #print(prob)
        except Exception as e:
            print(e)
            prob=0.0
            #print(prob)

        # try:
        if(dE < 0):
            current_tsp = newTSP
            current_tsp_cost = current_tsp.get_hn()
            if(current_tsp_cost < best_cost):
                best_solution = current_tsp
                best_cost = current_tsp_cost
        elif (prob > random.random()):
            current_tsp = newTSP
            current_tsp_cost = newTSP_cost
        #
        if(prob == 0):
            break

        if(datetime.datetime.now() - start_time > datetime.timedelta(seconds=time_to_execute)):
            break

        iteration += 1

    return best_solution


def getTemperature(dE, time_to_execute):
    # return 10.0*(0.9**iteration)
    return -dE / math.log(time_to_execute)