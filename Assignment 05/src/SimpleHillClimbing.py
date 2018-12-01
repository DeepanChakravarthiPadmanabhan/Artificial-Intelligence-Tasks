
def SimpleHillClimbingWithRestart(TSP, restartCount):
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
        successor = tsp.GetRightSuccessorAt(i)
        successor_heuristic = successor.get_hn()

        if(orignal_heuristic < successor_heuristic):
            return tsp

        tsp = successor
        i+=1
