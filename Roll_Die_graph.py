import pygal

from create_die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()
results = []

for roll_num in range(1000):
    result = die_1.roll_die() + die_2.roll_die() 
    results.append(result)

frequencies = []


max_result = die_1.num_of_sides + die_2.num_of_sides 
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Results of rolling two 6 sided Dice 1000 times!"
hist.x_title = "Total of Die 1 plus Die 2"
hist.y_title = "Frequency of Die total"
hist.x_labels = []

for value in range(min(results), max(results)+1):
    new_value = str(value)
    hist.x_labels.append(new_value)


hist.add("D6 + D6", frequencies)
hist.render_to_file('dice_visual.svg')