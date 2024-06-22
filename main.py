from board import Board


def main():
    color = 'белых'
    flag = False
    board = Board()
    while True:
        # board.print_board()
        print('''Команды:
           exit                                -- выход               
           move <row> <col> <row1> <col>       -- ход из клетки (row, <col)
                                                  в клетку (row1, col1)''')

        print(f'ход {color}:')
        command, row, col, row1, col1 = map(int, input().split())
        if command == 'exit':
            break


if __name__ == '__main__':
    main()
