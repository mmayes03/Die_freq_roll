from random import randint

# import pygal

class Die():
    def __init__(self, num_of_sides = 6):
        self.num_of_sides = num_of_sides
    def roll_die(self):
        return randint(1, self.num_of_sides)


die = Die()
roll_amount = []

for value in range(10):
    die_roll = die.roll_die()
    roll_amount.append(die_roll)

frequency = []

for value in range(1, die.num_of_sides + 1):
    freq = roll_amount.count(value)
    frequency.append(freq)