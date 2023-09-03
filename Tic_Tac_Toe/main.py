board_outline = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]
import random

list_of_choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def display_board(emp_board):
    print(f"{emp_board[0]} | {emp_board[1]} | {emp_board[2]}")
    print("---------")
    print(f"{emp_board[3]} | {emp_board[4]} | {emp_board[5]}")
    print("---------")
    print(f"{emp_board[6]} | {emp_board[7]} | {emp_board[8]}")


display_board(board_outline)


def user_input():
    x_input = int(input("Enter the position of your 'X' between 0,9 : "))
    if x_input not in list_of_choices:
        print("Stupid_its_already_filled")
    else:
        return x_input


def computer_input():
    comp_choice = random.choice(list_of_choices)
    return comp_choice


game_on = True
while game_on:
    user_choice = user_input()
    board_outline[user_choice] = "X"
    list_of_choices.remove(user_choice)
    print(list_of_choices)
    display_board(board_outline)
    comp = computer_input()
    board_outline[comp] = "O"
    list_of_choices.remove(comp)
    print(list_of_choices)
    display_board(board_outline)
    if (board_outline[0] =="X" and board_outline[1] == "X" and board_outline[2] == "X") or (board_outline[3] =="X" and board_outline[4] == "X" and board_outline[5] == "X") or (board_outline[6] =="X" and board_outline[7] == "X" and board_outline[8] == "X") or (board_outline[0] =="X" and board_outline[3] == "X" and board_outline[6] == "X") or (board_outline[1] =="X" and board_outline[4] == "X" and board_outline[7] == "X") or (board_outline[2] =="X" and board_outline[5] == "X" and board_outline[8] == "X") or (board_outline[0] =="X" and board_outline[4] == "X" and board_outline[8] == "X") or (board_outline[2] =="X" and board_outline[4] == "X" and board_outline[6] == "X") :
        print("You_Won...")
        game_on= False
        print("Game_Over")
    elif (board_outline[0] == "O" and board_outline[1] == "O" and board_outline[2] == "O") or (board_outline[3] == "O" and board_outline[4] == "O" and board_outline[5] == "O") or (board_outline[6] == "O" and board_outline[7] == "O" and board_outline[8] == "O") or (board_outline[0] == "O" and board_outline[3] == "O" and board_outline[6] == "O") or (board_outline[1] == "O" and board_outline[4] == "O" and board_outline[7] == "O") or (board_outline[2] == "O" and board_outline[5] == "O" and board_outline[8] == "O") or (board_outline[0] == "O" and board_outline[4] == "O" and board_outline[8] == "O") or (board_outline[2] == "O" and board_outline[4] == "O" and board_outline[6] == "O"):
        print("Computer_Won")
        game_on= False
        print("Game_Over")

