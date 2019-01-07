import numpy as np
from copy import copy, deepcopy

class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

class Node:

    def __init__(self, board, rows, columns, charsToWin, user1, user2, userStructure=None):
        self.rows = rows
        self.columns = columns
        self.board = board
        self.charsToWin = charsToWin
        self.userStructure = userStructure
        self.user1 = user1
        self.user2 = user2
        self.somebodyHasWon = False
        if(self.userStructure is None):
            self.userStructure = {user1 : { 'board' : {'horizontal': [], 'vertical' : [] , 'leftDiagonal': [],
                                                       'rightDiagonal': []},
                                            'count' : {},
                                            'evaluation' : 0 },
                                  user2: {'board': {'horizontal': [], 'vertical': [], 'leftDiagonal': [],
                                                    'rightDiagonal': []},
                                          'count': {},
                                            'evaluation' : 0 }
                                  }


    def GenerateChildren(self, user):
        list_of_children = []
        list_of_columns = []

        for i in range(self.columns):
            # if column is full then no further child can be added at that position
            if '|' not in self.board[:, i]:
                continue

            child = self.clone()
            child.insertAt(i+1, user)
            list_of_children.append(child)
            list_of_columns.append(i)

        return  list_of_children, list_of_columns

    def clone(self):
        return Node(np.copy(self.board), self.rows, self.columns, self.charsToWin, self.user1, self.user2, deepcopy(self.userStructure))

    def insertAt(self, column, user):
        row = -1
        for n, k in enumerate(self.board[:, column - 1][::-1]):
            if k == '|':
                row = (self.rows - 1) - n
                self.board[(self.rows - 1) - n, column - 1] = user
                break

        # Update Evaluator data structure
        col = column - 1

        self.UpdateBoard(user, row, col)

    def Evaluate(self):
        # if self.somebodyHasWon:
        #     if(self.userStructure[self.user1]['evaluation'] == np.NINF):
        #         return np.NINF
        #     else:
        #         return np.Inf

        return (self.userStructure[self.user2]['evaluation'] - self.userStructure[self.user1]['evaluation']) * 1.0


    def SomeBodyHasWon(self):
        # Update value in case somebody has won
        #self.somebodyHasWon = False
        return self.somebodyHasWon

    def CheckIfPositionExists(self, user, key, position):
        list_dimensions = self.userStructure[user]['board'][key]

        for n, k in enumerate(list_dimensions):
            if position in k:
                return True, self.userStructure[user]['board'][key].pop(n)

        return False, []

    def UpdateBoard(self, user, row, column):
        self.InsertIntoLevel(user, 'horizontal', Position(row, column), Position(row, column-1), Position(row, column+1))
        self.InsertIntoLevel(user, 'vertical', Position(row, column), Position(row-1, column), Position(row+1, column))
        self.InsertIntoLevel(user, 'leftDiagonal', Position(row, column), Position(row-1, column-1), Position(row+1, column+1))
        self.InsertIntoLevel(user, 'rightDiagonal', Position(row, column), Position(row+1, column-1), Position(row-1, column+1))

    #     self.InsertIntoHorizontalLevel(user, row, column)
    #
    # def InsertIntoHorizontalLevel(self, user, row, column):
    #     key = 'horizontal'
    #     list_of_neighbours = []
    #
    #     if(column + 1 != self.columns):
    #         list_of_neighbours.append(Position(row, column + 1))
    #     if(column - 1 != -1):
    #         list_of_neighbours.append(Position(row, column - 1))
    #
    #     bool_position1, list_position1 = self.CheckIfPositionExists(user, key, list_of_neighbours[0])
    #     bool_position2, list_position2 = self.CheckIfPositionExists(user, key, list_of_neighbours[1])
    #     if(bool_position1 and bool_position2):
    #         self.DecreamentCounter(self, user, len(list_position1))
    #         self.DecreamentCounter(self, user, len(list_position2))
    #
    #         list_position1.insert(0, Position(row, column))
    #         newList = list_position2 + list_position1
    #
    #         self.IncreamentCounter(user, len(newList))
    #
    #         self.userStructure[user][key].append(newList)
    #
    #     elif(bool_position1):
    #         self.DecreamentCounter(self, user, len(list_position1))
    #
    #         list_position1.insert(0, Position(row, column))
    #         newList = list_position2 + list_position1
    #
    #         self.IncreamentCounter(user, len(newList))
    #
    #         self.userStructure[user][key].append(newList)

    def InsertIntoLevel(self, user, key, insertPosition, leftTopAppendPosition, rightBottomAppendPosition):
        bool_position1, list_position1 = False, []
        bool_position2, list_position2 = False, []

        if(self.isValidPosition(leftTopAppendPosition)):
            bool_position1, list_position1 = self.CheckIfPositionExists(user, key, leftTopAppendPosition)
        if(self.isValidPosition(rightBottomAppendPosition)):
            bool_position2, list_position2 = self.CheckIfPositionExists(user, key, rightBottomAppendPosition)

        if (bool_position1 and bool_position2):
            self.DecreamentCounter(user, len(list_position1))
            self.DecreamentCounter(user, len(list_position2))

            list_position1.append(insertPosition)
            newList = list_position1 + list_position2

            winnable = self.CheckIfWinnableList(key, newList)

            if(winnable > 0 or len(newList) >= self.charsToWin):
                self.IncreamentCounter(user, len(newList))

                self.userStructure[user]['board'][key].append(newList)

        elif (bool_position1):
            self.DecreamentCounter(user, len(list_position1))

            list_position1.append(insertPosition)

            winnable = self.CheckIfWinnableList(key, list_position1)

            if (winnable > 0 or len(list_position1) >= self.charsToWin):
                self.IncreamentCounter(user, len(list_position1))

                self.userStructure[user]['board'][key].append(list_position1)

        elif (bool_position2):
            self.DecreamentCounter(user, len(list_position2))

            list_position2.insert(0, insertPosition)

            winnable = self.CheckIfWinnableList(key, list_position2)

            if (winnable > 0 or len(list_position2) >= self.charsToWin):
                self.IncreamentCounter(user, len(list_position2))

                self.userStructure[user]['board'][key].append(list_position2)

        else:
            list_single = [insertPosition]

            winnable = self.CheckIfWinnableList(key, list_single)

            if (winnable > 0 or len(list_single) >= self.charsToWin):
                self.IncreamentCounter(user, len(list_single))

                self.userStructure[user]['board'][key].append(list_single)



    def DecreamentCounter(self, user, counter_number):
        self.userStructure[user]['count'][counter_number] -= 1
        self.userStructure[user]['evaluation'] -= 4*10**counter_number

    def IncreamentCounter(self, user, counter_number):
        if counter_number in self.userStructure[user]['count'].keys():
            self.userStructure[user]['count'][counter_number] += 1
        else:
            self.userStructure[user]['count'][counter_number] = 1

        self.userStructure[user]['evaluation'] += 4*10**counter_number

        if(counter_number >= self.charsToWin and self.userStructure[user]['count'][counter_number] > 0):
            # print('blah blah')
            self.somebodyHasWon = True
            # if(user == self.user1):
            #     self.userStructure[user]['evaluation'] = np.Inf
            # else:
            #     self.userStructure[user]['evaluation'] = np.NINF

    def isValidPosition(self, position):
        if not (position.row >= 0 and position.row < self.rows):
            return False
        if not (position.column >= 0 and position.column < self.columns):
            return False

        return True

    def PrintCounter(self, user):
        print(str(self.userStructure[user]['count']))

    def CheckIfWinnableList(self, key, list):
        winnable = 0

        positions = self.GetValidNeighboursList(key, list)

        for position in positions:
            if self.board[position.row][position.column] == '|':
                winnable+=1

        return  winnable

    def GetValidNeighboursList(self, key,list):
        listofPositions = self.GetNeighboursList(key, list)
        positions = []

        for position in listofPositions:
            if self.isValidPosition(position):
                positions.append(position)

        return  positions

    def GetNeighboursList(self, key, list):
        listofPositions = []
        if(key == 'horizontal'):
            listofPositions.append(Position(list[0].row, list[0].column - 1))
            listofPositions.append(Position(list[-1].row, list[-1].column + 1))
        elif key == 'vertical':
            listofPositions.append(Position(list[0].row - 1, list[0].column))
            listofPositions.append(Position(list[-1].row + 1, list[-1].column))
        elif key == 'leftDiagonal':
            listofPositions.append(Position(list[0].row - 1, list[0].column - 1))
            listofPositions.append(Position(list[-1].row + 1, list[-1].column + 1))
        elif key == 'rightDiagonal':
            listofPositions.append(Position(list[0].row + 1, list[0].column - 1))
            listofPositions.append(Position(list[-1].row - 1, list[-1].column + 1))

        return listofPositions