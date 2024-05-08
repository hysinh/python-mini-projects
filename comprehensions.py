import pprint

"""
Basic List Comprehension - loops for x in range(10)
"""
values = []
for x in range(10):
    values.append(x)
print(values)

#Using list comprehension
values2 = [x for x in range(10)]
values3 = [x + 1 for x in range(10)]
print(f"List comprehension: {values2}, \n{values3}\n\n")


"""
Get all the even numbers from 0 - 50
"""
evens = []
for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)

# List comprehension
evens2 = [number for number in range(50) if number % 2 == 0] # put If condition at the end

print(evens)
print(f"List Comprehension: {evens2}")


"""
List Comprehension with multiply conditions
"""
# Strings that start with "a" and end in "y"
options = ["any", "albany", "apple", "world", "hello", ""]
valid_strings = []

for string in options:
    if len(string) <=1:
        continue
    if string[0] != "a":
        continue
    if string[-1] != "y":
        continue
    valid_strings.append(string)


# List comprehension with multiple conditions
valid_strings2 = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == "a"
    if string[-1] == "y"
]
print(f"Valid Strings: {valid_strings}")
print(f"List Comprehension with multiple conditions: {valid_strings2}")


"""
Multiple List Comprehensions - flatten a matrix
"""
# Flattening a matrix (list of lists)
matrix = [[1,2,3], [4,5,6],[7,8,9]]
flatten = []

for row in matrix:
    for num in row:
        flatten.append(num)


flatten2 = [num for row in matrix for num in row ] #secondary loop goes at the end, outer loop goes first
print(f"Flatten: {flatten}")
print(f"Flatten2: {flatten2}")


"""
If/Else in a Comprehension
"""
# Categorize numbers as even or odd
categories = []

for number in range(10):
    if number % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")

# List comprehension
categories2 = ["Even" if number % 2 == 0 else "Odd" for number in range(10)] # Put the filter code first and for loop second

print(f"Categories: {categories}")
print(f"Categories2: {categories2}")


"""
Nested List Comprehension
"""
printer = pprint.PrettyPrinter()
list = []

for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l2)

    list.append(l1)

# List comprehension
# on right side  - for loops - 2 for loops. find first for loop inside of main list
# Whatever is on the left of the last for loop is what gets added
# so, [num for num in range(5)] for _ in range(5) is what is added
# so then inside of that ^^ look for the most right for loop (for _ in range(5))
# then go to next for loop
# 5 lists of 5 lists with numbers 0-4
# _ is anonymous variable (instead of i) 
list2 = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
list3 = [l1 for a in range(5) for l2 in range(5)] # What I tried first - not correct
pprint.pp(list)
print(f"List 2 with comprehension ")
pprint.pp(list2)
print(f"List3 comprehension")
pprint.pp(list3)

# List com with functions - functions aren't written out
def square(x):
    return x**2

#squared_numbers = [square[x] for x in range(10) if valid(x)]


# Creating a dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]

my_dict = {k: v for k, v in pairs}
print(f"My_dict: {my_dict}")


# Set Comprehension
# Removing duplicates from a list while applying a function
# Python knows it's a set and not a dictionary if there are no keys
# sets do not allow duplicate values
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]

unique_squares = {x**2 for x in nums}
print(f"Unique_squares: {unique_squares}")



"""
Generator comprehension
"""
# dont' want to store all the numbers first before you add them together
# This one generates value when needed on the fly bc there is no [] syntax
# if we used sum([x**2 for x in range(1000000)]) it would store all the values first before added them together
sum_of_squares = sum(x**2 for x in range(1000000))
print(f"Sum_of_squares: {sum_of_squares}")