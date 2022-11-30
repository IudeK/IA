from entidades.Jogo import Jogo
from entidades.utils.enums import Direction
from entidades.utils.FuncoesTabuleiro import FuncoesTabuleiro
from heuristicas.ManhattanDistance import manhattanDistance
from heapq import heappush, heappop
from testes.configuracoes import *
import time
import psutil


class BuscaGulosa:
    def __init__(self, initialBoard=[]):
        self.game = Jogo(initialBoard)
        self.nodeStackBackup = list()
        self.listVisited = list()
        self.heap = []
        self.qtdGeneratedNodes = 0
        self.qtdStoredNodes = 0

    def addNewNode(self, node):
        h = manhattanDistance(node)
        heappush(self.heap, (h, node))
        self.qtdStoredNodes += 1

    def moveAndCheck(self, node, direction: Direction) -> bool:
        nodeMoved = FuncoesTabuleiro.tentar_mover(node, direction)

        if nodeMoved is None:
            return False

        self.qtdGeneratedNodes += 1

        if nodeMoved in self.listVisited:
            return False

        isFound = self.game.isCheckIfFinalState(nodeMoved)

        if isFound:
            self.game.printNodeAndInformation(nodeMoved)
            return True

        self.addNewNode(nodeMoved)

        return isFound

    def getBestWay(self):
        """Removendo o menor valor da pilha"""
        currentNode = heappop(self.heap)[1] if len(
            self.heap) != 0 else self.nodeStackBackup.pop()

        """Esvazia a heap e armazenar em uma pilha para resolver futuros conflitos"""
        length = len(self.heap) - 1
        while length >= 0:
            self.nodeStackBackup.append(self.heap.pop(length)[1])
            length -= 1

        self.listVisited.append(currentNode)
        self.game.printNodeAndInformation(currentNode)

        return currentNode

    def iniciar(self):

        currentNode = self.game.getInitialState()

        print("Tabuleiro Inicial:")
        self.game.print(currentNode)
        print(" --------------- ")

        time0 = time.time()

        if (not self.game.isSolvable()):
            print("Este tabuleiro não possui solução!")
            return

        heappush(self.heap, (2, currentNode))
        self.qtdStoredNodes += 1
        self.qtdGeneratedNodes += 1

        isFound = self.game.isCheckIfFinalState(currentNode)

        while (not isFound):
            currentNode = self.getBestWay()
            self.heap = []

            for direction in Direction:
                if (isFound):
                    break

                isFound = self.moveAndCheck(currentNode, direction)

        time1 = time.time()

        print("------------------------- Algoritmo Finalizado ------------------------")
        print(f"Quantidade de movimentos: {self.game.getCountMove()}")

        print(f"Quantidade de nós Gerados: {self.qtdGeneratedNodes} ")
        print(f"Quantidade de nós Armazenados: {self.qtdStoredNodes} ")

        print("Tempo de execução: ", time1 - time0)
        print(f"CPU em %: {psutil.cpu_percent()}")
        print(f"Uso de memória: {psutil.virtual_memory()._asdict()}")


escolha = input("Digite '1' para escolher a primeira opção de entrada e '2' para a segunda: ")
if escolha == '1':
    guloso = BuscaGulosa(TabelasIniciais[0]["tabuleiro"])
    guloso.iniciar()
elif escolha == '2':
    guloso = BuscaGulosa(TabelasIniciais[1]["tabuleiro"])
    guloso.iniciar()
else:
    print("Valor inválido")
