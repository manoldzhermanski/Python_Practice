"""
Using list comprehension, square the following list:
numbers = [1, 2, 3, 4, 5]
"""

numbers = [1, 2, 3, 4, 5]
squares = [
    number ** 2 for number in numbers
]

""""
Using list comprehension, create a new list in which every element is doubled
"""

numbers = [1, 2, 3, 4, 5]
doubled = [
    number * 2 for number in numbers
]

"""
Using list comprehension, create a new list where the even numbers are selected from the original list and doubled
"""

numbers = [1, 2, 3, 4, 5, 6]

result = [
    number * 2 for number in numbers if number % 2 == 0
]

""""
Using list comprehension, create a new list containing all even numbers from the original list
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [
    number for number in numbers if number % 2 == 0
]

"""
Using list comprehension, create a new list contaning the squares of all numbers bigger than 10
"""

numbers = [3, 8, 12, 5, 20, 7, 14]

result = [
    number ** 2 for number in numbers if number > 10
]

"""
Using list comprehension, create a new list containing all names with at least 5 letters
"""

names = ["Ivan", "Alex", "Maria", "George", "Jo", "Elena"]

result = [
    name for name in names if len(name) >= 5
]

"""
Using list comprehension, create a new list in which all names are uppercase
"""

names = ["ivan", "maria", "georgi", "elena"]

result = [
    name.upper() for name in names
]


"""
Using list comprehension, create a new list in which every element is categorized as "odd" or "even"
based on the given list.
"""

numbers = [1, 2, 3, 4, 5, 6]

result = [
    "even" if number % 2 == 0 else "odd" for number in numbers
]

"""
Using list comprehension, create a list containing only the employee names
"""
employees = [
    {"name": "Ivan", "salary": 3200},
    {"name": "Maria", "salary": 2800},
    {"name": "Georgi", "salary": 3500},
]

names = [
    employee["name"] for employee in employees
]

"""
Using list comprehension, create a list containing the names of the employees whose salary is at least 3000
"""

at_least_3000 = [
    employee["name"] for employee in employees if employee["salary"] >= 3000
]

print(at_least_3000)
