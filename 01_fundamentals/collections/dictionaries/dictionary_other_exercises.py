"""
Count the letters in the word 'banana'
"""

word = "banana"

letter_count = {}
for char in word:
    letter_count[char] = letter_count.get(char, 0) + 1

print(letter_count)

"""
Count the frequency of the mentioned words
"""
words = [
    "python",
    "sql",
    "python",
    "java",
    "sql",
    "python"
]

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

"""
Find the most mentioned word
"""
most_common_word = None
max_count = 0

for word, count in word_count.items():
    if count > max_count:
        most_common_word = word
        max_count = count

print(f"Most common word is {most_common_word}, mentioned {max_count} times")

"""
Group by department
"""
employees = [
    {"name": "Ivan", "department": "IT"},
    {"name": "Maria", "department": "HR"},
    {"name": "Georgi", "department": "IT"},
    {"name": "Elena", "department": "Finance"},
    {"name": "Petar", "department": "IT"}
]

dept_groups = {}

for employee in employees:
    department = employee["department"]

    dept_groups.setdefault(department, []).append(employee["name"])

print(dept_groups)

"""
Count the number of employees in every department
"""

employees = [
    {"name": "Ivan", "department": "IT"},
    {"name": "Maria", "department": "HR"},
    {"name": "Georgi", "department": "IT"},
    {"name": "Elena", "department": "Finance"},
    {"name": "Petar", "department": "IT"}
]

emps_by_dept = {}

for employee in employees:
    department = employee["department"]
    emps_by_dept[department] = emps_by_dept.setdefault(department, 0) + 1

print(emps_by_dept)

"""
Calculate the average salary for every department
"""
employees = [
    {"name": "Ivan", "department": "IT", "salary": 3200},
    {"name": "Georgi", "department": "IT", "salary": 3500},
    {"name": "Maria", "department": "HR", "salary": 2800},
    {"name": "Elena", "department": "Finance", "salary": 3100}
]

avg_salary_by_dept = {}
for employee in employees:
    department = employee["department"]

    if department not in avg_salary_by_dept:
        avg_salary_by_dept[department] = {
            "total_salary": 0,
            "employee_count": 0
        }

    avg_salary_by_dept[department]["total_salary"] += employee["salary"]
    avg_salary_by_dept[department]["employee_count"] += 1

for dept, dept_info in avg_salary_by_dept.items():
    print(f"""Department Name: {dept}, Avg Salary: {dept_info["total_salary"] / dept_info["employee_count"]:.2f}""")


"""
Convert to dict
"""
names = ["Ivan", "Maria", "Georgi"]
ages = [25, 30, 28]

result = dict(zip(names, ages))
print(result)

"""
Create a list
"""
scores = {
    "Ivan": 82,
    "Maria": 95,
    "Georgi": 78
}

result = [
    (name, score) for name, score in scores.items()
]

print(result)

"""
Invert dictionary
"""
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

result = {
    value: key for key, value in data.items()
}

print(result)

"""
Invert dict
"""
data = {
    "a": 1,
    "b": 1,
    "c": 2
}

inverted_dict = {}
for letter, count in data.items():
    inverted_dict.setdefault(count, []).append(letter)

print(inverted_dict)