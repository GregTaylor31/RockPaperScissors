# noob way

#import random
#
# computer_answer = random.randint(0, 2)
#
# possible_answers = ['Rock', 'Paper', 'Scissors']
# print(possible_answers[computer_answer])
#
# player_answer = input('Please choose Rock, Paper or Scissors: ')
# Player_win = ''
#
# if player_answer == 'Rock':
#     if  possible_answers[computer_answer] == 'Rock':
#         Player_win = 'Draw'
#     elif  possible_answers[computer_answer] == 'Paper':
#         Player_win = 'Lose'
#     else: #computer_answer == 'Scissors':
#         Player_win = 'Win'
#
# if player_answer == 'Paper':
#     if  possible_answers[computer_answer] == 'Paper':
#         Player_win = 'Draw'
#     elif  possible_answers[computer_answer] == 'Scissors':
#         Player_win = 'Lose'
#     else: #computer_answer == 'Scissors':
#         Player_win = 'Win'
#
# if player_answer == 'Scissors':
#     if  possible_answers[computer_answer] == 'Scissors':
#         Player_win = 'Draw'
#     elif  possible_answers[computer_answer] == 'Rock':
#         Player_win = 'Lose'
#     else: #computer_answer == 'Scissors':
#         Player_win = 'Win'
#
#
#
#
# print(Player_win)
# print('You picked:', player_answer)
# print('Computer picked: ', possible_answers[computer_answer])
#



### better way ###


import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_selection():
    user_input = input("Enter a choice (rock[0], paper[1], scissors[2]): ")
    selection = int(user_input)
    action = Action(selection)
    print(action)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

##end

