class Board:
    def __init__(self):
        self.fig = 'bP'
        self.board = [[f' {self.fig} '] * 8] * 8

    def print_board(self):
        k = 0
        for i in self.board:
            print('  +----+----+----+----+----+----+----+----+')
            s = f'{k} |'
            k += 1
            for j in i:
                s += str(j) + '|'
            print(s)
        print('  +----+----+----+----+----+----+----+----+')
        print('     0    1    2    3    4    5    6    7  ')

    def move(self, row1, col1, row2, col2):
        pass


b = Board()
b.print_board()
