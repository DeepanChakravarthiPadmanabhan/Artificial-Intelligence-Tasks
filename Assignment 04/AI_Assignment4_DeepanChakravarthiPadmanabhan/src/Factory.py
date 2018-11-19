from Enums import Heuristics
from Enums import Algorithms


class HeuristicFactory:

    def __init__(self, node):
        self.Node = node

    def GetHeuristicValue(self):
        heuristic = self.GetFactoryObject(self.Node.HeuristicType)
        return heuristic.GetHeuristicValue(self.Node.CurrentState, self.Node.GoalState)

    def GetFactoryObject(self, heuristicType):
        if(heuristicType == Heuristics.NUMBER_OF_TILES):
            return HeuristicNumberOfTiles()
        elif(heuristicType == Heuristics.MANHATTAN_DISTANCE):
            return HeuristicManhattanDistance()

        raise Exception('Invalid Heuristic type Provided : ' + str(heuristicType))


class HeuristicNumberOfTiles:

    def GetHeuristicValue(self, currentState, goalState):
        sumOfMisplacedTiles = 0

        for row, rowValue in enumerate(goalState.StateList):
            for column, columnValue in enumerate(rowValue):
                if(columnValue != currentState.StateList[row][column]):
                    sumOfMisplacedTiles + sumOfMisplacedTiles + 1

        return sumOfMisplacedTiles


class HeuristicManhattanDistance:

    def GetHeuristicValue(self, currentState, goalState):
        sumOfManhattanDistances = 0

        for row, rowValue in enumerate(goalState.StateList):
            for column, columnValue in enumerate(rowValue):
                currentPositionOfValue = currentState.FindValueCoOrdinates(columnValue)
                sumOfManhattanDistances = sumOfManhattanDistances + abs(row-currentPositionOfValue[0]) + abs(column - currentPositionOfValue[1])

        return  sumOfManhattanDistances


class AlgorithmFactory:

    def __init__(self, node):
        self.Node = node

    def Get_fn(self):
        algorithm = self.GetFactoryObject(self.Node, self.Node.AlgorithmType)
        return algorithm.Get_fn()

    def GetFactoryObject(self, node, algorithmType):
        if(algorithmType == Algorithms.GREEDY):
            return AlgorithmGreedy(node)
        elif(algorithmType == Algorithms.A_STAR):
            return AlgorithmAStar(node)

        raise Exception('Invalid Algorithm type Provided : ' + str(algorithmType))


class AlgorithmGreedy:

    def __init__(self, node):
        self.Node = node

    def Get_fn(self):
        return self.Node.Get_hn()


class AlgorithmAStar:

    def __init__(self, node):
        self.Node = node

    def Get_fn(self):
        return self.Node.Get_gn() + self.Node.Get_hn()

