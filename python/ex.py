letters = ['a', 'b', 'c']
nums = [1, 2, 3]
for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
print(list(letters))
print(list(nums))

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i + 1, letter)

squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)

values = [x**2 if x % 2 == 0 else x + 10 for x in range(9) ]
print(values)

names = ["Vasco Manuel", "Michael Jordan", "Lionel Messi", "Tiger Woods", "Roger Federer"]
first_names = [name.split(' ')[0].lower() for name in names]
print(first_names)

multiples_3 = [3*x for x in range(1, 21)]
print(multiples_3)

scores = {
    "Michael Jordan": 70,
    "Tiger Woods": 35,
    "Vasco Manuel": 82,
    "Lionel Messi": 23,
    "Roger Federer": 98
}
passed = [name for name, value in scores.items() if value >= 65] # write your list comprehension here
print(passed)

egg_count = 0
def buy_eggs(count):
    return count + 12 # purchase a dozen eggs

print(buy_eggs(egg_count))

numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]
averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

cities = ["New York City", "Vienna", "Zurich", "Paris", "Porto", "Barcelona"]
short_cities = list(filter(lambda x: len(x) > 5, cities))
print(short_cities)

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
def my_enumerate(iterable, start=0):
    for element in iterable:
        yield start, element
        start += 1
for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

sq_list = [x**2 for x in range(10)]  # this produces a list of squares
print(sq_list)
sq_iterator = (x**(1/2) for x in range(5,10))  # this produces an iterator of square roots
for n in sq_iterator:
    print(n)

def party_planner(cookies, people):
    leftovers = None
    num_each = None
    try:
        leftovers = cookies % people
        num_each = cookies // people
    except ZeroDivisionError as e:
        print("We need people to eat... plz")
        print("ZeroDivisionError occurred: {}".format(e))
    return (leftovers, num_each)

leftovers, num_each = party_planner(10, 0)
if leftovers is None:
    print("Nothing to show.")
else: 
    print(leftovers, num_each)

f = open('my_file.txt', 'w')
f.write("Hello!!\n\nYou've read the contents of this file!")
f.close()

with open('my_file.txt', 'r') as f: # closes file 
    file_data = f.read()
print(file_data)

def create_cast_list(filename):
    with open(filename, 'r') as f:
        return [line.split(',')[0] for line in f]

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
print(cast_list)

from math import e
print(e**3)

import random
word_file = "words.txt"
word_list = []

with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word) 

def generate_password():
    return ''.join(random.sample(word_list, 3))

# test your function
print(generate_password())

# FSM Interpretation

# Provide s1 and s2 that are both accepted, but s1 != s2.

s1 = "bdf"
s2 = "bdgbdf"

edges = {(1,'a') : 2,
         (1,'b') : 3,
         (2,'c') : 4,
         (3,'d') : 5,
         (5,'c') : 2,
         (5,'f') : 6,
         (5,'g') : 1}

accepting = [6]

def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        if (current, letter) in edges:
            destination = edges[(current, letter)]
            remaining_string = string[1:]
            return fsmsim(remaining_string, destination, edges, accepting)
        else:
            return False


print(fsmsim(s1,1,edges,accepting))
# >>> True

print(fsmsim(s2,1,edges,accepting))
# >>> True

print(s1 != s2)
# >>> True
