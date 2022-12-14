import os
import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

win = 1
draw = -1
running = 0
stop = 1

Game = running
mark = 'x'


def display_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")


def check_pos(x):
    if board[x] == ' ':
        return True
    else:
        return False


def check_win():
    global Game
    if board[0] == board[1] and board[1] == board[2] and board[0] != ' ':
        Game = win
    elif board[3] == board[4] and board[4] == board[5] and board[3] != ' ':
        Game = win
    elif board[6] == board[7] and board[7] == board[8] and board[6] != ' ':
        Game = win
    elif board[0] == board[3] and board[3] == board[6] and board[0] != ' ':
        Game = win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = win
    elif board[0] == board[4] and board[4] == board[8] and board[4] != ' ':
        Game = win
    elif board[2] == board[4] and board[4] == board[6] and board[4] != ' ':
        Game = win
    elif (board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' '
         and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' '):
        Game = draw
    else:
        Game = running


print("Tic Tac Toe Game")
print("Player[1] - 'X' and Player[2] - 'O'")

display_board()
time.sleep(1)
while Game == running:
    os.system('cls')
    display_board()
    if player % 2 == 0:
        print("Player 2 chance ")
        mark = 'O'
    else:
        print("Player 1 chance ")
        mark = 'X'

    choice = int(input("Enter a position between [1-9]  where it is empty : "))

    if check_pos(choice-1):
        board[choice-1] = mark
        player += 1
        display_board()
        check_win()

os.system('cls')
display_board()
if Game == draw:
    print("Game Drawn")
elif Game == win:
    player -= 1
    if player % 2 == 0:
        print(f"Game is won by Player 1")
    else:
        print(f"Game is won by Player 2")
