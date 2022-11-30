from random import choice
from entidades.utils.constante import BLANK_SYMBOL


class Tabuleiro:
    def __init__(self, initialState=[], size=4):
        self.size = size
        self.blankSimbol = BLANK_SYMBOL
        self.initialState = initialState or list([])
        self.finalState = list([])

        self.startBoard()

    def startBoard(self):
        self.finalState = self.createFinalState()
        print("Estado Final: ", self.finalState)

        if not self.initialState:
            self.initialState = self.createInitialState()

    def createFinalState(self):
        limitNumber = self.size**2
        listNumbers = list(range(1, limitNumber))

        finalState = list()
        count = 1

        for i in range(0, limitNumber, self.size):
            limit = self.size * count

            if limit == limitNumber:
                temp = listNumbers[i:(limit-1)]
                temp.append(0)
                finalState.append(temp)
            else:
                finalState.append(listNumbers[i:limit])
            count += 1

        return finalState

    def createInitialState(self):
        limitNumber = self.size**2
        listNumbers = list(range(limitNumber))

        boardRandom = list()

        for i in range(self.size):
            boardRandom.append([])

            for j in range(self.size):
                number = choice(listNumbers)
                listNumbers.remove(number)
                boardRandom[i].append(number)

        return boardRandom

    def printFinalState(self):
        self.print(self.finalState)

    def printInitialState(self):
        self.print(self.initialState)

    def print(self, board):
        matrizView = ""

        for i in range(self.size):
            linha = board[i]
            for j in range(self.size):
                matrizView += "{} ".format(linha[j])

            matrizView += "\n"
        print(matrizView)

    def __str__(self):
        return self.printFinalState()

    def getInitialState(self):
        return self.initialState

    def getFinalState(self):
        return self.finalState

    def getBlankSimbol(self):
        return self.blankSimbol

    def getBoardSize(self):
        return self.size
