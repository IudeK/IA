# Verificações de teste do trabalho
TabelasIniciais = [
    {
        "isSolvable": True,  # Entrada possui solução
        "tabuleiro": [
            [1, 2, 3, 4],
            [5, 6, 8, 12],
            [13, 9, 0, 7],
            [14, 11, 10, 15]
        ],
    }, {
        "isSolvable": False,  # Entrada não possui solução
        "tabuleiro": [
            [1, 2, 3, 4],
            [13, 6, 8, 12],
            [5, 9, 0, 7],
            [14, 11, 10, 15]
        ],
    },
]

if __name__ == "__main__":
    print(TabelasIniciais[0]["tabuleiro"])
