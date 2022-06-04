#  Object Oriented Programming .py3
class NewClass:  # This is the Header of a Class. Use the 'class' command to make a class, then assign a name to it.
    pass         # This is the Body of a Class. This command proclaims a class as empty. Indication that something will be written here later.


class BasicAttack:  # This class is assigned with the name BasicAttack. Note that it is written in Pascal Case. First letter of each word is capitalised.

    def __init__(self, damage):  # __init__() is used to define an objects state. Self is always used as the first parameter. Self refers to instance/--object--.
        self.damage = damage     # The 'damage' parameter in first row is only the same as the second 'damage' parameter in the second row.


class BasicAbility:

    def __init__(self, mana_cost, cooldown):  # Here we have multiple --items-- displayed inside the "list". 'Self' is always first.
        self.damage = []                      # The word 'damage' displayed here isn't part of the list of objects. Therefore, it is blanked out.
        self.mana_cost = mana_cost            # The second 'mana_cost' is the parameter from the list of objects, NOT the first.
        self.cooldown = cooldown              # ^ These three are instance attributes. --


class UltimateAbility:
    def __init__(self):                # Here we assign the class no objects other than 'self'.
        self.items = []


ultimate_variable = UltimateAbility()  # Here we assign the class to a variable.
print(ultimate_variable)               # Here we print the variable. The data type for the object is then displayed, and which class it refers to. --?-- 27.


class Circle:

    def __init__(self, radius):  # Here we write a class with an object, as usual.
        self.radius = radius


circle_variable = Circle(4)      # Here we have the argument '4' for the parameter 'radius'. The object 'radius' is now given a value of 4.
print(circle_variable)           # Here the variable is printed.


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


rectangle_variable = Rectangle(4, 6)  # Here we have two arguments: '4' and '6'. These arguments are values given to the corresponding parameter.
print(rectangle_variable)


class Dog:

    def __init__(self, name, age, kilograms, is_male):
        self.name = name
        self.age = age
        self.kilograms = kilograms
        self.is_male = is_male


dog_variable = Dog("Yogi", 4, 16, True)
print(dog_variable)
print()


# Own Project, Killing Enemy
from random import randint

repeat_damage = True
while repeat_damage:
    damage_boost = randint(1, 5)


    class AbilityQ:                      # <<<< Make New for OOP Course Exercise <<<<

        def __init__(self, damage=25):
            self.damage = damage


    total_damage = (25 * damage_boost)
    enemy_health = 100 - total_damage

    if damage_boost == 2:
        print("Q Ability:\nDealt {} physical damage to enemy. (25 = 25 + 0%)".format(total_damage))
        print(str("\nRemaining Enemy Health: {}/100\n\n").format(enemy_health))
    elif damage_boost == 2:
        print("Q Ability:\nDealt {} physical damage to enemy. (50 = 25 + 100%)".format(total_damage))
        print(str("\nRemaining Enemy Health: {}/100\n\n").format(enemy_health))
    elif damage_boost == 3:
        print("Q Ability:\nDealt {} physical damage to enemy. (75 = 25 + 200%)".format(total_damage))
        print(str("\nRemaining Enemy Health: {}/100\n\n").format(enemy_health))
    elif damage_boost == 4:
        print("Q Ability:\nDealt {} physical damage to enemy. (100 = 25 + 300%)".format(total_damage))
        print(str("\nRemaining Enemy Health: {}/100\n\n").format(enemy_health))
        print("You killed the enemy.")
        repeat_damage = False
    elif damage_boost == 5:
        print("Q Ability:\nDealt {} physical damage to enemy. (125 = 25 + 400%)".format(total_damage))
        if enemy_health < 0:
            enemy_health = 0
            print(str("\nRemaining Enemy Health: {}/100").format(enemy_health))
            print("You killed the enemy.\n\n")
        repeat_damage = False

# Fix Problem with Repeat: Remember Health from Previous Hit


