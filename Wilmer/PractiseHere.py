# exercises
integer = 2
float_num = 3.125
bool_val = False
integer = 7

addition = 10 + 5        # 15
subtraction = 7 - 4      # 3
division = 12 / 5        # 2.4
multiplication = 4 * 4   # 16

exponentiation = 5 ** 3  # 125
floordivision = 32 // 6  # 5
modulo = 20 % 6          # 2

# addition
add = 10
add += 4  # 14
# subtraction
sub = 20
sub -= 9  # 11
# multiplication
mult = 5
mult *= 7  # 35
# division
div = 40
div /= 4  # 10
# exponentiation
exp = 2
exp **= 5  # 32
# floor_division
floor = 18
floor //= 8  # 2
# modulo
mod = 16
mod %= 5  # 1

# operator precedence
# Step 1: ()
# Step 2: **
# Step 3: %, /, // and *
# Step 4: + and -

# Expression: (9 - 7) * 2 ** 3 + 10 % 6 // -1 * 2 - 1
# Step 1: 2 * 2 ** 3 + 10 % 6 // -1 * 2 - 1
# Step 2: 2 * 8 + 10 % 6 // -1 * 2 - 1
# Step 3: 16 + -8 - 1
# Step 4: 7

ex1_var = 5 ** 3
print(ex1_var)
print(True)
print(3 * 4 // 5 + 8)

print()

purchase_var = 16.68 + 6.98 + 16.78 + 15.26 + 3.00 + 4.39
print(purchase_var)
print(round(purchase_var, 2))
purchase2_var = (16.68 + 6.98 + 16.78 + 15.26 + 3.00 + 4.39) * 100 / 100
print(purchase2_var)

print()

pasta = 16.68
sauce = 6.98
garlic = 16.78
seasoning = 15.26
bread = 3.00
meatballs = 4.39
purchase3_var = (pasta + sauce + garlic + seasoning + bread + meatballs) * 100 / 100
print(purchase3_var)
print(round(pasta + sauce + garlic + seasoning + bread + meatballs, 2))

fruit1 = "banana"
print(fruit1[:3])
print(fruit1[3:6])
print(fruit1[2:])
print(fruit1[4:])

print()

string1_var = "Just do it!"
print(string1_var[10])
print(string1_var[5:7])
print(string1_var[8:11])
print("Don't " + string1_var[5:11])

print()

ex1 = True
ex2 = 7.04
ex3 = 6
print(type(ex1))
print(type(ex2))
print(type(ex3))

ex4 = str(False)
ex5 = str(5.78)
ex6 = str(10)
print(type(ex4))
print(type(ex5))
print(type(ex6))

print()

print("\"The sum " + ex5 + " is a float.\"")

ex7 = "\"Hello, I\'m Wilmer, it\'s nice to meet you.\""
print(ex7)

print()

print(str("*******\n *****\n  ***\n   *"))

print()

name2 = input("\"What is your name?\"\n")
quest = input("\"What is your quest?\"\n")
colour = input("\"What is your favourite colour?\"\n")
print("\"So ur name is " + name2 + ", your quest is " + quest + ", and your favourite colour is " + colour + "?\"\n\"Nice to meet you " + name2 + ".\"")

print()

float1 = float(input("Please enter a float or integer to double.\n"))

print()

print(float1 * 2)
print(type(float1))

print()

# function_test_1
def function_1():
    print(2 ** 3)


function_1()

print()

# function_test_2
def function_2(parameter):
    print(parameter % 5)


function_2(143)

print()

# function_test_3
def function_3():
    print("\"Congratulations!\"\n\"You got an apple!\"")


function_3()

print()

# function_test_4
def function_4(parameter_2):
    print("\"Congratulations!\"\n\"You received a " + parameter_2 + ".\"")


function_4("package")

print()

function_4("gift")

print()

#function_test_5
p1 = "\"Congratulations\"\n\""
p3 = ".\""

def function_5(p1, p2, p3):
    print(p1 + p2 + p3 )


function_5(p1, "You won a prize", p3)

print()

# function_test_6
p4 = "\"Your results are...\"\n\""
p7 = " coin(s).\""


def function_6(p4, p5, p6, p7):
    print(p4 + p5 + str(p6) + p7)


function_6(p4, "You lost ", 4, p7)

print()

# function_test_6_return
def function_6(number1=3, number2=4):
    return number1 * number2


print(function_6() ** 2)

print()

# Function & Parameter Exercose
def name_printer(user_name):
    print(user_name)


name = input("\"Please enter you name.\" ")
name_printer("\"" + name + ", nice to meet you.\"")
name_printer(name)

print()

# Programming Challenge - Volume of a Rectangular Prism
length_var = float(input("Enter a length in centimeters. "))
width_var = float(input("Enter a width in centimeters. "))
height_var = float(input("Enter a height centimeters. "))

def prism_volume_1(l, w, h):
    return l * w * h


print("The volume of the rectangular prism is " + str(prism_volume_1(length_var, width_var, height_var)) + "cm3.")

print()

# Programming Challenge - Celsuis to Fahrenheit
celsius = int(input("Enter an integer value for degrees celsius to turn into fahrenheit. "))


def fahrenheit(cel):
    return (18 * cel + 320) / 10


print("The value amount of " + str(celsius) + "°C is equivalent to " + str(fahrenheit(celsius)) + "°F.")

print()


# module/import_testing
from random import randint

fuel = randint(10, 25)        # gallons
distance = randint(200, 400)  # miles
print("\"If a car travels " + str(distance) + " miles on a full tank-\"")
print("\"-and the fuel tank can hold " + str(fuel) + " gallons of gas-\"")
print("\"-then the car travels at approximately " + str(distance // fuel) + " miles per gallon.\"")

print()

# --------
# --------
# --------

# scopes, help <<<<<
# (think fixed) ^^

# Programming Challenge - Grade Determiner
score = int(input("Please enter the student's exam score from 0 to 100.\n"))

if score == 100:
    print("This student aced the exam with all 100 questions correct, resulting in an A.")
else:
    if score >= 90:
        print("This student's exam score of " + str(score) + " results in an A.")
    else:
        if score >= 80:
            print("This student's exam score of " + str(score) + " results in a B.")
        else:
            if score >= 70:
                print("This student's exam score of " + str(score) + " results in a C.")
            else:
                if score >= 60:
                    print("This student's exam score of " + str(score) + " results in a D.")
                else:
                    if score >= 50:
                        print("This student's exam score of " + str(score) + " results in an E.")
                    else:
                        if score < 50:
                            print("This student's exam score of " + str(score) + " results in an F.")

print()

# Programming Challenge - Roman Numeral
from random import randint
one_to_ten = randint(1, 10)

if one_to_ten == 1:
    print("The Roman numeral for 1 is: I")
elif one_to_ten == 2:
    print("The Roman numeral for 2is: II")
elif one_to_ten == 3:
    print("The Roman numeral for 3 is: III")
elif one_to_ten == 4:
    print("The Roman numeral for 4 is: IV")
elif one_to_ten == 5:
    print("The Roman numeral for 5 is: V")
elif one_to_ten == 6:
    print("The Roman numeral for 6 is: VI")
elif one_to_ten == 7:
    print("The Roman numeral for 7 is: VII")
elif one_to_ten == 8:
    print("The Roman numeral for 8 is: VIII")
elif one_to_ten == 9:
    print("The Roman numeral for 9 is: IX")
else:
    print("The Roman numeral for 10 is: X")

print()

# While Loops Exercise
counter_int = 10

while counter_int > 0:
    print(str(counter_int) + " is higher than 0.")
    counter_int -= 1
if counter_int == 0:
    print("0 is equal to 0.")

print()

# Programming Challenge - Sum of Numbers From A Positive Integer
pos_int = int(input("Insert a positive integer: "))
int_init = pos_int
summed = 0

while pos_int > 0:
    summed += pos_int
    pos_int -= 1

print(int_init)
print(summed)

print()
# ?? ^^ ?? ^^ ?? (don't quite understand)
# (I think I understand now)
# ----------
# ----------

food = "PASTA BOLOGNESE"

for lunch in food:
    print(lunch)

print()

# For-Loop Practice
word = "Hello World"

for sentence in word:
    print(sentence)

print()

# Programming Challenge - Find The Number of Characters in A String
str_num = str(input("Insert any string: "))

count = 0
for char in str_num:
    count += 1

print(str_num)

print()

print(count)

print()
# don't quite understand entirely ^^^

# Range Practice
# 1 Ranges + input
one_input = int(input("Insert a number to view the range of.\nAnswer: "))
input_answer = range(one_input)

for num in input_answer:
    print(num)

print()

# 2 Ranges + input
two_inputs_1 = int(input("Insert the starting number of a range.\nAnswer: "))
two_inputs_2 = int(input("Insert the range of the starting number.\nAnswer: "))

input_answer_2 = range(two_inputs_1, two_inputs_2)
for num in input_answer_2:
    print(num)

print()

# 3 Ranges + input
three_inputs_1 = int(input("Insert the starting number of a range.\nAnswer: "))
three_inputs_2 = int(input("Insert the range of the starting number.\nAnswer: "))
three_inputs_3 = int(input("Insert the space between each shown number within range.\nAnswer: "))

input_answer_3 = range(three_inputs_1, three_inputs_2, three_inputs_3)
for num in input_answer_3:
    print(num)

print()

# Programming Challenge - Fizz Buzz
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

print()

# Programming Challenge - Factorial
def factorial(fac_num):
    returned = 1
    for item in range(fac_num, 1, -1):
        returned *= item
    return returned

print(factorial(3))
print(factorial(4))
print(factorial(5))

print()
# help on this one ^^^ ----------------------------------------------
# --- not expected to know this ^^^ factorials are above my level ---
# -------------------------------------------------------------------

# Math Equation Question (own creation)
from random import randint

math_num_1 = randint(1, 100)
math_num_2 = randint(1, 100)

math_equation_1 = math_num_1 * math_num_2
math_question = int(input("What is " + str(math_num_1) + "x" + str(math_num_2) + "?\nAnswer: "))
if math_equation_1 == math_question:
    print("Correct. The answer was " + str(math_equation_1) + ".")
else:
    print("Incorrect. The answer was " + str(math_equation_1) + ".")

print()

# Random Number Generator - Guess (own creation)
from random import randint

num_random = randint(1, 10)

num_guess = int(input("Guess a number between 1 and 10."))
if num_random == num_guess:
    print("Correct. The answer was " + str(num_random) + ".")
else:
    print("Incorrect. The answer was " + str(num_random) + ".")

print()

# String Methods 1 Exercises
mixed_case = "A Song of Ice and Fire"  # 1

print(mixed_case.isupper())            # 2
print(mixed_case.islower())            # 3
print(mixed_case.upper())              # 4
print(mixed_case.lower())              # 5
print(mixed_case.istitle())            # 6
title_case = mixed_case.title()        # 7
print(title_case)                      # 8
print(mixed_case.startswith("A"))      # 9
print(mixed_case.endswith("e"))        # 10

words = mixed_case.split()             # 11
print(words)                           # 12
print("".join(words).isalpha())        # 13

print()

# String Methods 2 Exercises
the_string = "North Dakota"                  # 1

print(the_string.rjust(17))                  # 2
print(the_string.ljust(17, "*"))             # 3
center_plus = the_string.center(16, "+")     # 4
print(center_plus)                           # 5
print(the_string.lstrip("North"))            # 6
print(center_plus.rstrip("+"))               # 7
print(center_plus.strip("+"))                # 8
print(the_string.replace("North", "South"))  # 9

print()

# stringmethod 2 selfpracticing 1
greeting_var = "Good Morning."

from random import randint
time_var_1 = randint(1, 2)
if time_var_1 == 1:
    print(greeting_var)
else:
    print(greeting_var.replace("Morning.", "Afternoon."))

print()

# Programming Challenge - String Reverser
user_stringVar = input("Please enter a string.")
reversed = "" #

for item in range(len(user_stringVar) - 1, -1, -1): #
    reversed += user_stringVar[item] #

print(reversed)

print()

# ^^^ fix ---------------------------------
# --- don't understand: reversed (( = "" ))
# -----------------------------------------

# Programming Challenge - Word Counter
word_count = "Hello. My name is Wilmer and I am 14 years old, gonna be 15 years old later this year. I am currently practicing the coding language Python and programming."

spaces_and_letters = ""

for char in word_count:
    if char.isalnum() or char.isspace() or char == "-" or char == "'":
        spaces_and_letters += char

words_var = spaces_and_letters.split()
word_num = len(words_var)

print(words_var)
print(word_num)

print()

# ^^^ don't understand
# --------------------
# --------------------

# Introduction to Lists Exercises
list_var_1 = [5, 4.55, False, "Donut", [5, 4.55, False, "Another Donut"]]  # 1
list_var_2 = list("Why am I existent?")                                    # 2

print("e" in list_var_2)                                                   # 3
print("a" not in list_var_2)                                               # 4

print()

# Indexes and List Slicing Exercises
index_var_1 = [[0, 2], [4, 6], [8, 10], [12, 14]]                                   # 1

print(index_var_1[1])                                                               # 2
print(index_var_1[3][1])                                                            # 3

index_var_2 = ["chair", "table", "desk", "lamp", "bed"]                             # 4

print(index_var_2[-5])                                                              # 5
print("Most people own at least {} {}s".format(index_var_1[0][1], index_var_2[0]))  # 6

index_var_3 = [0.98, 8.76, 6.54, 4.32]                                              # 7

print(index_var_3[1:])                                                              # 8
print(index_var_3[1:3])                                                             # 9
print(index_var_3[:2])                                                             # 10

print()

# own creation ^ from exercise above
from random import randint
random_furniture = randint(0, 9)
index_variable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Stanley has been sitting at his desk for {} hour(s).".format(index_variable[random_furniture]))

print()

# own creation - time of day
from random import randint
random_hour = randint(0, 23)
random_minute = randint(0, 59)
timeline_var = "AM"
if random_hour >= 12:
    timeline_var = "PM"

print("The time is {}:{} {}.".format(str(random_hour), str(random_minute).rjust(2, "0"), timeline_var))

print()

# Del and List Methods Exercise
arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]  # 1
del arctic_animals[4]
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(2, "snow owl")
arctic_animals.sort()

print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())

print()

# Introductions to Dictionaries Exercises
dictionary_var = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

print(dictionary_var["c"])
print("a" in dictionary_var)
print("b" not in dictionary_var)

print()

age_dict = {14: "emil", 16: "olle", 20: "daniel", 21: "fabian"}

print(age_dict.get(14, "No one is that age."))

print()

# -------------fix under-----------------
# ---------------------------------------
# own creation: hamburger-restaurant menu
# menu_dict = {1.79: "Fries", 2.19: "Coca Cola", 2.49: "Chicken Nuggets", 2.99: "Burger", 8.79: "Full menu"}
# cash_amount = float(input("Insert your current cash amount to buy with."))
# if cash_amount < 1.79:
#     print("You have insufficient money.")
# elif cash_amount >= 1.79:
#     print(menu_dict.items()[:0])
#     for key, value in menu_dict.items()[:0]:
#         print("£", key, "=", value)
# elif cash_amount >= 2.19:
#     print(menu_dict.items()[:1])
#     for key, value in menu_dict.items()[:1]:
#         print("£", key, "=", value)
# elif cash_amount >= 2.49:
#     print(menu_dict.items()[:2])
#     for key, value, in menu_dict.items()[:2]:
#         print("£", key, "=", value)
# elif cash_amount >= 2.99:
#     print(menu_dict.items()[:3])
#     for key, value in menu_dict.items()[:3]:
#         print("£", key, "=", value)
# else:
#     print(menu_dict.items())
#     for key, value in menu_dict.items():
#         print("£", key, "=", value)

# print()

# Dictionary Methods 1 Exercise
artist_song_dict = {"Queen": "Bohemian Rhapsody",                            # 1
                    "Bee Gees": "Stayin' Alive",
                    "U2": "One",
                    "Michael Jackson": "Billie Jean",
                    "The Beatles": "Hey Jude",
                    "Bob Dylan": "Like A Rolling Stone"}                     # 2

print()

print("Artists: Amount =", len(artist_song_dict))                            # 3
for key in artist_song_dict.keys():
    print("•", key)

print()

print(artist_song_dict.keys())                                               # 4
print(artist_song_dict.values())                                             # 5

print()

print("Artists & Famous Songs =", len(artist_song_dict))

for key, value in artist_song_dict.items():

    print(key.center(15), "-".center(3), value.center(15))                   # 6

print()

print(artist_song_dict.get("Promise of the Real", "That song is invalid."))  # 7

print()

# Dictionary Methods 2 Exercises
fromkeys_dict = {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant")
for key, value in fromkeys_dict.items():
    print(key, value)                                              # 1

print()

fast_food_dict = {"McDonald's": "Big Mac",
                  "Burger King": "Whopper",
                  "Chick-fil-A": "Original Chicken Sandwich"}

print(fast_food_dict.pop("McDonald's"))                            # 2

fast_food_dict.popitem()
print(fast_food_dict)

print()

# Dictionary Methods 3 Exercises
internet_celebrities = {"Dr Disrespect": "Youtube",  # 1
                        "ZLaner": "Facebook",
                        "Ninja": "Mixer"}
another_one = {"Shroud": "Twitch"}
internet_celebrities.update(another_one)             # 2
gamers = internet_celebrities.copy()                 # 3
internet_celebrities.clear()                         # 4

print(internet_celebrities)                          # 5
print(gamers)                                        # 6

print()
