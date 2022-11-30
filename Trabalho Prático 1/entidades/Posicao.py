class Posicao:
    def __init__(self, line: int, column: int):
        self._line = line
        self._column = column

    @property
    def line(self) -> int:
        return self._line

    @property
    def column(self) -> int:
        return self._column

    @line.setter
    def line(self, line: int):
        self._line = line

    @column.setter
    def column(self, column: int):
        self._column = column

    def set_position(self, line: int, column: int):
        self._line = line
        self._column = column

    def __str__(self) -> str:
        return f"line: {self.line}, column: {self.column}"
