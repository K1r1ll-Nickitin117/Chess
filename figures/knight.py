from base_figure import BaseFigure


class Knight(BaseFigure):
    def __init_(self, row: int, col: int, color: int, symbol: str):
        self.color = color
        self.row = row
        self.col = col
        self.symbol = symbol

    def can_move(self, row1, col1, row2, col2, color):
        """Описание логики хода фигуры"""
