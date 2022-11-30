def isOdd(value: int):
    return value % 2 == 1


# Conversão do tabuleiro para o formato de lista
def converter_b_l(tabuleiro: list) -> list:
    return [j for sub in tabuleiro for j in sub]


if __name__ == "__main__":
    tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(tabuleiro)
    print(converter_b_l(tabuleiro))
