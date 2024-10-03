from random import randint
import time
start = time.time()
board = []

for x in range(7):
    board.append(["_"] * 10)

def print_board(board):
    for row in board:
        print ("   ".join(row))

def random_o():
    return randint(1, 6)

def random_l():
    return randint(1, 9)

def bot_place(board, tag):
    bot_row = random_o()
    bot_col = random_l()
    if board[bot_row][bot_col] == "_":
        board[bot_row][bot_col] = tag
    else:
        bot_place(board, tag)

board[0][0] = "TTG"
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

for i in range(7):
    board[i][3] = "brk"
    board[i][6] = "brk"

k = 0
for j in range(1, 7):
    board[j][0] = days[k]
    k += 1

m = 1
l = 1
while l < 10:

    if board[0][l] == "_":
        board[0][l] = str(m) + "Hr"
        m += 1
    else:
        l += 1

board[6][7] = "N/A"
board[6][8] = "N/A"
board[6][9] = "N/A"

def ranno():
    return randint(0, 2)

def lab_place1(board, sub):
    lab_row = random_o()
    list1 = [1, 4, 7]
    rw = list1[ranno()]
    if board[lab_row][rw] == "_":
        board[lab_row][rw] = sub
        board[lab_row][rw+1] = sub
    if board[lab_row][rw+2] == "_":
        board[lab_row][rw+2] = sub
    elif board[lab_row][rw+2] == "brk":
        board[lab_row][rw+2] = sub
        board[lab_row][rw+3] = "brk"
    else:
        print("\n")

def lab_place2(board, sub):
    lab_row = random_o()
    list1 = [1, 4, 7]
    rw = list1[ranno()]
    if board[lab_row][rw] == "_":
        board[lab_row][rw] = sub
        board[lab_row][rw+1] = sub
    if board[lab_row][rw+2] == "_":
        board[lab_row][rw+2] = sub
    elif board[lab_row][rw+2] == "brk":
        board[lab_row][rw+2] = sub
        board[lab_row][rw+3] = "brk"
    else:
        print("\n")

def tut_place(board):
    for i in range(1, 7):
        for j in range(1, 10):
            if board[i][j] == "_":
                board[i][j] = "TUT"

lab_row = random_o()
for i in range(1):
    lab_place1(board, "MPL")

for i in range(1):
    lab_place2(board, "ADL")

sub_list = ["MAT", "SE ", "DAA", "MP ", "OOC", "DC "]
for i in range(4):
    for j in range(0, 6):
        bot_place(board, sub_list[j])

tut_place(board)
print("\n")
print (print_board(board))
print("\n")

print("Time elapsed = " + str(time.time() - start) + " ms")
