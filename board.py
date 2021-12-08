def print_board(brd):
    for i in brd:
        print(i)


def check_mark(brd, row, col):
    if row < 0 or row > 2:
        return False
    elif col < 0 or col > 2:
        return False
    else:
        if brd[row][col] != "-":
            return False
        else:
            return True


def place_mark(brd, row, col, player_id):
    if not check_mark(brd, row, col):
        print("Mark cannot be placed here")
    else:
        if player_id == 1:
            brd[row][col] = "X"
        elif player_id == 2:
            brd[row][col] = "O"


def check_win(brd):
    fully_filled = True
    for i in range(0, 3):
        for j in range(0, 3):
            if brd[i][j] == "-":
                fully_filled = False
    who_won = 0
    for i in range(0, 3):
        if brd[i][0] == brd[i][1] == brd[i][2] == "X":
            who_won = 1
        elif brd[i][0] == brd[i][1] == brd[i][2] == "O":
            who_won = 2
        else:
            for j in range(0, 3):
                if brd[0][j] == brd[1][j] == brd[2][j] == "X":
                    who_won = 1
                elif brd[0][j] == brd[1][j] == brd[2][j] == "O":
                    who_won = 2
                else:
                    if brd[0][0] == brd[1][1] == brd[2][2] == "X":
                        who_won = 1
                    elif brd[0][0] == brd[1][1] == brd[2][2] == "O":
                        who_won = 2
                    else:
                        if brd[0][2] == brd[1][1] == brd[2][0] == "X":
                            who_won = 1
                        elif brd[0][2] == brd[1][1] == brd[2][0] == "O":
                            who_won = 2
                        else:
                            if fully_filled:
                                who_won = 3
    return who_won


def run(brd, player):
    row = int(input("Player " + str(player) + ", Please input a row: "))
    col = int(input("Player " + str(player) + ", Please input a column: "))
    place_mark(brd, row, col, player)
    print_board(brd)

    if player == 1:
        player = player + 1
    elif player == 2:
        player = player - 1

    if check_win(brd) == 1:
        print("Player 1 wins!")
    elif check_win(brd) == 2:
        print("Player 2 wins!")
    elif check_win(brd) == 3:
        print("Draw")
    else:
        run(brd, player)


board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
print_board(board)
run(board, 1)
