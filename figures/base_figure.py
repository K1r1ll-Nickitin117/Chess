class BaseFigure:
    """Это базовый класс, для наследования его другими классами фигур."""
    def __init__(self, row: int, col: int, color: int, symbol: str):
        self.row = row
        self.col = col
        self.color = color
        self.symbol = symbol

    def get_char(self) -> str:
        return self.symbol

    def get_color(self) -> int:
        return self.color

    def set_position(self, row: int, col: int):
        self.row = row
        self.col = col
