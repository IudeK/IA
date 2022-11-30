import itertools


def manhattanDistance(nodeCurrent):
    length = len(nodeCurrent)
    node = list(itertools.chain(*nodeCurrent))

    total = sum(
        abs((val - 1) % length - i % length) +
        abs((val - 1) // length - i // length)
        for i, val in enumerate(node) if val
    )

    return total


"""
Em um espaço bidimensional, a distância de Manhattan entre dois pontos 
(x1, y1) e (x2, y2) seria calculada como: distância = |x2 - x1| + |y2 - y1|.
"""
