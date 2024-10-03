from random import randint

board = []

for x in range(3):
    board.append(["_"] * 3)

def print_board(board):
    for row in board:
        print ("  ".join(row))



def random_o(board):
    return randint(0, len(board)-1)



def row_check(board, row, col, player, tag):
    if board[row][col] == tag:
        if board[row][col+1] == tag:
            if board[row][col+2] == tag:
                if player == "bot":
                    print ("I win!")
                    print
                    return 11
                else:
                    print ("You win!")
                    print
                    return 12


def col_check(board, row, col, player, tag):
    if board[row][col] == tag:
        if board[row+1][col] == tag:
            if board[row+2][col] == tag:
                if player == "bot":
                    print ("I win!")
                    print
                    return 21
                else:
                    print ("You win!")
                    print
                    return 22

def dia_check(board, row, col, player, tag):
    if board[row][col] == tag:
        if board[row+1][col+1] == tag:
            if board[row+2][col+2] == tag:
                if player == "bot":
                    print
                    print ("I win!")
                    print
                    return 31


                else:
                    print
                    print ("You win!")
                    print
                    return 32


bot_count = 0
pl_count = 0
i = 100
v = 100
def bot_place(board):
    bot_row = random_o(board)
    bot_col = random_o(board)
    if board[bot_row][bot_col] == "_":
        board[bot_row][bot_col] = "X"
    else:
        bot_place(board)

def pl1_stat(pl, count):
    if pl >= count:
        if row_check(board, 0, 0, "player", "O") == 12:
            return 12

        elif col_check(board, 0, 0, "player", "O") == 22:
            return 22

        elif dia_check(board, 0, 0, "player", "O") == 32:
            return 32

        elif row_check(board, 1, 0, "player", "O") == 12:
            return 12

        elif col_check(board, 0, 1, "player", "O") == 22:
            return 22

        elif row_check(board, 2, 0, "player", "O") == 12:
            return 12

        elif col_check(board, 0, 2, "player", "O") == 22:
            return 22

        else:
            pl1_stat(pl, count+1)

def pl2_stat(pl, count):
    if pl >= count:
        if row_check(board, 0, 0, "bot", "X") == 11:
            return 11

        elif col_check(board, 0, 0, "bot", "X") == 21:
            return 21

        elif dia_check(board, 0, 0, "bot", "X") == 11:
            return 11

        elif row_check(board, 1, 0, "bot", "X") == 21:
            return 21

        elif col_check(board, 0, 1, "bot", "X") == 11:
            return 11

        elif row_check(board, 2, 0, "bot", "X") == 21:
            return 21

        elif col_check(board, 0, 2, "bot", "X") == 11:
            return 11

        else:
            pl1_stat(pl, count+1)

while i > 0:



    print ("My turn:")
    bot_place(board)
    bot_count += 1
    print
    print (print_board(board))
    if pl2_stat(bot_count, 3) == 11 or pl2_stat(bot_count, 3) == 21 or pl2_stat(bot_count, 3) == 31:
        print ("bot wins!")
        break
        if bot_count >= 5:
            print ("Draw!")
            break


    print ("Your turn:")
    pl_row = int(input("Enter row:"))
    pl_row -= 1
    print
    pl_col = int(input("Enter col:"))
    pl_col -= 1
    pl_count += 1
    print

    if board[pl_row][pl_col] != "_":
        print ("You can't do that, enter again")
        pl_row -= int(input("Enter row:"))
        pl_row = 1
        print
        pl_col -= int(input("Enter col:"))
        pl_col = 1
        print
    else:
        board[pl_row][pl_col] = "O"

    print (print_board(board))
    if pl1_stat(pl_count, 2) == 12 or pl1_stat(pl_count, 3) == 22 or pl1_stat(pl_count, 3) == 32:
        print ("Player wins!")
        break
        if pl_count >= 5:
            print ("Draw!")
            break
    print (print_board(board))
