# Python Dictionaries — Cheatsheet

## 1. What is a Dictionary?

A `dict` is an **ordered, mutable collection of key-value pairs**.

```python
employee = {
    "name": "Ivan",
    "age": 25,
    "salary": 3200
}
```

Each entry consists of:

```text
key → value
```

For example:

```text
"name"   → "Ivan"
"age"    → 25
"salary" → 3200
```

### Main characteristics

| Property                 | Dictionary |
| ------------------------ | ---------- |
| Ordered                  | Yes*       |
| Mutable                  | Yes        |
| Allows duplicate keys    | No         |
| Allows duplicate values  | Yes        |
| Indexed by position      | No         |
| Accessed by key          | Yes        |
| Keys must be hashable    | Yes        |
| Values can be any type   | Yes        |
| Allows mixed value types | Yes        |

* Dictionaries preserve **insertion order** in modern Python (Python 3.7+ guarantees this behavior).

---

# 2. Creating Dictionaries

## Empty dictionary

```python
employee = {}
```

or:

```python
employee = dict()
```

---

## Dictionary with values

```python
employee = {
    "name": "Ivan",
    "age": 25,
    "department": "IT"
}
```

---

## Multiple key-value pairs

```python
employee = {
    "name": "Ivan",
    "age": 25,
    "department": "IT",
    "salary": 3200
}
```

---

## Keys can be strings

```python
person = {
    "name": "Ivan",
    "city": "Sofia"
}
```

---

## Keys can be integers

```python
scores = {
    1: 100,
    2: 200,
    3: 300
}
```

---

## Values can have different types

```python
data = {
    "name": "Ivan",
    "age": 25,
    "active": True,
    "salary": 3200.50,
    "skills": ["Python", "SQL"],
    "address": None
}
```

---

# 3. Key-Value Pairs

A dictionary stores relationships between keys and values.

```python
employee = {
    "name": "Ivan",
    "age": 25
}
```

Here:

```text
key       value
----------------
"name" → "Ivan"
"age"  → 25
```

The key identifies the value.

Think of a dictionary like a real-world lookup:

```text
employee ID → employee
product ID  → product
country     → capital
username    → account
```

---

# 4. Dictionary Keys Must Be Unique

You cannot have two distinct entries with the same key.

```python
employee = {
    "name": "Ivan",
    "name": "Maria"
}
```

Python keeps only the last value:

```python
{
    "name": "Maria"
}
```

The second assignment overwrites the first.

---

# 5. Dictionary Values Can Be Duplicated

Values do not need to be unique.

```python
employees = {
    "Ivan": 3200,
    "Maria": 3200,
    "Georgi": 3500
}
```

Both Ivan and Maria can have the same salary.

---

# 6. Accessing Values

Use the key:

```python
employee = {
    "name": "Ivan",
    "age": 25,
    "salary": 3200
}
```

```python
employee["name"]
```

Result:

```python
"Ivan"
```

```python
employee["salary"]
```

Result:

```python
3200
```

---

## Accessing a missing key

```python
employee["department"]
```

If `"department"` doesn't exist, Python raises:

```python
KeyError
```

This is one of the most important differences between:

```python
dict[key]
```

and:

```python
dict.get(key)
```

---

# 7. `get()`

`get()` safely retrieves a value.

```python
employee = {
    "name": "Ivan",
    "age": 25
}
```

```python
employee.get("name")
```

Result:

```python
"Ivan"
```

Missing key:

```python
employee.get("salary")
```

Result:

```python
None
```

No `KeyError` is raised.

---

## Providing a default value

```python
employee.get("salary", 0)
```

Result:

```python
0
```

Another example:

```python
department = employee.get(
    "department",
    "Unknown"
)
```

Result:

```python
"Unknown"
```

---

## `[]` vs `get()`

```python
employee["salary"]
```

If missing:

```text
KeyError
```

While:

```python
employee.get("salary")
```

If missing:

```text
None
```

And:

```python
employee.get("salary", 0)
```

If missing:

```text
0
```

### Rule of thumb

Use:

```python
dict[key]
```

when the key **must exist**.

Use:

```python
dict.get(key)
```

when the key **might not exist**.

---

# 8. Adding New Key-Value Pairs

Dictionaries are mutable.

```python
employee = {
    "name": "Ivan",
    "age": 25
}
```

Add a new key:

```python
employee["salary"] = 3200
```

Now:

```python
{
    "name": "Ivan",
    "age": 25,
    "salary": 3200
}
```

---

# 9. Updating Existing Values

The same syntax is used to update a value.

```python
employee = {
    "name": "Ivan",
    "salary": 3200
}
```

```python
employee["salary"] = 3500
```

Result:

```python
{
    "name": "Ivan",
    "salary": 3500
}
```

### Important

This:

```python
employee["salary"] = 3500
```

does two different things depending on whether the key exists.

If the key exists:

```text
UPDATE
```

If the key doesn't exist:

```text
ADD
```

---

# 10. Modifying Values

You can perform operations directly:

```python
employee = {
    "name": "Ivan",
    "salary": 3200
}

employee["salary"] += 500
```

Result:

```python
{
    "name": "Ivan",
    "salary": 3700
}
```

Another example:

```python
employee["age"] += 1
```

---

# 11. Adding Multiple Key-Value Pairs

## `update()`

```python
employee = {
    "name": "Ivan",
    "age": 25
}

employee.update({
    "salary": 3200,
    "department": "IT"
})
```

Result:

```python
{
    "name": "Ivan",
    "age": 25,
    "salary": 3200,
    "department": "IT"
}
```

---

## Updating existing keys

```python
employee.update({
    "age": 26,
    "salary": 3500
})
```

Existing values are overwritten.

---

## `update()` with keyword arguments

Keys must be valid Python identifiers:

```python
employee.update(
    salary=3500,
    department="IT"
)
```

---

## Dictionary merging with `|`

Python 3.9+ supports:

```python
employee = {
    "name": "Ivan",
    "age": 25
}

job = {
    "department": "IT",
    "salary": 3200
}

result = employee | job
```

Result:

```python
{
    "name": "Ivan",
    "age": 25,
    "department": "IT",
    "salary": 3200
}
```

This creates a **new dictionary**.

---

## In-place merge with `|=`

```python
employee |= job
```

This modifies `employee`.

---

# 12. Removing Elements

## `pop()`

`pop()` removes a key-value pair and returns the value.

```python
employee = {
    "name": "Ivan",
    "age": 25,
    "salary": 3200
}

salary = employee.pop("salary")
```

Now:

```python
salary
```

is:

```python
3200
```

and:

```python
employee
```

is:

```python
{
    "name": "Ivan",
    "age": 25
}
```

---

## `pop()` with default

Without a default:

```python
employee.pop("department")
```

raises:

```python
KeyError
```

With a default:

```python
employee.pop("department", None)
```

returns:

```python
None
```

No error.

---

# 13. `del`

Remove a specific key:

```python
del employee["age"]
```

If the key doesn't exist:

```python
KeyError
```

Unlike `pop()`, `del` does not return the removed value.

---

# 14. `popitem()`

`popitem()` removes and returns the **last inserted key-value pair**.

```python
employee = {
    "name": "Ivan",
    "age": 25,
    "salary": 3200
}

item = employee.popitem()
```

Result:

```python
item
```

is:

```python
("salary", 3200)
```

Dictionary becomes:

```python
{
    "name": "Ivan",
    "age": 25
}
```

Because dictionaries preserve insertion order, `popitem()` removes the last inserted pair.

---

# 15. `clear()`

Remove everything:

```python
employee.clear()
```

Result:

```python
{}
```

The dictionary still exists; it is simply empty.

---

# 16. Removing Methods Comparison

| Method              | Removes by         | Returns something?   | Missing key         |
| ------------------- | ------------------ | -------------------- | ------------------- |
| `pop(key)`          | Key                | Yes — value          | `KeyError`          |
| `pop(key, default)` | Key                | Yes — value/default  | No error            |
| `del dict[key]`     | Key                | No                   | `KeyError`          |
| `popitem()`         | Last inserted pair | Yes — `(key, value)` | `KeyError` if empty |
| `clear()`           | Everything         | No                   | N/A                 |

---

# 17. Checking Whether a Key Exists

Use:

```python
in
```

Example:

```python
employee = {
    "name": "Ivan",
    "age": 25
}
```

```python
"name" in employee
```

Result:

```python
True
```

```python
"salary" in employee
```

Result:

```python
False
```

---

## `not in`

```python
"salary" not in employee
```

Result:

```python
True
```

---

# 18. Important: `in` Checks Keys

When used directly on a dictionary:

```python
"name" in employee
```

checks the **keys**, not the values.

For example:

```python
employee = {
    "name": "Ivan",
    "age": 25
}
```

```python
"Ivan" in employee
```

returns:

```python
False
```

because `"Ivan"` is a value, not a key.

---

# 19. Checking Whether a Value Exists

Use:

```python
in employee.values()
```

Example:

```python
employee = {
    "name": "Ivan",
    "age": 25
}
```

```python
"Ivan" in employee.values()
```

Result:

```python
True
```

```python
30 in employee.values()
```

Result:

```python
False
```

---

# 20. Keys, Values, and Items

Dictionaries provide three important views:

```python
employee.keys()
employee.values()
employee.items()
```

---

## `keys()`

```python
employee = {
    "name": "Ivan",
    "age": 25,
    "salary": 3200
}

employee.keys()
```

Conceptually:

```text
dict_keys(["name", "age", "salary"])
```

Convert to a list if needed:

```python
list(employee.keys())
```

---

## `values()`

```python
employee.values()
```

Conceptually:

```text
dict_values(["Ivan", 25, 3200])
```

Convert:

```python
list(employee.values())
```

---

## `items()`

```python
employee.items()
```

Conceptually:

```text
dict_items([
    ("name", "Ivan"),
    ("age", 25),
    ("salary", 3200)
])
```

Each item is a:

```python
(key, value)
```

pair.

---

# 21. Iterating Over Dictionary Keys

The most basic dictionary loop:

```python
employee = {
    "name": "Ivan",
    "age": 25,
    "salary": 3200
}

for key in employee:
    print(key)
```

Output:

```text
name
age
salary
```

You can also write:

```python
for key in employee.keys():
    print(key)
```

But:

```python
for key in employee:
```

is usually preferred.

---

# 22. Iterating Over Dictionary Values

```python
for value in employee.values():
    print(value)
```

Output:

```text
Ivan
25
3200
```

---

# 23. Iterating Over Keys and Values

Use:

```python
for key, value in employee.items():
    print(key, value)
```

Output:

```text
name Ivan
age 25
salary 3200
```

This is one of the most important dictionary patterns to know.

---

# 24. Dictionary `items()` Unpacking

This:

```python
for key, value in employee.items():
    ...
```

works because every item is a two-element tuple:

```python
("name", "Ivan")
```

Python unpacks it into:

```python
key = "name"
value = "Ivan"
```

---

# 25. Length of a Dictionary

Use:

```python
len(employee)
```

Example:

```python
employee = {
    "name": "Ivan",
    "age": 25,
    "salary": 3200
}
```

```python
len(employee)
```

Result:

```python
3
```

The length is the number of **key-value pairs**.

---

# 26. Dictionary Truthiness

An empty dictionary is falsy:

```python
{}
```

Therefore:

```python
if not employee:
    print("Dictionary is empty")
```

For a non-empty dictionary:

```python
if employee:
    print("Dictionary contains data")
```

Prefer this:

```python
if employee:
```

over:

```python
if len(employee) > 0:
```

---

# 27. `None` vs Empty Dictionary

These are different:

```python
data = None
```

means:

> There is no dictionary/value.

While:

```python
data = {}
```

means:

> There is a dictionary, but it contains no entries.

Check explicitly:

```python
if data is None:
    ...
```

Check emptiness:

```python
if not data:
    ...
```

Be aware that:

```python
not None
```

and:

```python
not {}
```

are both `True`.

---

# 28. Dictionary Keys and Hashability

Dictionary keys must be **hashable**.

Common valid keys:

```python
"string"
42
3.14
True
None
(1, 2)
```

Example:

```python
data = {
    "name": "Ivan",
    42: "answer",
    (1, 2): "coordinates"
}
```

---

## Lists cannot be dictionary keys

This is invalid:

```python
data = {
    [1, 2]: "value"
}
```

It raises:

```python
TypeError: unhashable type: 'list'
```

---

## Sets cannot be dictionary keys

Also invalid:

```python
data = {
    {1, 2}: "value"
}
```

because sets are mutable and unhashable.

---

## Tuples can be keys

A tuple can be a key if all of its elements are hashable:

```python
locations = {
    (42.7, 23.3): "Sofia"
}
```

But a tuple containing a list is not hashable:

```python
{
    ([1, 2], 3): "value"
}
```

---

# 29. Why Must Dictionary Keys Be Hashable?

Dictionaries use a **hash table** internally.

The hash of a key helps Python quickly locate the corresponding value.

This is why dictionaries provide very fast average-case lookup:

```python
employee["salary"]
```

The key must have a stable hash value.

Mutable objects such as lists cannot safely be used as keys because their contents can change.

---

# 30. Dictionary Key Equality

Dictionary keys are considered the same when they compare equal and have compatible hashes.

For example:

```python
data = {
    1: "one",
    True: "true"
}
```

You may be surprised that these represent the same key because:

```python
1 == True
```

is:

```python
True
```

Therefore the second entry overwrites the first.

---

# 31. Nested Dictionaries

Dictionaries can contain other dictionaries.

```python
employee = {
    "name": "Ivan",
    "address": {
        "city": "Sofia",
        "country": "Bulgaria"
    }
}
```

Access the nested value:

```python
employee["address"]["city"]
```

Result:

```python
"Sofia"
```

---

# 32. Modifying Nested Dictionaries

```python
employee["address"]["city"] = "Plovdiv"
```

Now:

```python
{
    "name": "Ivan",
    "address": {
        "city": "Plovdiv",
        "country": "Bulgaria"
    }
}
```

---

# 33. Adding to Nested Dictionaries

```python
employee["address"]["postcode"] = "4000"
```

Result:

```python
{
    "name": "Ivan",
    "address": {
        "city": "Plovdiv",
        "country": "Bulgaria",
        "postcode": "4000"
    }
}
```

---

# 34. Lists Inside Dictionaries

Values can be lists.

```python
employee = {
    "name": "Ivan",
    "skills": [
        "Python",
        "SQL",
        "Git"
    ]
}
```

Access the list:

```python
employee["skills"]
```

Access an individual skill:

```python
employee["skills"][0]
```

Result:

```python
"Python"
```

Add a skill:

```python
employee["skills"].append("Docker")
```

---

# 35. Dictionaries Inside Lists

This structure is extremely important for data work.

```python
employees = [
    {
        "name": "Ivan",
        "salary": 3200
    },
    {
        "name": "Maria",
        "salary": 2800
    },
    {
        "name": "Georgi",
        "salary": 3500
    }
]
```

Access the first employee:

```python
employees[0]
```

Access the first employee's name:

```python
employees[0]["name"]
```

Result:

```python
"Ivan"
```

Access the second employee's salary:

```python
employees[1]["salary"]
```

Result:

```python
2800
```

---

# 36. Iterating Over a List of Dictionaries

```python
for employee in employees:
    print(employee["name"])
```

Output:

```text
Ivan
Maria
Georgi
```

Print multiple fields:

```python
for employee in employees:
    print(
        employee["name"],
        employee["salary"]
    )
```

---

# 37. Filtering a List of Dictionaries

Find employees with salary greater than 3000:

```python
high_paid = [
    employee
    for employee in employees
    if employee["salary"] > 3000
]
```

Result:

```python
[
    {
        "name": "Ivan",
        "salary": 3200
    },
    {
        "name": "Georgi",
        "salary": 3500
    }
]
```

---

# 38. Extracting a Value from a List of Dictionaries

Get all employee names:

```python
names = [
    employee["name"]
    for employee in employees
]
```

Result:

```python
[
    "Ivan",
    "Maria",
    "Georgi"
]
```

Get all salaries:

```python
salaries = [
    employee["salary"]
    for employee in employees
]
```

---

# 39. Updating Values in a List of Dictionaries

Increase every salary by 10%:

```python
for employee in employees:
    employee["salary"] *= 1.10
```

This modifies the dictionaries in the list.

---

# 40. Safe Access in Nested Dictionaries

Consider:

```python
employee = {
    "name": "Ivan",
    "address": {
        "city": "Sofia"
    }
}
```

This works:

```python
employee["address"]["city"]
```

But if `"address"` might not exist:

```python
employee["address"]["city"]
```

can raise:

```python
KeyError
```

Use `get()`:

```python
address = employee.get("address", {})
city = address.get("city")
```

This is safer when data may be incomplete.

---

# 41. The `get()` Pattern for Nested Data

```python
city = (
    employee
    .get("address", {})
    .get("city")
)
```

If `"address"` doesn't exist:

```python
{}
```

is used.

Then:

```python
{}.get("city")
```

returns:

```python
None
```

This pattern is useful when processing messy external data.

---

# 42. `setdefault()`

`setdefault()` returns the value for a key.

If the key doesn't exist, it creates it with a default value.

Example:

```python
employee = {
    "name": "Ivan"
}

age = employee.setdefault("age", 25)
```

Now:

```python
age
```

is:

```python
25
```

and:

```python
employee
```

is:

```python
{
    "name": "Ivan",
    "age": 25
}
```

---

## Existing key with `setdefault()`

```python
employee = {
    "name": "Ivan",
    "age": 25
}

age = employee.setdefault("age", 100)
```

The existing value is preserved:

```python
age == 25
```

Dictionary:

```python
{
    "name": "Ivan",
    "age": 25
}
```

The default `100` is ignored.

---

# 43. `setdefault()` vs `get()`

`get()`:

```python
value = data.get("key", default)
```

does **not** add the key.

`setdefault()`:

```python
value = data.setdefault("key", default)
```

**does** add the key if missing.

Example:

```python
data = {}

value = data.get("name", "Unknown")
```

Dictionary remains:

```python
{}
```

But:

```python
data = {}

value = data.setdefault("name", "Unknown")
```

Dictionary becomes:

```python
{
    "name": "Unknown"
}
```

---

# 44. Dictionary Comprehensions

Dictionary comprehensions create dictionaries in a compact way.

Basic syntax:

```python
{
    key_expression: value_expression
    for item in iterable
}
```

Example:

```python
numbers = [1, 2, 3, 4]

squares = {
    number: number ** 2
    for number in numbers
}
```

Result:

```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16
}
```

---

# 45. Dictionary Comprehension with Strings

```python
names = ["Ivan", "Maria", "Georgi"]

name_lengths = {
    name: len(name)
    for name in names
}
```

Result:

```python
{
    "Ivan": 4,
    "Maria": 5,
    "Georgi": 6
}
```

---

# 46. Dictionary Comprehension with Filtering

```python
numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}
```

Result:

```python
{
    2: 4,
    4: 16
}
```

---

# 47. Dictionary Comprehension from Another Dictionary

```python
prices = {
    "apple": 2,
    "banana": 3,
    "orange": 4
}
```

Create a dictionary with prices doubled:

```python
new_prices = {
    fruit: price * 2
    for fruit, price in prices.items()
}
```

Result:

```python
{
    "apple": 4,
    "banana": 6,
    "orange": 8
}
```

---

# 48. Filtering a Dictionary

Keep only employees with salary above 3000:

```python
employees = {
    "Ivan": 3200,
    "Maria": 2800,
    "Georgi": 3500
}

high_paid = {
    name: salary
    for name, salary in employees.items()
    if salary > 3000
}
```

Result:

```python
{
    "Ivan": 3200,
    "Georgi": 3500
}
```

---

# 49. Transforming Dictionary Values

```python
prices = {
    "apple": 2,
    "banana": 3,
    "orange": 4
}

updated_prices = {
    fruit: price * 1.10
    for fruit, price in prices.items()
}
```

Result:

```python
{
    "apple": 2.2,
    "banana": 3.3,
    "orange": 4.4
}
```

---

# 50. Transforming Dictionary Keys

```python
data = {
    "first_name": "Ivan",
    "last_name": "Petrov"
}
```

Convert keys to uppercase:

```python
result = {
    key.upper(): value
    for key, value in data.items()
}
```

Result:

```python
{
    "FIRST_NAME": "Ivan",
    "LAST_NAME": "Petrov"
}
```

---

# 51. Creating a Dictionary from Two Lists

Given:

```python
names = [
    "Ivan",
    "Maria",
    "Georgi"
]

salaries = [
    3200,
    2800,
    3500
]
```

Use `zip()`:

```python
employees = dict(
    zip(names, salaries)
)
```

Result:

```python
{
    "Ivan": 3200,
    "Maria": 2800,
    "Georgi": 3500
}
```

This is a very useful pattern.

---

# 52. `dict()` Constructor

You can create dictionaries using `dict()`.

```python
employee = dict(
    name="Ivan",
    age=25,
    salary=3200
)
```

Result:

```python
{
    "name": "Ivan",
    "age": 25,
    "salary": 3200
}
```

---

# 53. `dict()` from a List of Tuples

```python
data = [
    ("name", "Ivan"),
    ("age", 25),
    ("salary", 3200)
]

employee = dict(data)
```

Result:

```python
{
    "name": "Ivan",
    "age": 25,
    "salary": 3200
}
```

---

# 54. `dict.fromkeys()`

Creates a dictionary using a collection of keys.

```python
keys = ["name", "age", "salary"]

data = dict.fromkeys(keys)
```

Result:

```python
{
    "name": None,
    "age": None,
    "salary": None
}
```

Provide a default value:

```python
data = dict.fromkeys(
    keys,
    0
)
```

Result:

```python
{
    "name": 0,
    "age": 0,
    "salary": 0
}
```

---

# 55. Important `fromkeys()` Mutable-Value Pitfall

Be careful:

```python
data = dict.fromkeys(
    ["a", "b", "c"],
    []
)
```

The same list object is used as the value for every key.

Therefore:

```python
data["a"].append(1)
```

will make:

```python
{
    "a": [1],
    "b": [1],
    "c": [1]
}
```

If you need independent lists, use a comprehension:

```python
data = {
    key: []
    for key in ["a", "b", "c"]
}
```

Now each key gets a separate list.

---

# 56. Dictionary Copying

This is important because dictionaries are mutable.

```python
a = {
    "name": "Ivan",
    "age": 25
}

b = a
```

`b` is not a copy.

Both variables refer to the same dictionary.

```python
b["age"] = 30
```

Now:

```python
a["age"]
```

is also:

```python
30
```

---

# 57. Shallow Copy

Use:

```python
b = a.copy()
```

Example:

```python
a = {
    "name": "Ivan",
    "age": 25
}

b = a.copy()

b["age"] = 30
```

Now:

```python
a
```

is:

```python
{
    "name": "Ivan",
    "age": 25
}
```

and:

```python
b
```

is:

```python
{
    "name": "Ivan",
    "age": 30
}
```

---

# 58. Other Ways to Make a Shallow Copy

```python
b = a.copy()
```

or:

```python
b = dict(a)
```

or:

```python
b = {**a}
```

All create a new outer dictionary.

---

# 59. Nested Dictionaries and Shallow Copy

Consider:

```python
a = {
    "name": "Ivan",
    "address": {
        "city": "Sofia"
    }
}
```

Then:

```python
b = a.copy()
```

The outer dictionary is copied, but the nested dictionary is still shared.

```python
b["address"]["city"] = "Plovdiv"
```

This also changes:

```python
a["address"]["city"]
```

because both dictionaries reference the same nested object.

---

# 60. Deep Copy

For a completely independent recursive copy:

```python
import copy

b = copy.deepcopy(a)
```

Now nested mutable objects are copied as well.

```python
b["address"]["city"] = "Plovdiv"
```

does not change `a`.

---

# 61. Dictionary Unpacking

Python allows dictionary unpacking with `**`.

```python
person = {
    "name": "Ivan",
    "age": 25
}

result = {
    **person,
    "city": "Sofia"
}
```

Result:

```python
{
    "name": "Ivan",
    "age": 25,
    "city": "Sofia"
}
```

---

# 62. Overwriting During Dictionary Unpacking

Later values overwrite earlier values.

```python
person = {
    "name": "Ivan",
    "age": 25
}

result = {
    **person,
    "age": 30
}
```

Result:

```python
{
    "name": "Ivan",
    "age": 30
}
```

---

# 63. Merging Dictionaries with Unpacking

```python
personal = {
    "name": "Ivan",
    "age": 25
}

job = {
    "department": "IT",
    "salary": 3200
}

employee = {
    **personal,
    **job
}
```

Result:

```python
{
    "name": "Ivan",
    "age": 25,
    "department": "IT",
    "salary": 3200
}
```

Modern Python can also use:

```python
employee = personal | job
```

---

# 64. Dictionary Equality

Two dictionaries are equal if they contain the same key-value pairs.

```python
a = {
    "name": "Ivan",
    "age": 25
}

b = {
    "age": 25,
    "name": "Ivan"
}
```

```python
a == b
```

Result:

```python
True
```

The insertion order does not affect dictionary equality.

---

# 65. Dictionary Identity

`==` checks whether dictionaries contain equal data.

`is` checks whether they are the **same object**.

```python
a = {"name": "Ivan"}
b = {"name": "Ivan"}
```

```python
a == b
```

is:

```python
True
```

But:

```python
a is b
```

is:

```python
False
```

because they are separate dictionary objects.

---

# 66. Dictionary Ordering

Modern Python dictionaries preserve insertion order.

```python
data = {}

data["a"] = 1
data["b"] = 2
data["c"] = 3
```

Iteration gives:

```text
a
b
c
```

If you delete and re-add a key:

```python
del data["b"]
data["b"] = 20
```

the key is inserted at the end:

```text
a
c
b
```

---

# 67. Dictionaries Are Not Indexed by Position

This does **not** mean:

```python
data[0]
```

"give me the first item."

It means:

> Find the value whose key is `0`.

Example:

```python
data = {
    "name": "Ivan",
    "age": 25
}
```

This:

```python
data[0]
```

raises:

```python
KeyError
```

because there is no key `0`.

If you actually want the first inserted item:

```python
first_item = next(iter(data.items()))
```

Result:

```python
("name", "Ivan")
```

---

# 68. Converting Dictionary Views to Lists

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

Keys:

```python
list(data.keys())
```

Values:

```python
list(data.values())
```

Items:

```python
list(data.items())
```

---

# 69. Sorting Dictionary Keys

```python
data = {
    "banana": 3,
    "apple": 2,
    "orange": 4
}
```

```python
sorted(data)
```

Result:

```python
[
    "apple",
    "banana",
    "orange"
]
```

By default, iterating over a dictionary sorts nothing; `sorted()` explicitly creates a sorted list.

---

# 70. Sorting a Dictionary by Keys

```python
sorted_data = {
    key: data[key]
    for key in sorted(data)
}
```

Result:

```python
{
    "apple": 2,
    "banana": 3,
    "orange": 4
}
```

---

# 71. Sorting a Dictionary by Values

```python
data = {
    "banana": 3,
    "apple": 2,
    "orange": 4
}
```

```python
sorted_data = dict(
    sorted(
        data.items(),
        key=lambda item: item[1]
    )
)
```

Result:

```python
{
    "apple": 2,
    "banana": 3,
    "orange": 4
}
```

Descending:

```python
sorted_data = dict(
    sorted(
        data.items(),
        key=lambda item: item[1],
        reverse=True
    )
)
```

---

# 72. Sorting a Dictionary by Key

```python
sorted_data = dict(
    sorted(
        data.items(),
        key=lambda item: item[0]
    )
)
```

Or more simply:

```python
sorted_data = dict(sorted(data.items()))
```

---

# 73. Finding the Maximum Value

Given:

```python
employees = {
    "Ivan": 3200,
    "Maria": 2800,
    "Georgi": 3500
}
```

Maximum salary:

```python
max(employees.values())
```

Result:

```python
3500
```

---

# 74. Finding the Employee with the Highest Salary

Use `key`:

```python
highest_paid = max(
    employees,
    key=employees.get
)
```

Result:

```python
"Georgi"
```

Then:

```python
employees[highest_paid]
```

gives:

```python
3500
```

---

# 75. Finding the Employee with the Lowest Salary

```python
lowest_paid = min(
    employees,
    key=employees.get
)
```

Result:

```python
"Maria"
```

---

# 76. `max()` / `min()` with Dictionary Items

You can also work directly with `.items()`:

```python
highest_paid = max(
    employees.items(),
    key=lambda item: item[1]
)
```

Result:

```python
("Georgi", 3500)
```

This is useful when you need both the key and the value.

---

# 77. `sum()` with Dictionary Values

```python
total_salary = sum(
    employees.values()
)
```

Average:

```python
average_salary = (
    sum(employees.values())
    / len(employees)
)
```

Make sure the dictionary is not empty before dividing by its length.

---

# 78. `any()` with Dictionaries

When used directly:

```python
any(data)
```

iterates over dictionary keys.

Example:

```python
data = {
    "a": 1,
    "b": 2
}
```

```python
any(data)
```

checks the truthiness of the keys.

More commonly, use a generator expression for a specific condition:

```python
any(
    salary > 3000
    for salary in employees.values()
)
```

This checks whether **at least one employee** earns more than 3000.

---

# 79. `all()` with Dictionaries

Example:

```python
all(
    salary > 2000
    for salary in employees.values()
)
```

Returns:

```python
True
```

if every salary is above 2000.

---

# 80. Counting with Dictionaries

Dictionaries are extremely useful for counting frequencies.

Example:

```python
numbers = [
    1, 2, 2, 3, 3, 3
]
```

We want:

```python
{
    1: 1,
    2: 2,
    3: 3
}
```

---

## Manual counting

```python
counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1
```

---

## Using `get()`

A cleaner approach:

```python
counts = {}

for number in numbers:
    counts[number] = counts.get(number, 0) + 1
```

This is a very important dictionary pattern.

---

# 81. Counting Strings

```python
words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple"
]
```

```python
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1
```

Result:

```python
{
    "apple": 3,
    "banana": 2,
    "orange": 1
}
```

---

# 82. Grouping Data with Dictionaries

Suppose:

```python
employees = [
    {"name": "Ivan", "department": "IT"},
    {"name": "Maria", "department": "HR"},
    {"name": "Georgi", "department": "IT"}
]
```

We want:

```python
{
    "IT": ["Ivan", "Georgi"],
    "HR": ["Maria"]
}
```

Using `setdefault()`:

```python
groups = {}

for employee in employees:
    department = employee["department"]

    groups.setdefault(
        department,
        []
    ).append(employee["name"])
```

Result:

```python
{
    "IT": ["Ivan", "Georgi"],
    "HR": ["Maria"]
}
```

This is a very useful real-world pattern.

---

# 83. Grouping with `defaultdict`

Python also provides:

```python
from collections import defaultdict
```

Example:

```python
groups = defaultdict(list)

for employee in employees:
    department = employee["department"]

    groups[department].append(
        employee["name"]
    )
```

Result:

```python
{
    "IT": ["Ivan", "Georgi"],
    "HR": ["Maria"]
}
```

`defaultdict` is useful, but first master the normal dictionary patterns with `get()` and `setdefault()`.

---

# 84. `defaultdict(int)` for Counting

Instead of:

```python
counts = {}

for number in numbers:
    counts[number] = counts.get(number, 0) + 1
```

you can use:

```python
from collections import defaultdict

counts = defaultdict(int)

for number in numbers:
    counts[number] += 1
```

Missing keys automatically start at:

```python
0
```

---

# 85. `Counter`

For frequency counting, Python also provides:

```python
from collections import Counter
```

Example:

```python
numbers = [
    1, 2, 2, 3, 3, 3
]

counts = Counter(numbers)
```

Result conceptually:

```python
Counter({
    3: 3,
    2: 2,
    1: 1
})
```

Most common:

```python
counts.most_common()
```

or:

```python
counts.most_common(2)
```

`Counter` is worth knowing, but it is part of the `collections` module rather than the core `dict` API.

---

# 86. Inverting a Dictionary

Suppose:

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

Swap keys and values:

```python
inverted = {
    value: key
    for key, value in data.items()
}
```

Result:

```python
{
    1: "a",
    2: "b",
    3: "c"
}
```

### Important caveat

This only works safely if the values are unique and hashable.

If:

```python
data = {
    "a": 1,
    "b": 1
}
```

then:

```python
{
    value: key
    for key, value in data.items()
}
```

produces:

```python
{
    1: "b"
}
```

because duplicate keys are overwritten.

---

# 87. Dictionary Comprehension vs Loop

This:

```python
squares = {
    number: number ** 2
    for number in numbers
}
```

is equivalent to:

```python
squares = {}

for number in numbers:
    squares[number] = number ** 2
```

Use comprehensions when they make the transformation obvious.

Don't force a complex algorithm into one giant comprehension.

---

# 88. Conditional Values in Dictionary Comprehensions

You can use conditional expressions:

```python
numbers = [1, 2, 3, 4]

labels = {
    number: "even" if number % 2 == 0 else "odd"
    for number in numbers
}
```

Result:

```python
{
    1: "odd",
    2: "even",
    3: "odd",
    4: "even"
}
```

---

# 89. Conditional Keys in Dictionary Comprehensions

You can filter which entries are included:

```python
numbers = [1, 2, 3, 4]

result = {
    number: number ** 2
    for number in numbers
    if number > 2
}
```

Result:

```python
{
    3: 9,
    4: 16
}
```

---

# 90. Nested Dictionary Comprehensions

Possible:

```python
matrix = {
    i: {
        j: i * j
        for j in range(1, 4)
    }
    for i in range(1, 4)
}
```

Result:

```python
{
    1: {1: 1, 2: 2, 3: 3},
    2: {1: 2, 2: 4, 3: 6},
    3: {1: 3, 2: 6, 3: 9}
}
```

This is powerful, but readability matters.

---