import State
import Helper
import Frontiers
import Statistics

import datetime

class PathFinder:

    def __init__(self, frontier, algorithm, heuristic):
        self.Algorithm = algorithm
        self.Heuristic = heuristic
        self.Frontier = frontier
        Statistics.Instance.Algorithm = self.Algorithm
        Statistics.Instance.Heuristic = self.Heuristic

    def FindPath(self, initialState, goalState, emptyValue):
        Statistics.Instance.StartTime = datetime.datetime.now()
        goalNode = self.GetGoalNode(initialState, goalState, emptyValue)
        Statistics.Instance.EndTime = datetime.datetime.now()
        if(goalNode is None):
            raise Exception("Could not find goal state. Invalid state provided")

        goalPath = []
        node = goalNode
        while(not node is None):
            goalPath.append(node)
            node = node.Parent
        goalPath = goalPath[::-1]

        for node in goalPath:
            print(node)

        Statistics.Instance.GoalPathLength = len(goalPath)
        Statistics.Instance.GoalNodePathCost_fn = goalNode.Get_fn()
        Statistics.Instance.GoalNodePathCost_gn = goalNode.Get_gn()
        Statistics.Instance.GoalNodePathCost_hn = goalNode.Get_hn()

        print(str(Statistics.Instance))


    def GetGoalNode(self, initialState, goalState, emptyValue):
        state_intitialState = State.State(Helper.DeepCopy2dArray(initialState), emptyValue)
        self.state_goalState = State.State(goalState, emptyValue)
        startNode = Frontiers.FrontierNode(None, state_intitialState, self.state_goalState, self.Algorithm, self.Heuristic)
        self.Frontier.PushNode(startNode)
        return self.PerformGoalSearchOperation()

    def PerformGoalSearchOperation(self):
        while(not self.Frontier.isEmpty()):
            node = self.Frontier.PopNode()
            if(node.CurrentState == self.state_goalState):
                return node
            listOfExpandedNodes = node.ExpandNode()
            self.AddListOfNodeToFrontier(listOfExpandedNodes)

        return None

    def AddListOfNodeToFrontier(self, listOfNodes):
        for node in listOfNodes:
            self.Frontier.PushNode(node)



