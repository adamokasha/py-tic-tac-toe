import sys


def display_board(board):
    line_board = ""
    for line1_item in range(7, 10):
        if line1_item == 9:
            line_board += "|" + board[line1_item] + "|"
        else:
            line_board += "|" + board[line1_item]
    line_board += "\n"
    for line2_item in range(4, 7):
        if line2_item == 6:
            line_board += "|" + board[line2_item] + "|"
        else:
            line_board += "|" + board[line2_item]
    line_board += "\n"
    for line3_item in range(1, 4):
        if line3_item == 3:
            line_board += "|" + board[line3_item] + "|"
        else:
            line_board += "|" + board[line3_item]
    print(line_board)


# display_board(['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'])

board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
plays = []
play_count = 0
current_player = 1


def new_game():
    global current_player, play_count
    while True:
        if end_game() == True:
            return replay()
        play = player_turn()
        if play != False:
            if current_player == 1:
                board[play] = "X"
            else:
                board[play] = "O"
            play_count += 1
            plays.append(play)
        else:
            continue
        if current_player == 1:
            current_player += 1
        else:
            current_player -= 1
        print("\n"*100)
        display_board(board)


def player_turn():
    global play_count

    print("Player {} , choose a position from 1 - 9".format(current_player))
    valid_input = "123456789"
    play = input()
    if play not in valid_input:
        print("\n"*100)
        print("**Not a valid play. Try again.**")
        display_board(board)
        return False

    play = int(play)
    if play > 0 and play <= 9:
        return play
    else:
        print("\n"*100)
        print("**Not a valid play. Try again.**")
        display_board(board)
        return False


def end_game():
    if board[1] == board[2] == board[3] == "X":
        print("Player 1 Won!")
        return True
    elif board[1] == board[2] == board[3] == "O":
        print("Player 2 Won!")
        return True
    elif board[4] == board[5] == board[6] == "X":
        print("Player 1 Won!")
        return True
    elif board[4] == board[5] == board[6] == "O":
        print("Player 2 Won!")
        return True
    elif board[7] == board[8] == board[9] == "X":
        print("Player 1 Won!")
        return True
    elif board[7] == board[8] == board[9] == "O":
        print("Player 2 Won!")
        return True
    elif board[1] == board[4] == board[7] == "X":
        print("Player 1 Won!")
        return True
    elif board[1] == board[4] == board[7] == "O":
        print("Player 2 Won!")
        return True
    elif board[2] == board[5] == board[8] == "X":
        print("Player 1 Won!")
        return True
    elif board[2] == board[5] == board[8] == "O":
        print("Player 2 Won!")
        return True
    elif board[3] == board[6] == board[9] == "X":
        print("Player 1 Won!")
        return True
    elif board[3] == board[6] == board[9] == "O":
        print("Player 2 Won!")
        return True
    elif board[1] == board[5] == board[9] == "X":
        print("Player 1 Won!")
        return True
    elif board[1] == board[5] == board[9] == "O":
        print("Player 2 Won!")
        return True
    elif board[7] == board[5] == board[3] == "X":
        print("Player 1 Won!")
        return True
    elif board[7] == board[5] == board[3] == "O":
        print("Player 2 Won!")
        return True
    elif play_count == 9:
        print("\n"*100)
        print("**Draw!**")
        display_board(board)
        return replay()
    else:
        return False


def replay():
    global board, plays, current_player, play_count
    print("Play again? Y/N")
    response = input()
    if response.lower() == "y":
        board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        plays = []
        current_player = 1
        play_count = 0
        print("\n"*100)
        new_game()
    elif response.lower() == "n":
        sys.exit("Thanks for playing!")
    else:
        replay()


new_game()
