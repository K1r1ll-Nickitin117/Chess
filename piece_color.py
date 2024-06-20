WHITE = 1
BLACK = 2


class PieceColor:
    def __init__(self, color_now):
        self.color_now = color_now

    def opponent(self):
        if self.color_now == WHITE:
            return BLACK
        return WHITE

    def is_black(self):
        return self.color_now == BLACK

    def is_white(self):
        return self.color_now == WHITE


