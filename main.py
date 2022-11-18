board = list(range(1, 10))


def paint_board():
    print('------------')
    for i in range(3):
        print('I', board[0 + i * 3], board[1 + i * 3], board[2 + i * 3], 'I')
    print('------------')

paint_board()
