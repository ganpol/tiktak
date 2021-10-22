board = list(range(1, 10))
win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def d_board():
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def check_win(board):
    for each in win:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def input_play(player_turn):
    while True:
        turn = input("Куда поставить: " + player_turn + " ? ")
        turn = int(turn)
        if not (1 <= turn <= 9):
            print("Значение за пределами доски")
            continue
        if str(board[turn - 1]) in "XO":
            print("Эта клетка занята")
            continue
        board[turn - 1] = player_turn
        break


def main():
    counter = 0
    while True:
        d_board()
        if counter % 2 == 0:
            input_play("X")
        else:
            input_play("O")
        if counter > 3:
            winner = check_win(board)
            if winner:
                d_board()
                print(winner, "Выиграл!")
                break
        counter += 1
        if counter == 9:
            d_board()
            print(winner, "Ничья")
            break


main()
