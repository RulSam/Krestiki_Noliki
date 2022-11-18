board = list(range(1, 10))


def paint_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def write_input(Player_token):
    while True:
        value = input('Выберите число :' + Player_token)
        if not (value in '123456789'):
            print('Вне диапазона. Ввведите число от 1 до 9')
            continue
        value = int(value)
        if str(board[value -1] in 'XO'):
            print('Ячейка занята')
            continue
        board[value -1] = Player_token
        break



paint_board()
