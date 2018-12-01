
def SteepestAscendHillClimbingWithRestart(TSP, restartCount):
    listOfTSP = []
    for i in range(0, restartCount):
        listOfTSP.append(SimpleHillClimbing(TSP))

    return min(listOfTSP, key= lambda tsp: tsp.get_hn())


def SimpleHillClimbing(TSP):
    tsp = TSP.GetNewTSP()
    tsp.Randomize()
    i = 0

    while True:
        orignal_heuristic = tsp.get_hn()
        successors = tsp.GetAllSuccessors(i)
        successor = min(successors, key=lambda s:s.get_hn())
        successor_heuristic = successor.get_hn()

        if(orignal_heuristic < successor_heuristic):
            return tsp

        tsp = successor
        i+=1