class BaseFigure:
    """Это базовый класс, для наследования его другими классами фигур."""
    def __init__(self, row, col, color, symbol):
        self.row = row
        self.col = col
        self.color = color
        self.symbol = symbol

    def char(self):
        return self.symbol

    def color(self):
        return self.color()

    def set_position(self, row, col):
        self.row = row
        self.col = col
