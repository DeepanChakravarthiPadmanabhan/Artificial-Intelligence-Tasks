import sys
import Frontiers
import Enums
import Input
import PathFinder

arguments_length = len(sys.argv)

if(arguments_length < 3):
    raise Exception("Invalid number of arguments. Required : " + str(3) + ', Found: ' + str(arguments_length))

sys_AlgoType = sys.argv[1]
sys_HeuristicType = sys.argv[2]
# sys_AlgoType = 'A*'
# sys_HeuristicType = 'NUMBEROFTILES'

frontier = Frontiers.Frontier()
AlgorithmType = Enums.Algorithms.GREEDY
HeurisitcType = Enums.Heuristics.MANHATTAN_DISTANCE


if(str.upper(sys_AlgoType) == 'A*'):
    AlgorithmType = Enums.Algorithms.A_STAR
elif(str.upper(sys_AlgoType) == 'GREEDY'):
    AlgorithmType = Enums.Algorithms.GREEDY

if(str.upper(sys_HeuristicType) == 'NUMBEROFTILES' or str.upper(sys_HeuristicType) == 'TILES'):
    HeurisitcType = Enums.Heuristics.NUMBER_OF_TILES
elif(str.upper(sys_HeuristicType) == 'MANHATTANDISTANCE' or str.upper(sys_HeuristicType) == 'MANHATTAN'):
    HeurisitcType = Enums.Heuristics.MANHATTAN_DISTANCE

pathFinder = PathFinder.PathFinder(frontier, AlgorithmType, HeurisitcType)
pathFinder.FindPath(Input.StartState, Input.GoalState, Input.EmptyValue)

