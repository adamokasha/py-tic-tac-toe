import sys


board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
plays = []
play_count = 0
current_player = 1
player1_score = 0
player2_score = 0


def display_board(board):
    print("\n"*100)
    line_board = ""
    line_board += "Player1 Score: {} \nPlayer2 Score: {} \n\n".format(
        player1_score, player2_score)
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
    print(line_board+"\n")


def new_game():
    global current_player, play_count
    print("\n"*100)
    display_board(board)
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
        display_board(board)


def player_turn():
    global play_count

    print("Player {} , choose a position from 1 - 9".format(current_player))
    valid_input = "123456789"
    play = input()
    if play not in valid_input:
        display_board(board)
        print("**Not a valid play. Try again.**")
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
    global player1_score, player2_score
    if board[1] == board[2] == board[3] == "X":
        player1_score += 1
        display_board(board)
        print("Player 1 Won!")
        return True
    elif board[1] == board[2] == board[3] == "O":
        player2_score += 1
        display_board(board)
        print("Player 2 Won!")
        return True
    elif board[4] == board[5] == board[6] == "X":
        player1_score += 1
        display_board(board)
        print("Player 1 Won!")
        return True
    elif board[4] == board[5] == board[6] == "O":
        player2_score += 1
        display_board(board)
        print("Player 2 Won!")
        return True
    elif board[7] == board[8] == board[9] == "X":
        player1_score += 1
        display_board(board)
        print("Player 1 Won!")
        return True
    elif board[7] == board[8] == board[9] == "O":
        player2_score += 1
        display_board(board)
        print("Player 2 Won!")
        return True
    elif board[1] == board[4] == board[7] == "X":
        player1_score += 1
        display_board(board)
        print("Player 1 Won!")
        return True
    elif board[1] == board[4] == board[7] == "O":
        player2_score += 1
        display_board(board)
        print("Player 2 Won!")
        return True
    elif board[2] == board[5] == board[8] == "X":
        player1_score += 1
        display_board(board)
        print("Player 1 Won!")
        return True
    elif board[2] == board[5] == board[8] == "O":
        player2_score += 1
        display_board(board)
        print("Player 2 Won!")
        return True
    elif board[3] == board[6] == board[9] == "X":
        player1_score += 1
        display_board(board)
        print("Player 1 Won!")
        return True
    elif board[3] == board[6] == board[9] == "O":
        player2_score += 1
        display_board(board)
        print("Player 2 Won!")
        return True
    elif board[1] == board[5] == board[9] == "X":
        player1_score += 1
        display_board(board)
        print("Player 1 Won!")
        return True
    elif board[1] == board[5] == board[9] == "O":
        player2_score += 1
        display_board(board)
        print("Player 2 Won!")
        return True
    elif board[7] == board[5] == board[3] == "X":
        player1_score += 1
        display_board(board)
        print("Player 1 Won!")
        return True
    elif board[7] == board[5] == board[3] == "O":
        player2_score += 1
        display_board(board)
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
        print("\n"*100)
        sys.exit("Thanks for playing!\n\n** Final Score **\nPlayer1: {}\nPlayer2: {}\n".format(
            player1_score, player2_score))
    else:
        replay()


new_game()
