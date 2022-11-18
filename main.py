board = list(range(1, 10))

win_points = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def paint_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def write_input(Player_token):
    while True:
        value = input('Выберите число: ' + Player_token)
        if not (value in '1,2,3,4,5,6,7,8,9'):
            print('Вне диапазона. Ввведите число от 1 до 9.')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Ячейка занята')
            continue
        board[value - 1] = Player_token
        break


def win_check():
    for ech in win_points:
        if (board[ech[0] - 1]) == (board[ech[1] - 1]) == (board[ech[2] - 1]):
            return board[ech[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        paint_board()
        if counter % 2 == 0:
            write_input('X')
        else:
            write_input('O')
        if counter > 3:
            winner = win_points
            if winner:
                paint_board()
                print("Вы выиграли")
                break
        counter += 1
        if counter > 8:
            paint_board()
            print('Ничья!')
            break


main()
