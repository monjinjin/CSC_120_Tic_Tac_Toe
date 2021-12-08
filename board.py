def print_board(brd):
    for i in brd:
        print(i)
    print("Board printed")


def check_mark(brd, row, col):
    if row < 0 or row > 2:
        return False
    elif col < 0 or col > 2:
        return False
    else:
        for i in brd:
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


def run(brd, player):
    row = int(input("Player " + str(player) + ", Please input a row: "))
    col = int(input("Player " + str(player) + ", Please input a column: "))
    place_mark(brd, row, col, player)
    print_board(brd)
    if player == 1:
        player = player + 1
    elif player == 2:
        player = player - 1
    run(brd, player)


board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
print_board(board)
run(board, 1)
