from Enums import Positions

class State:
    def __init__(self, stateList, emptyValue):
        self.StateList = stateList
        self.EmptyValue = emptyValue
        self.EmptyCoOrdinates = (-1, -1)

    def __eq__(self, other):
        if(len(self.StateList) != len(other.StateList)):
            # Rows count do not match. Return false
            return False

        for i in range(0, len(self.StateList)):
            if (len(self.StateList[i]) != len(other.StateList[i])):
                # Columns count do not match. Return false
                return False

            for j in range(0, len(self.StateList[i])):
                if(self.StateList[j] != other.StateList[j]):
                    # Items do not match at position (i,j)
                    return False

        # All conditions of a 2d array have passed
        return True

    def __str__(self):
        str_state = ''
        for row in self.StateList:
            str_state = str_state + ' '.join([str(x) for x in row]) + '\n'

        return str_state

    def GetEmptyCoOrdinates(self):
        if(self.EmptyCoOrdinates == (-1,-1)):
            self.SetEmptyCoOrdinates(self.FindEmptyValueCoOrdinates())

        return self.EmptyCoOrdinates

    def FindValueCoOrdinates(self, value):
        for i in range(0, len(self.StateList)):
            for j in range(0, len(self.StateList[i])):
                if self.StateList[i][j] == value:
                    return (i,j)

        raise Exception('Error: Cannot find position for: '+ str(value))

    def FindEmptyValueCoOrdinates(self):
        return self.FindValueCoOrdinates(self.EmptyValue)

    def SetEmptyCoOrdinates(self, position):
        self.EmptyCoOrdinates = position

    def PerformShiftOperation(self, position):
        if(not self.isShiftOperationPossible(position)):
            raise Exception('Invalid Shift operation requested')

        emptyPosition = self.GetEmptyCoOrdinates()

        if (position == Positions.RIGHT):
            self.Replace(emptyPosition, (emptyPosition[0], emptyPosition[1] + 1))
            self.SetEmptyCoOrdinates((emptyPosition[0], emptyPosition[1] + 1))

        elif (position == Positions.LEFT):
            self.Replace(emptyPosition, (emptyPosition[0], emptyPosition[1] - 1))
            self.SetEmptyCoOrdinates((emptyPosition[0], emptyPosition[1] - 1))

        elif (position == Positions.TOP):
            self.Replace(emptyPosition, (emptyPosition[0] - 1, emptyPosition[1]))
            self.SetEmptyCoOrdinates((emptyPosition[0] - 1, emptyPosition[1]))

        elif (position == Positions.BOTTOM):
            self.Replace(emptyPosition, (emptyPosition[0] + 1, emptyPosition[1]))
            self.SetEmptyCoOrdinates((emptyPosition[0] + 1, emptyPosition[1]))


    def isShiftOperationPossible(self, position):
        emptyPosition = self.GetEmptyCoOrdinates()

        if (position == Positions.RIGHT and emptyPosition[1] + 1 == len(
                self.StateList[emptyPosition[0]])):
            return False

        if (position == Positions.LEFT and emptyPosition[1] - 1 == -1):
            return False

        if (position == Positions.TOP and emptyPosition[0] - 1 == -1):
            return False

        if (position == Positions.BOTTOM and emptyPosition[0] + 1 == len(self.StateList)):
            return False

        return True

    def Replace(self, coordinates1, coordinates2):
        coordinates1_value = self.StateList[coordinates1[0]][coordinates1[1]]
        self.StateList[coordinates1[0]][coordinates1[1]] = self.StateList[coordinates2[0]][coordinates2[1]]
        self.StateList[coordinates2[0]][coordinates2[1]] = coordinates1_value



