from base_figure import BaseFigure


class Bishop(BaseFigure):
    def __init_(self, row, col, color, symbol):
        self.color = color
        self.row = row
        self.col = col
        self.symbol = symbol

    def can_move(self):
        """Описание логики хода фигуры"""