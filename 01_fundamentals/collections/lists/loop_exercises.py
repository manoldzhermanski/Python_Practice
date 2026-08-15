"""
Use a for loop and count how many numbers are greater than 5.
"""

numbers = [4, 7, 2, 9, 6, 3, 8, 1]

count = 0
for number in numbers:
    if number > 5:
        count += 1
        
print(count)

"""
Use a loop to get the sum of the list
"""
    
numbers = [10, 20, 30, 40, 50]

total = 0
for number in numbers:
    total += number
    
print(total)

""""
Raise every element to the power of 2
"""
numbers = [1, 2, 3, 4, 5]

power_of_two = []
for number in numbers:
    power_of_two.append(number ** 2)
    
print(power_of_two)

"""
Modify the existing list
"""
numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers)):
    numbers[i] *= 2
    
print(numbers)

"""
Find the first number that is greater than 15.
"""

numbers = [3, 7, 11, 14, 19, 22, 25]

for number in numbers:
    if number > 15:
        print(number)
        break
    
"""
Create a new list which contains all even numbers
"""

numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        
print(even_numbers)

"""
Use enumerate to print the following:
0: Ivan
1: Maria
2: Georgi
3: Elena

Then use start = 1 agrument in the enumerate function
"""

names = ["Ivan", "Maria", "Georgi", "Elena"]

for index, name in enumerate(names):
    print(f"{index}: {name}")
    
for index, name in enumerate(names, start=1):
    print(f"{index}: {name}")
    
"""
Use a for loop to create a new list, `high_paid`, containing only employees with a salary >= 3000.
"""

employees = [
    {"name": "Ivan", "salary": 3200},
    {"name": "Maria", "salary": 2800},
    {"name": "Georgi", "salary": 3500},
    {"name": "Elena", "salary": 4100},
    {"name": "Petar", "salary": 2900}
]

high_paid = []
for employee in employees:
    if employee["salary"] >= 3000:
        high_paid.append(employee)
        
print(high_paid)
