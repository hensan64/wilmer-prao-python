# INSTRUCTION:
#
# Create a Rock/Scissors/Paper game, where you play against the computer
#    1. Print the options: 1=Rock, 2=Scissors, 3=Paper
#    2. Read a digit (1, 2, 3) from the CONSOLE (representing Rock/Scissors/Paper)
#    3. Check that no other digit than (1, 2, 3) is being entered.
#       If a faulty value was added, print an error message and read a digit once again
#    4. Calculate the computer choice (1, 2, 3) by using RANDOM function, and print it
#    5. Calculate who won the round ('if' or 'case' clause)
#    6. Print a WIN/LOOSE statement
#
# TIP: Do one point at a time and test that it works before moving on to the next point


#  Import Statement - Random;Randint
from random import randint

#  Strings Assigned to Constants
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

#  Draw While Loop
RPS_draw = True
while RPS_draw:  # Draw Loop
    RPS_AI = randint(1, 3)

    # Error While Loop
    while True:
        player_input = str(input("Rock, Paper, Scissors: ").lower())
        if player_input == ROCK or player_input == PAPER or player_input == SCISSORS:
            break
        print("\nInvalid input. Please retry.")

    #  1 = Rock
    if RPS_AI == 1:
        if player_input == ROCK:
            print("\nDraw.\n- Your opponent picked Rock.\n\nTry again.")
        elif player_input == PAPER:
            print("\nYou won.\n- Your opponent picked Rock.\n")
            RPS_draw = False
        elif player_input == SCISSORS:
            print("\nYou lost.\n- Your opponent picked Rock.\n")
            RPS_draw = False

    #  2 = Paper
    if RPS_AI == 2:
        if player_input == ROCK:
            print("\nYou lost.\n- Your opponent picked Paper.\n")
            RPS_draw = False
        elif player_input == PAPER:
            print("\nDraw.\n- Your opponent picked Paper.\n\nTry again.")
        elif player_input == SCISSORS:
            print("\nYou won.\n- Your opponent picked Paper.\n")
            RPS_draw = False

    #  3 = Scissors
    if RPS_AI == 3:
        if player_input == ROCK:
            print("\nYou won.\n- Your opponent picked Scissors.\n")
            RPS_draw = False
        elif player_input == PAPER:
            print("\nYou lost.\n- Your opponent picked Scissors.\n")
            RPS_draw = False
        elif player_input == SCISSORS:
            print("\nDraw.\n- Your opponent picked Scissors.\n\nTry again.")

# Presentation Preparation

#  1) Variables/Constants, Randint Function, Input/Guess Function and Error Function
#     - Randomly picked integer from Randint Module, imported from Random Module.
#     - Variable assigned to Randint Module.
#     - Player Inputs Rock, Paper or Scissors as Guess. "Lower" String Method Used to Ignore Capital Letters.
#     - If Player Input is not Rock, Paper or Scissors, Display Error String Under Error Conditions and While Loop.

#  2) If/Elif Statements, Constant Strings into If/Elif Statements. Randint Function.
#     - Randomly Picked Number Through Randint Function. If Statement for Randint Number Determines AI Pick.
#     - Constants Assigned as Strings into If/Elif Statements Determines if Player Input is True.
#     - If Player Input Follows If-Conditions of AI Pick and Constants, Display Pre-set Message for Loss, Win or Draw.

#  3) While Loop, True Statements, Retry Function for Draw/Error
#     - Entire Script Set Inside While Loop. While Loop Set to a Variable as True. Constantly Loops Code.
#     - Under If/Elif Statements Set as Win or Lose, Set While Loop Variable to False, Ending Loop.
#     - Under Randint If-Condition, If Player Input is Same as Constant, While Loop Continues for Retry.
#     - Error String Function Run Through While Loop. If Player Input is not Error, Break Error While Loop. If Error, Run Retry Function in Loop.
