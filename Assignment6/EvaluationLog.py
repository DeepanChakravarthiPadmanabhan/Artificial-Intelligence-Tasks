
class EvaluationLog:
    def __init__(self, parent = None, depth = 0, isMax = True):
        self.somebodyHasWon = False
        self.depth = depth
        self.children = []
        self.ChildEvaluationResult = 0
        self.index = -1
        self.isMax = isMax
        self.OrignalEvaluation = 0
        self.board = []
        if depth == 0:
            self.parent = None
        else:
            self.parent = parent

    def SetSomebodyHasWon(self, value, setParent = False):
        self.somebodyHasWon = value
        if(self.parent is not None and setParent):
            self.parent.SetSomebodyHasWon(value)

    def SetSomebodyHasWon(self, value):
        self.somebodyHasWon = value

    def SetEvaluation(self, evaluation):
        self.ChildEvaluationResult = evaluation

    def SetOrignalEvaluation(self, evaluation):
        self.OrignalEvaluation = evaluation

    def AddChild(self, child):
        self.children.append(child)

    def SetIndex(self, index):
        self.index = index

    def SetBoard(self, board):
        self.board = board


    def printLog(self):
        message = ''
        for i in range(self.depth):
            message += '\t'

        board = message + 'board : ' + str(self.getBoardString())

        if(self.isMax):
            message += 'Max : '
        else:
            message += 'Min : '

        message += 'Sombody has won : ' + str(self.somebodyHasWon) + ', Depth : ' + str(
            self.depth) + ', Evaluation : ' + str(self.ChildEvaluationResult) + ', Index : ' + str(self.index) + ', Orignal Evaluation : ' + str(self.OrignalEvaluation) \
        + '\n ' + board
        print(message)
        for child in self.children:
            child.printLog()

    def getBoardString(self):
        board_str = '['
        for i,j in enumerate(self.board):
            board_str+= '['
            for m, n in enumerate(j):
                board_str += n
            board_str+=']'
        board_str+=']'
        return  board_str

