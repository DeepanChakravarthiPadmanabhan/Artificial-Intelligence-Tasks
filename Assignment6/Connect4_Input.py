import sys
import numpy as np
import Node

CUTOFF_DEPTH = 3
LOG_ALPHABETAPRUNE = False

# self.rows=int(input("Enter the number of rows\n"))
# self.columns=int(input("Enter the number of columns"))
# self.chartowin=int(input("Enter the threshold to win"))
# self.user1=input("Enter the user 1 character between A-Z")
# self.user2=input("Enter the user 2 character between A-Z")
# self.user1=self.user1.upper()
# self.user2=self.user2.upper()

class Connect4:
    def __init__(self):
        self.rows=int(input("Enter the number of rows"))
        self.columns=int(input("Enter the number of columns"))
        self.chartowin=int(input("Enter the threshold to win"))

        self.user1=input("Enter the user 1 character between A-Z")
        self.user2=input("Enter the user 2 character between A-Z")
        self.user1=self.user1.upper()
        self.user2=self.user2.upper()
        self.winflag=False
        self.board= np.full((self.rows,self.columns),'|')
        print(self.board)
        self.winner=None

        # For Evaluation Purposes
        self.NodeBoardEvaluator = Node.Node(np.copy(self.board), self.rows, self.columns, self.chartowin, self.user1, self.user2)
        # self.user1 is the person playing the game while self.user2 is the computer playing

    def fill_board(self):
        self.winflag=False
        self.fillrow=self.rows-1
        self.occupied=False
        while(self.winflag!=True):


            if self.occupancycheck():
                break
            else:
                self.inputuser1 = int(input('Enter the column of User1 insertion'))
                self.validentry(self.inputuser1,1)
                self.board=self.insert(1)
                # For Evaluation Purposes
                self.NodeBoardEvaluator.insertAt(self.inputuser1, self.user1)
                print(self.board)
                self.wincheck(1)
                if self.winflag==True:
                    print("Flagloop")
                    if self.winner == 1:
                        print("User1 is the winner")
                    else:
                        print("User2 is the winner")
                    break

            if self.occupancycheck():
                break
            else:
                # self.inputuser2 = int(input('Enter the column of User2 insertion'))
                # self.validentry(self.inputuser2,2)
                # self.board=self.insert(2)
                # For Evaluation Purposes
                self.inputuser2 = self.EsitmateNextPosition(self.NodeBoardEvaluator, self.user2)
                self.board = self.insert(2)
                self.NodeBoardEvaluator.insertAt(self.inputuser2, self.user2)

                print(self.board)

                self.wincheck(2)
                if self.winflag==True:
                    if self.winner == 1:
                        print("User1 is the winner")
                    else:
                        print("User2 is the winner")
                    break


    def occupancycheck(self):
        if '|' in self.board:
            return False
        else:
            return True


    def wincheck(self,usernumber):
        print("Atwincheck")
        if usernumber==1:
            flag1=self.checkhorizontal(self.user1)
            flag2=self.checkvertical(self.user1)
            flag3=self.rightdiagonal(self.user1)
            flag4=self.leftdiagonal(self.user1)
            if (flag1 or flag2 or flag3 or flag4)==True:
                print("Hey1")
                self.winflag=True
                self.winner=1
                return None
            else:
                print("Hey1else")
                return None

        elif usernumber==2:
            flag1=self.checkhorizontal(self.user2)
            flag2=self.checkvertical(self.user2)
            flag3=self.rightdiagonal(self.user2)
            flag4=self.leftdiagonal(self.user2)
            if (flag1 or flag2 or flag3 or flag4)==True:
                print("Hey2")
                self.winflag=True
                self.winner=2
            return None
        else:
            print("Hey2else")
            return None

    def checkhorizontal(self, user):
        end = self.board.shape[1] - self.chartowin + 1

        for n, i in enumerate(self.board):
            # print("n=", n)
            for m, j in enumerate(i):
                if m < end:
                    # print("m=", m)
                    if self.board[n, m] == self.board[n, m + 1] == self.board[n, m + 2] == self.board[n, m + 3]==user:
                        flag = True
                        return flag
                    else:
                        flag = False
        return flag

    def checkvertical(self, user):
        end = self.board.shape[0] - self.chartowin + 1

        for n, i in enumerate(self.board):
            # print("n=", n)
            for m, j in enumerate(i):
                if n < end:
                    # print("m=", m)
                    if self.board[n, m] == self.board[n + 1, m] == self.board[n + 2, m] == self.board[n + 3, m]==user:
                        flag = True
                        return flag
                    else:
                        flag = False
        return flag

    def leftdiagonal(self, user):
        endrow = self.board.shape[0] - self.chartowin + 1
        endcol = self.board.shape[1] - self.chartowin + 1

        for n, i in enumerate(self.board):
            # print("n=", n)
            if n < endrow:
                for m, j in enumerate(i):
                    if m < endcol:
                        # print("m=", m)
                        if self.board[n, m] == self.board[n + 1, m + 1] == self.board[n + 2, m + 2] == self.board[n + 3, m + 3]==user:
                            flag = True
                            return flag
                        else:
                            flag = False
        return flag

    def rightdiagonal(self, user):
        endrow = self.board.shape[0] - self.chartowin + 1
        endcol = self.board.shape[1] - self.chartowin + 1
        for n, i in enumerate(self.board):
            # print("n=", n)
            if n < endrow:
                for m, j in enumerate(i[::-1]):
                    if m >= endcol:
                        # print("m=", m)
                        if self.board[n, m] == self.board[n + 1, m - 1] == self.board[n + 2, m - 2] == self.board[n + 3, m - 3]==user:
                            flag = True
                            return flag
                        else:
                            flag = False
        return flag

    def insert(self,user):
        insertflag=False
        if (user==1):
            for n, k in enumerate(self.board[:, self.inputuser1 - 1][::-1]):
                if k == '|':
                    self.board[(self.rows - 1) - n, self.inputuser1 - 1] = self.user1
                    insertflag=True
                    return self.board
                    break
                else:
                    pass
            if insertflag==False:
                inputnew=int(input("Please select another position"))
                for n, k in enumerate(self.board[:, inputnew - 1][::-1]):
                    if k == '|':
                        self.board[(self.rows - 1) - n, inputnew - 1] = self.user1
                        insertflag=True
                        return self.board
                        break
                    else:
                        pass


        elif (user==2):
            for n, k in enumerate(self.board[:, self.inputuser2 - 1][::-1]):
                if k == '|':
                    self.board[(self.rows - 1) - n, self.inputuser2 - 1] = self.user2
                    insertflag = True
                    return self.board
                    break
                else:
                    pass
            if insertflag == False:
                inputnew = int(input("Please select another position"))
                for n, k in enumerate(self.board[:, inputnew - 1][::-1]):
                    if k == '|':
                        self.board[(self.rows - 1) - n, inputnew - 1] = self.user2
                        insertflag = True
                        return self.board
                        break
                    else:
                        pass

    def validentry(self,value,user):
        if(value>self.columns):
            if(user==1):
                self.inputuser1=int(input('Enter a valid column value'))
            else:
                self.inputuser2 = int(input('Enter a valid column value'))
            return True
        else:
            return True

    def EsitmateNextPosition(self, node, user):
        depth = 0
        alpha = np.NINF
        beta = np.Inf

        evaluation, index = self.AlphaBetaPrune(node, depth, alpha, beta, user)

        return index + 1


    def AlphaBetaPrune(self, node, depth, alpha, beta, user, isMax=True):
        if(node.SomeBodyHasWon == True or depth == CUTOFF_DEPTH):
            evaluation = node.Evaluate()
            message = 'Sombody has won : ' + str(node.SomeBodyHasWon) + ', Depth : ' + str(depth) + 'Evaluation : ' + str(evaluation)
            self.Log_AlphaBeta(message)
            return  evaluation, -1

        children = node.GenerateChildren(user)

        eval, index = 0, 0

        if (isMax):
            v = np.NINF
            for i, child in enumerate(children):
                value, notUsedIndex = self.AlphaBetaPrune(child, depth+1, alpha, beta, user, not isMax)
                v = min(v, value)
                eval = v
                index = i
                if (v > beta):
                    break
                    # return v
                alpha = max(v, alpha)
        else:
            v = np.Inf
            for i, child in enumerate(children):
                value, notUsedIndex = self.AlphaBetaPrune(child, depth+1, alpha, beta, user, not isMax)
                v = max(v, value)
                eval = v
                index = i
                if(v < alpha):
                    break
                    # return v
                beta = min(v, beta)

        return eval, index

    def Log(self, message):
        print(message)

    def Log_AlphaBeta(self, message):
        if LOG_ALPHABETAPRUNE:
            self.Log(message)

k=Connect4()
k.fill_board()

