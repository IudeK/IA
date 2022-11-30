import copy
from entidades.Posicao import Posicao
from entidades.utils.enums import Direction
from entidades.utils.constante import BLANK_SYMBOL


class FuncoesTabuleiro:
    @staticmethod
    def pegar_posicao_vazia(node: list) -> Posicao:
        for i in range(0, len(node)):
            for j in range(0, len(node[i])):
                if node[i][j] == BLANK_SYMBOL:
                    return Posicao(i, j)
        return Posicao(0, 0)

    @staticmethod
    def pode_mover(node: list, direction: Direction, positionBlankSymbol: Posicao) -> bool:
        """Verifica se a peça em branco pode ser movida na direção indicada."""
        
        if direction == Direction.CIMA:
            return positionBlankSymbol.line > 0
        elif direction == Direction.DIREITA:
            return positionBlankSymbol.column < (len(node) - 1)
        elif direction == Direction.BAIXO:
            return positionBlankSymbol.line < (len(node) - 1)
        else:
            return positionBlankSymbol.column > 0

    @staticmethod
    def mover(node: list, direction: Direction, positionBlankSymbol: Posicao):
        """Move peça em branco na direção indicada."""

        line = positionBlankSymbol.line
        column = positionBlankSymbol.column
        nodeMoved = copy.deepcopy(node)

        if direction == Direction.CIMA:
            line -= 1
        elif direction == Direction.DIREITA:
            column += 1
        elif direction == Direction.BAIXO:
            line += 1
        else:
            column -= 1

        FuncoesTabuleiro.trocar(nodeMoved, line, column, positionBlankSymbol)
        return nodeMoved

    @staticmethod
    def trocar(node: list, lineValue: int, columnValue: int, positionBlankSymbol: Posicao):
        """Troca uma peça de lugar com a peça em branco."""

        node[positionBlankSymbol.line][positionBlankSymbol.column] = node[lineValue][columnValue]
        node[lineValue][columnValue] = BLANK_SYMBOL

    @staticmethod
    def tentar_mover(node: list, direction: Direction):
        positionBlankSymbol = FuncoesTabuleiro.pegar_posicao_vazia(node)

        if FuncoesTabuleiro.pode_mover(node, direction, positionBlankSymbol):
            return FuncoesTabuleiro.mover(node, direction, positionBlankSymbol)
        return None
