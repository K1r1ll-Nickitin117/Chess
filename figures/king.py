from base_figure import BaseFigure


class King(BaseFigure):
    def __init_(self, row: int, col: int, color: int, symbol: str):
        self.color = color
        self.row = row
        self.col = col
        self.symbol = symbol

    def can_move(self, row1: int, col1: int, row2: int, col2: int, color: int):
        """Описание логики хода фигуры"""
