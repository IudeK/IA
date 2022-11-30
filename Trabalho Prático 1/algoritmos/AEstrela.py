from entidades.Jogo import Jogo
from entidades.utils.enums import Direction
from entidades.utils.FuncoesTabuleiro import FuncoesTabuleiro
from heuristicas.ManhattanDistance import manhattanDistance
from heapq import heappush, heappop
from testes.configuracoes import *
import time
import psutil


class AEstrela:
    def __init__(self, initialBoard=[]):
        self.game = Jogo(initialBoard)
        self.nodeStackBackup = list()
        self.listVisited = list()
        self.heap = []
        self.qtdGeneratedNodes = 0
        self.qtdStoredNodes = 0

    def adicionar_novo_no(self, node):
        h = manhattanDistance(node)
        g = len(node)  # custo do caminho do nó inicial até o nó n
        f = g + h

        heappush(self.heap, (f, node))
        self.qtdStoredNodes += 1

    def mover_verificar(self, node, direction: Direction) -> bool:
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

        self.adicionar_novo_no(nodeMoved)
        return isFound

    def escolher_melhor_caminho(self):
        # Removendo o menor valor da pilha
        currentNode = heappop(self.heap)[1] if len(
            self.heap) != 0 else self.nodeStackBackup.pop()

        # Esvazia a heap e armazenar em uma pilha para resolver futuros conflitos
        length = len(self.heap) - 1
        while length >= 0:
            self.nodeStackBackup.append(self.heap.pop(length)[1])
            length -= 1

        self.listVisited.append(currentNode)
        self.game.printNodeAndInformation(currentNode)

        return currentNode

    def iniciar(self):

        currentNode = self.game.getInitialState()

        print("tabuleiro Inicial:")
        self.game.print(currentNode)
        print(" --------------- ")

        time0 = time.time()

        if not self.game.isSolvable():
            print("Este tabuleiro não possui solução!")
            return

        heappush(self.heap, (16, currentNode))
        self.qtdStoredNodes += 1
        self.qtdGeneratedNodes += 1

        isFound = self.game.isCheckIfFinalState(currentNode)

        while not isFound:
            currentNode = self.escolher_melhor_caminho()
            self.heap = []

            for direction in Direction:
                if isFound:
                    break

                isFound = self.mover_verificar(currentNode, direction)

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
    estrela = AEstrela(TabelasIniciais[0]["tabuleiro"])
    estrela.iniciar()
elif escolha == '2':
    estrela = AEstrela(TabelasIniciais[1]["tabuleiro"])
    estrela.iniciar()
else:
    print("Valor inválido")
