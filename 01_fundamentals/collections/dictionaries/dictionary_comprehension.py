"""
Create the following:
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
"""

result = {
    i: i ** 2 for i in range(1, 6)
}

"""
Create the following dictionary:
{
    1: "odd",
    2: "even",
    3: "odd",
    4: "even",
    5: "odd"
}
"""

result = {
    number: "even" if number % 2 == 0 else "odd" for number in range(1, 6)
}

print(result)

"""
Create a new dictionary containing only scores >= 90.
"""
scores = {
    "Ivan": 82,
    "Maria": 95,
    "Georgi": 78,
    "Elena": 91
}

result = {
    name: score for name, score in scores.items() if score >= 90
}
