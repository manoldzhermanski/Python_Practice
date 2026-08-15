from copy import deepcopy

"""
Use the append() method to add 40 and 50 to the list.
"""

numbers = [10, 20, 30]
numbers.append(40)
numbers.append(50)

"""
You have the list numbers = [1, 2, 3]
Using append() and extend() get the following results
[1, 2, 3, [4, 5]]
[1, 2, 3, 4, 5]
"""

numbers = [1, 2, 3]

appended_list = deepcopy(numbers)
extended_list = deepcopy(numbers)

# [1, 2, 3, [4, 5]]
appended_list.append([4, 5]) #type: ignore 

# [1, 2, 3, 4, 5]
extended_list.extend([4, 5])

"""
You have the list numbers = [10, 20, 30, 20, 40, 20, 50]
how many times 20 appears;
the index of the first 20;
the index of 40.
"""
numbers = [10, 20, 30, 20, 40, 20, 50]
print(f'How many times does 20 appears: {numbers.count(20)}')
print(f'Index of the first 20: {numbers.index(20)}')
print(f'Index of 40: {numbers.index(40)}')

"""
You have the following list names = ["Ivan", "Georgi", "Elena"]
Insert "Maria" between "Ivan" and "Georgi"
"""

names = ["Ivan", "Georgi", "Elena"]
names.insert(1, "Maria")

print(names)

"""
You have the list numbers = [10, 20, 30, 40, 50]
remove the last element;
store the removed element in a variable named `removed`;
then remove the first element and store it as well.
"""

numbers = [10, 20, 30, 40, 50]
removed = numbers.pop(-1)
first = numbers.pop(0)

print(removed == 50)
print(first == 10)
print(numbers == [20, 30, 40])

"""
Remove the first 20
"""
numbers = [10, 20, 30, 20, 40, 20]
numbers.remove(20)

print(numbers)

"""
add "cheese" to the end;
add "butter" to the end;
insert "coffee" at position 0;
remove "bread";
remove the last element and store it in removed_item
"""

shopping_cart = [
    "milk",
    "bread",
    "eggs"
]

shopping_cart.extend(["cheese", "butter"])
shopping_cart.insert(0, "coffee")
shopping_cart.remove("bread")
removed_item = shopping_cart.pop(-1)

print(f"Cart: {shopping_cart}")
print(f"Removed item: {removed_item}")

"""
Create a list of sorted employees by their salaries in ascending order
"""

employees = [
    {"name": "Ivan", "salary": 3200},
    {"name": "Maria", "salary": 2800},
    {"name": "Georgi", "salary": 3500},
    {"name": "Elena", "salary": 4100},
]

sorted_employees = sorted(employees, key=(lambda emp: emp["salary"]))
print(sorted_employees)

""""
Sort the following list in ascending and descending order using the sorted() function
"""

numbers = [42, 7, 19, 3, 88, 15]
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print(ascending)
print(descending)

"""
Use any() and all() to answer the following questions about the list numbers = [12, 18, 24, 31, 42]
Is there at least one odd number?
Are all the numbers positive?
Are all the numbers even?
"""

numbers = [12, 18, 24, 31, 42]

print(any(number % 2 != 0 for number in numbers))
print(all(number > 0 for number in numbers))
print(all(number % 2 == 0 for number in numbers))

"""
Using the zip() function create the follwing list named employee_data
[
    ("Ivan", 3200),
    ("Maria", 2800),
    ("Georgi", 3500),
    ("Elena", 4100)
]
"""

names = ["Ivan", "Maria", "Georgi", "Elena"]
salaries = [3200, 2800, 3500, 4100]

employee_data = list(zip(names, salaries))
print(employee_data)

""""
Create the following list
employees = [
    {"name": "Ivan", "salary": 3200},
    {"name": "Maria", "salary": 2800},
    {"name": "Georgi", "salary": 3500},
    {"name": "Elena", "salary": 4100}
]
"""

result = [
    {
        "name": employee[0], "salary": employee[1]
    } for employee in employee_data
]

print(result)

"""
Check if:
    "maria" is in users
    "nikolay" is in users
    "petar" is not in users
"""

users = ["ivan", "maria", "georgi", "petar", "elena"]

print(
    f'"maria" is in users: {"maria" in users}',
    f'"nikolay" is in users: {"nikolay" in users}',
    f'"petar" is not in users: {"petar" not in users}'
    )
