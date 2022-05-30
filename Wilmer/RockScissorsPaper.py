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
RPS_AI = randint(1, 3)

while True:
    RPS_input = str(input("Rock, Paper or Scissors: ").lower())
    if RPS_input == "rock" or RPS_input == "paper" or RPS_input == "scissors":
        break
    print("\nInvalid input. Please retry.")

# 1 = Rock
# 2 = Paper
# 3 = Scissors

if RPS_AI == 1:
    if RPS_input == "rock":
        print("\nDraw.\nYour opponent picked Rock.")
    elif RPS_input == "paper":
        print("\nYou won.\nYour opponent picked Rock.")
    elif RPS_input == "scissors":
        print("\nYou lost.\nYour opponent picked Rock.")

if RPS_AI == 2:
    if RPS_input == "rock":
        print("\nYou lost.\nYour opponent picked Paper.")
    elif RPS_input == "paper":
        print("\nDraw.\nYour opponent picked Paper.")
    elif RPS_input == "scissors":
        print("\nYou won.\nYour opponent picked Paper.")

if RPS_AI == 3:
    if RPS_input == "rock":
        print("\nYou won.\nYour opponent picked Scissors.")
    elif RPS_input == "paper":
        print("\nYou lost.\nYour opponent picked Scissors.")
    elif RPS_input == "scissors":
        print("\nDraw.\nYour opponent picked Scissors.")
