import time
from queue import Queue

import psutil

from entidades.Jogo import Jogo
from entidades.utils.FuncoesTabuleiro import FuncoesTabuleiro
from entidades.utils.enums import Direction
from testes.configuracoes import *


class BuscaLargura:
    def __init__(self, initialBoard=[]):
        self.game = Jogo(initialBoard)
        self.checkQueue = Queue()
        self.listVisited = list()
        self.qtdGeneratedNodes = 0
        self.qtdStoredNodes = 0

    def mover_verificar(self, node, direction: Direction) -> bool:
        nodeMoved = FuncoesTabuleiro.tentar_mover(node, direction)
        if nodeMoved is None:
            return False
        
        self.qtdGeneratedNodes += 1

        if nodeMoved in self.listVisited:
            return False

        self.checkQueue.put(nodeMoved)
        self.listVisited.append(nodeMoved)
        self.qtdStoredNodes += 1
        self.game.printNodeAndInformation(nodeMoved)

        isFound = self.game.isCheckIfFinalState(nodeMoved)
        return isFound

    def iniciar(self):
        currentNode = self.game.getInitialState()

        print("Tabuleiro Inicial:")
        self.game.print(currentNode)
        print(" --------------- ")

        time0 = time.time()

        if not self.game.isSolvable():
            print("Este tabuleiro não possui solução!")
            return

        self.checkQueue.put(currentNode)
        self.listVisited.append(currentNode)
        self.qtdGeneratedNodes += 1
        self.qtdStoredNodes += 1

        isFound = self.game.isCheckIfFinalState(currentNode)

        while not isFound and not self.checkQueue.empty():
            currentNode = self.checkQueue.get() 

            for direction in Direction:
                if isFound:
                    break
                isFound = self.mover_verificar(currentNode, direction)

        time1 = time.time()

        print("------------------------- Algoritmo Finalizado ------------------------")
        print(f"Quantidade de movimentos: {self.game.getCountMove()}")

        print(f"Quantidade de nós Gerados: {self.qtdGeneratedNodes}")
        print(f"Quantidade de nós Armazenados: {self.qtdStoredNodes}")
        
        print("Tempo de execução: ", time1 - time0)
        print(f"CPU em %: {psutil.cpu_percent()}")
        print(f"Uso de memória: {psutil.virtual_memory()._asdict()}")


escolha = input("Digite '1' para escolher a primeira opção de entrada e '2' para a segunda: ")
if escolha == '1':
    largura = BuscaLargura(TabelasIniciais[0]["tabuleiro"])
    largura.iniciar()
elif escolha == '2':
    largura = BuscaLargura(TabelasIniciais[1]["tabuleiro"])
    largura.iniciar()
else:
    print("Valor inválido")
