from flask import Flask, render_template, request, redirect, flash, url_for
app = Flask(__name__)

@app.route('/first.html')
def profile():
    return render_template("first.html")
''' use this for css
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='filename.css') }}">'''
@app.route('/admin1.html')
def login():
    return render_template("admin1.html")

@app.route('/admin2.html')
def page1():
    return render_template("admin2.html")

@app.route('/admin3.html')
def page2():
    return render_template("admin3.html")

@app.route('/hod1.html')
def page3():
    return render_template("hod1.html")

@app.route('/hod2.html')
def page4():
    return render_template("hod2.html")

@app.route('/hod3.html')
def page5():
    return render_template("hod3.html")

@app.route('/student1.html')
def page6():
    return render_template("student1.html")

@app.route('/zxc.html')
def start():
    from random import randint
    import time

    start = time.time()
    board = []

    for x in range(6):
        board.append(["_"] * 10)

    def print_board(board):
        for row in board:
            print ("   ".join(row))

    def random_o():
        return randint(0, 5)

    def random_x():
        return randint(0, 7)

    def random_l():
        return randint(0, 9)

    def bot_place(board, tag):
        bot_row = random_o()
    #    bot_col = random_l()
        bot_col = random_x()
        if board[bot_row][bot_col] == "_":
            board[bot_row][bot_col] = tag
        else:
            bot_place(board, tag)


    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    for i in range(0, 6):
        board[i][3] = "BRK"
        board[i][6] = "BRK"

    k = 0
    for j in range(0, 6):
        board[j][0] = days[k]
        k += 1

    m = 1
    l = 1

    board[5][7] = "N/A"
    board[5][8] = "N/A"
    board[5][9] = "N/A"

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
        elif board[lab_row][rw+2] == "BRK":
            board[lab_row][rw+2] = sub
            board[lab_row][rw+3] = "BRK"
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
        elif board[lab_row][rw+2] == "BRK":
            board[lab_row][rw+2] = sub
            board[lab_row][rw+3] = "BRK"
        else:
            print("\n")

    def tut_place(board):
        for i in range(0, 6):
            for j in range(7, 10):
                if board[i][j] == "_":
                    board[i][j] = "TUT"

    def sub_fill(board):
        for i in range(0, 6):
            for j in range(0, 10):
                if board[i][j] == "_":
                    board[i][j] = sub_list[randint(0, 5)]

    lab_row = random_o()
    for i in range(1, 2):
        lab_place1(board, "MPL")

    for i in range(1, 2):
        lab_place2(board, "ADL")

    sub_list = ["MAT", "SE ", "DAA", "MP ", "OOC", "DC "]
    for i in range(4):
        for j in range(0, 6):
            bot_place(board, sub_list[j])

    tut_place(board)
    sub_fill(board)
    print("\n")
    print (print_board(board))
    print("\n")

    print("Time elapsed = " + str(time.time() - start) + " ms")

    return render_template("zxc.html", board=board)


if __name__ == "__main__":
    app.run()
	
