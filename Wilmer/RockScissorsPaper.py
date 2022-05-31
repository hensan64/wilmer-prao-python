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
# TIP: Do one point at the time and test that it works before moving on to the next point

from random import randint

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

RPS_draw = True
while RPS_draw:
    RPS_AI = randint(1, 3)
    while True:
        RPS_input = str(input("Rock, Paper, Scissors: ").lower())
        if RPS_input == ROCK or RPS_input == PAPER or RPS_input == SCISSORS:
            break
        print("\nInvalid input. Please retry.")

    #  1 = Rock
    if RPS_AI == 1:
        if RPS_input == ROCK:
            print("\nDraw.\n- Your opponent picked Rock.\n\nTry again.")
        elif RPS_input == PAPER:
            print("\nYou won.\n- Your opponent picked Rock.\n")
            RPS_draw = False
        elif RPS_input == SCISSORS:
            print("\nYou lost.\n- Your opponent picked Rock.\n")
            RPS_draw = False

    #  2 = Paper
    if RPS_AI == 2:
        if RPS_input == ROCK:
            print("\nYou lost.\n- Your opponent picked Paper.\n")
            RPS_draw = False
        elif RPS_input == PAPER:
            print("\nDraw.\n- Your opponent picked Paper.\n\nTry again.")
        elif RPS_input == SCISSORS:
            print("\nYou won.\n- Your opponent picked Paper.\n")
            RPS_draw = False

    #  3 = Scissors
    if RPS_AI == 3:
        if RPS_input == ROCK:
            print("\nYou won.\n- Your opponent picked Scissors.\n")
            RPS_draw = False
        elif RPS_input == PAPER:
            print("\nYou lost.\n- Your opponent picked Scissors.\n")
            RPS_draw = False
        elif RPS_input == SCISSORS:
            print("\nDraw.\n- Your opponent picked Scissors.\n\nTry again.")
