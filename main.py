board = list(range(1, 10))


def paint_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')

def write_input(Player_token):
    value = input('Иыберите число :'+Player_token)
    if not (value in '123456789'):
        print('Вне диапазона. Ввведите число от 1 до 9')



paint_board()

