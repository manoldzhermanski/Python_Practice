"""
Print:
    Ivan
    25
    Sofia
    IT
    3200
"""

employee = {
    "name": "Ivan",
    "personal": {
        "age": 25,
        "city": "Sofia"
    },
    "job": {
        "department": "IT",
        "salary": 3200
    }
}

print(employee["name"],
      employee["personal"]["age"],
      employee["personal"]["city"],
      employee["job"]["department"],
      employee["job"]["salary"])

"""
Modify the city to Plovdiv and the salary to 3500
"""
employee["personal"]["city"] = "Plovdiv"
employee["job"]["salary"] = 3500

"""
Print the following:
Ivan -> IT -> 3200
Maria -> HR -> 2800
"""
employees = [
    {
        "name": "Ivan",
        "job": {
            "department": "IT",
            "salary": 3200
        }
    },
    {
        "name": "Maria",
        "job": {
            "department": "HR",
            "salary": 2800
        }
    }
]

for emp in employees:
    print(f"{emp["name"]} -> {emp["job"]["department"]} -> {emp["job"]["salary"]}")
