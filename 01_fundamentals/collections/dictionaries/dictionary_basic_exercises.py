"""
Add salary = 3200
"""

employee = {
    "name": "Ivan",
    "age": 25,
    "department": "IT"
}

employee["salary"] = 3200

"""
Print the following:
    the employee's name
    age
    department
    salary
"""

employee = {
    "name": "Ivan",
    "age": 25,
    "department": "IT",
    "salary": 3200
}

for key in employee:
    print(key)
    
"""
Change:
age → 26
salary → 3500
"""
employee["age"] = 26
employee["salary"] = 3500

"""
Check if "salary" is present in employee
"""

print(f"Is 'salary' in employee ? {"salary" in employee}")

"""
Retrieve 'salary' without causing a KeyError.
If the key doesn't exist return 0
"""
print(employee.get("salary", 0))

"""
Print:
    all keys
    all values

Then iterate over the dictionary and print:
 key -> value
"""

for key in employee.keys():
    print(key)
    
for value in employee.values():
    print(value)
    
for key, value in employee.items():
    print(f"{key} -> {value}")

"""
Write code that determines how many keys the dictionary contains.
"""

print(f"How many keys does the dict contain ? {len(employee)}")

"""
Remove "age" key-value pair than add it
"""

del employee["age"]

print(f"After delete: {employee}")

employee.update(
    {
        "age": 26
    }
)

print(f"After update: {employee}")

"""
Safely remove "salary" and add it back
"""

salary = employee.pop("salary", 0)
print(f"After delete: {employee}")

employee["salary"] = salary
print(f"After update: {employee}")

"""
Clear the dictionary
"""

employee.clear()
print(f"After clear: {employee}")
