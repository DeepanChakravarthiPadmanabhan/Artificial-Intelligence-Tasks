from Enums import Positions
import Helper
import State
import Statistics
import Factory

class FrontierNode():

    def __init__(self, parent, currentState, goalState, algorithmType, heuristicType):
        self.Parent = parent
        self.CurrentState = currentState
        self.GoalState = goalState
        if self.Parent is None :
            self.g_n = 0
        else:
            self.g_n = self.Parent.Get_gn() + 1
        self.AlgorithmType = algorithmType
        self.HeuristicType = heuristicType
        self.IsExtimatedCostCalculated = False
        self.f_n = None
        self.h_n = None
        self.Get_fn()

    def __eq__(self, other):
        return self.CurrentState == other.CurrentState and self.Get_fn() >= other.Get_fn()

    def __str__(self):
        return str(self.CurrentState)

    def Get_fn(self):
        if(self.f_n is None):
            algorithmFactory = Factory.AlgorithmFactory(self)
            self.f_n = algorithmFactory.Get_fn()
        return self.f_n


    def Get_gn(self):
        return self.g_n

    def Get_hn(self):
        if(self.h_n is None):
            heuristicFactory = Factory.HeuristicFactory(self)
            self.h_n = heuristicFactory.GetHeuristicValue()
        return self.h_n

    def ExpandNode(self):
        listOfExpandedNodes = []
        if(self.TryAddExapnasionToList(Positions.RIGHT, listOfExpandedNodes)):
            Statistics.Instance.NumberOfExtensions +=1

        if(self.TryAddExapnasionToList(Positions.LEFT, listOfExpandedNodes)):
            Statistics.Instance.NumberOfExtensions +=1

        if(self.TryAddExapnasionToList(Positions.BOTTOM, listOfExpandedNodes)):
            Statistics.Instance.NumberOfExtensions +=1

        if(self.TryAddExapnasionToList(Positions.TOP, listOfExpandedNodes)):
            Statistics.Instance.NumberOfExtensions +=1

        return listOfExpandedNodes

    def TryAddExapnasionToList(self, position, listOfExpandedNodes):
        if( not self.CurrentState.isShiftOperationPossible(position)):
            return False

        newStateList = Helper.DeepCopy2dArray(self.CurrentState.StateList)
        newState = State.State(newStateList, self.CurrentState.EmptyValue)
        newState.PerformShiftOperation(position)
        newNode = FrontierNode(self, newState, self.GoalState, self.AlgorithmType, self.HeuristicType)
        listOfExpandedNodes.append(newNode)
        return True


class Frontier:
    def __init__(self):
        self.MeasuredItemsList = []
        self.FrontierNodeManagementList = []

    def PushNode(self, frontierNode):
        if(not frontierNode in self.MeasuredItemsList):
            self.MeasuredItemsList.append(frontierNode)
            self.FrontierNodeManagementList.append(frontierNode)
            # self.FrontierNodeManagementList.sort(key=lambda x: x.Get_fn())
            self.FrontierNodeManagementList.sort(key=lambda x:x.Get_fn())
            Statistics.Instance.Enqeues +=1
        else:
            Statistics.Instance.NumberOfInsertionRejectionsDueToAlreadyAvailability +=1


    def PopNode(self):
        Statistics.Instance.Deqeues +=1
        return self.FrontierNodeManagementList.pop(0)

    def isEmpty(self):
        return self.Size() == 0

    def Size(self):
        return len(self.FrontierNodeManagementList)

    def ResetFrontier(self):
        self.MeasuredItemsList = []
        self.FrontierNodeManagementList = []

    def __contains__(self, item):
        return item in self.MeasuredItemsList


