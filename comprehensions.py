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
options = ["any"]