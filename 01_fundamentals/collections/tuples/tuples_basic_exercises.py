"""
Print using indexes
"""
person = ("Ivan", 25, "Sofia")

print(person[0]) # Ivan
print(person[1]) # 25
print(person[2]) # Sofia

"""
Print the last 3 unsing negative indexes
"""
numbers = (10, 20, 30, 40, 50)
print(numbers[-1]) # 50
print(numbers[-2]) # 40
print(numbers[-3]) # 30

"""
Print the length of the tuple
"""
colors = ("red", "green", "blue", "yellow")
print(len(colors))

"""
Check if "IT" or "Sales" are in departments
"""
departments = ("IT", "HR", "Finance", "Marketing")
print("IT" in departments)
print("Sales" in departments)

"""
Using slicing print the following:
(2, 3, 4, 5)
(0, 2, 4, 6, 8)
(9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
"""
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers[2:6])
print(numbers[::2])
print(numbers[::-1])

"""
How many times are 10, 20 and 30 encountered ?
"""
numbers = (10, 20, 10, 30, 10, 40, 20)
print(f"10 is encountered {numbers.count(10)} times")
print(f"20 is encountered {numbers.count(20)} times")
print(f"30 is encountered {numbers.count(30)} times")

"""
Find the index of the first encountering of 20 and 40
"""
numbers = (50, 20, 30, 20, 40)
print(f"First 20 is at index {numbers.index(20)}")
print(f"First 40 is at index {numbers.index(40)}")

"""
Unpack the following employee = ("Ivan", 25, "IT")
"""
employee = ("Ivan", 25, "IT")
name, age, dept = employee

"""
Unpack to get the following:
first = 10
middle = [20, 30, 40, 50]
last = 60
"""
numbers = (10, 20, 30, 40, 50, 60)
first, *middle, last = numbers

"""
Unpack only name and department
"""
person = ("Ivan", 25, "Sofia", "IT")
name, _, _, dept = person

"""
Swap values
"""
a = 10
b = 20

print(f"Before: a = {a}, b= {b}")
a, b = b, a
print(f"After: a = {a}, b= {b}")

"""
Using a for loop, print how much every employee earns
"""
employees = [
    ("Ivan", 3200),
    ("Maria", 2800),
    ("Georgi", 3500),
    ("Elena", 3100)
]

for emp in employees:
    print(f"{emp[0]} earns {emp[1]}")

"""
Filter out the employees who earn above 3000
"""
employees = [
    ("Ivan", 3200),
    ("Maria", 2800),
    ("Georgi", 3500),
    ("Elena", 3100)
]

result = [
    emp for emp in employees if emp[1] > 3000
]

print(result)

"""
Write a function called `calculate` which accepts a tuple of numbers and
returns the min, max and sum. Unpack the result of the function
"""
def calculate(num_tuple: tuple[int]):
    return min(num_tuple), max(num_tuple), sum(num_tuple)

numbers = (10, 20, 5, 40, 15)
min_res, max_res, sum_res = calculate(numbers)
print(min_res, max_res, sum_res)

"""
Sort employees by salary
"""
employees = (
    ("Ivan", 3200),
    ("Maria", 2800),
    ("Georgi", 3500),
    ("Elena", 3100)
)

result = sorted(employees,
                key= lambda emp: emp[1])

print(result)