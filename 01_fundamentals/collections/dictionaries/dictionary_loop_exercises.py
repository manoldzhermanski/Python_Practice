"""
Print only the keys
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
Print only values
"""
for value in employee.values():
    print(value)
    
"""
Print all int and float values
"""

data = {
    "name": "Ivan",
    "age": 25,
    "salary": 3200,
    "department": "IT",
    "years_experience": 3
}

for field in data.values():
    if not isinstance(field, str):
        print(field)
        
"""
Calculate the sum of all numeric values
"""

total = 0
for field in data.values():
    if not isinstance(field, str):
        total += field
        
print(total)

"""
Find the largest value
"""

scores = {
    "Ivan": 82,
    "Maria": 95,
    "Georgi": 78,
    "Elena": 91
}

max_score = 0
score_owner = None
for name, score in scores.items():
    if score > max_score:
        max = score
        score_owner = name
    
"""
Count how many students scored at least 80.
Create a new dictionary containing only students with scores >= 80.
"""
scores = {
    "Ivan": 82,
    "Maria": 95,
    "Georgi": 78,
    "Elena": 91,
    "Petar": 67
}

count = 0
for score in scores.values():
    if score > 80:
        count += 1
        
top_students = {
    student: score
    for student, score in scores.items() if score > 80
}

"""
Extract name, salaries and IT employees in separate lists
"""
employees = [
    {"name": "Ivan", "department": "IT", "salary": 3200},
    {"name": "Maria", "department": "HR", "salary": 2800},
    {"name": "Georgi", "department": "IT", "salary": 3500},
    {"name": "Elena", "department": "Finance", "salary": 3100}
]

emp_names = [
    emp["name"] for emp in employees
]

emp_salaries = [
    emp["salary"] for emp in employees
]

it_emps = [
    emp for emp in employees if emp["department"] == "IT"
]

"""
Create a list containing employees whose salary is greater than 3000.
"""
highest_salaries = [
    emp for emp in employees if emp["salary"] > 3000
]

"""
Modify the existing dictiony and give everyone a 10% raise
"""

for emp in employees:
    emp["salary"] *= 1.1
