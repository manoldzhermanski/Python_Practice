"""
Output the following:
    the first element
    the last element
    the third element
    the second-to-last element
"""

numbers = [10, 25, 37, 42, 58, 63, 71]

print(
    f"the first element: {numbers[0]}",
    f"the last element: {numbers[-1]}",
    f"the third element: {numbers[2]}",
    f"the second-to-last element: {numbers[-2]}"
      )

"""
Modify the list numbers = [10, 20, 30, 40, 50]
using the indexes of the elements to get the following result:
[100, 20, 300, 40, 500]
"""
    
numbers = [10, 20, 30, 40, 50]
numbers[0] *=10
numbers[2] *= 10
numbers[-1] *=10

print(numbers)

"""
Create the following lists:
first_three      # [0, 1, 2]
middle           # [3, 4, 5, 6]
last_three       # [7, 8, 9]
even_positions   # [0, 2, 4, 6, 8]
reversed_numbers # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first_three = numbers[0:3]
middle = numbers[3:-3]
last_three = numbers[-3:]
even_positions = numbers[::2]
reversed_numbers = numbers[::-1]

print(
    f"first_three: {first_three}",
    f"middle: {middle}",
    f"last_three: {last_three}",
    f"even_positions: {even_positions}",
    f"reversed_numbers: {reversed_numbers}"
    )

"""
Output the following:
1. length of list
2. first city
3. Middle city
4. Last city
"""

cities = ["Sofia", "Plovdiv", "Varna", "Burgas", "Ruse"]

print(f"Length: {len(cities)}")
print(f"First city: {cities[0]}")
print(f"Middle city: {cities[len(cities) // 2]}")
print(f"Last city: {cities[-1]}")

"""
From the list numbers = [5, 10, 15, 20, 25, 30]
Get the following result: [30, 25, 20]
"""
numbers = [5, 10, 15, 20, 25, 30]
result = numbers[-1:-4:-1]

print(result)
