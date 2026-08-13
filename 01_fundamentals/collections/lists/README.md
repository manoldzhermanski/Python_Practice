# Python Lists — Cheatsheet

## 1. What is a List?

A `list` is an **ordered, mutable collection** that can contain multiple values.

```python
numbers = [10, 20, 30, 40]
```

Lists can contain different data types:

```python
data = [10, "Ivan", 3.14, True, None]
```

Lists can contain other lists and dictionaries:

```python
data = [
    [1, 2, 3],
    {"name": "Ivan", "age": 25}
]
```

### Main characteristics

| Property           | List |
| ------------------ | ---- |
| Ordered            | Yes  |
| Mutable            | Yes  |
| Allows duplicates  | Yes  |
| Indexed            | Yes  |
| Allows mixed types | Yes  |

---

# 2. Creating Lists

Empty list:

```python
items = []
```

With values:

```python
numbers = [1, 2, 3, 4, 5]
```

Using `list()`:

```python
numbers = list()
```

From another iterable:

```python
numbers = list(range(5))
```

```python
letters = list("hello")
```

Result:

```python
["h", "e", "l", "l", "o"]
```

---

# 3. Indexing

List indexes start at `0`.

```python
numbers = [10, 20, 30, 40, 50]
```

```python
numbers[0]    # 10
numbers[1]    # 20
numbers[4]    # 50
```

Negative indexes start from the end:

```python
numbers[-1]   # 50
numbers[-2]   # 40
numbers[-5]   # 10
```

### Index structure

```text
[10, 20, 30, 40, 50]
  ↑   ↑           ↑
  0   1          -1
```

Trying to access an invalid index raises:

```python
IndexError
```

Example:

```python
numbers[10]
```

---

# 4. Modifying Elements

Lists are mutable.

```python
numbers = [10, 20, 30]

numbers[0] = 100
```

Result:

```python
[100, 20, 30]
```

Multiple elements can be replaced using slicing:

```python
numbers[0:2] = [100, 200]
```

---

# 5. Slicing

Syntax:

```python
list[start:stop:step]
```

`stop` is **exclusive**.

```python
numbers = [0, 1, 2, 3, 4, 5]
```

### Basic slicing

```python
numbers[1:4]
```

Result:

```python
[1, 2, 3]
```

### From beginning

```python
numbers[:3]
```

```python
[0, 1, 2]
```

### To the end

```python
numbers[3:]
```

```python
[3, 4, 5]
```

### Copy using slicing

```python
copy = numbers[:]
```

### Step

```python
numbers[::2]
```

```python
[0, 2, 4]
```

### Reverse

```python
numbers[::-1]
```

```python
[5, 4, 3, 2, 1, 0]
```

### Negative step

```python
numbers[4:1:-1]
```

```python
[4, 3, 2]
```

---

# 6. Adding Elements

## `append()`

Adds **one element** to the end.

```python
numbers = [1, 2, 3]

numbers.append(4)
```

Result:

```python
[1, 2, 3, 4]
```

If you append another list:

```python
numbers.append([5, 6])
```

Result:

```python
[1, 2, 3, 4, [5, 6]]
```

The list `[5, 6]` is treated as **one element**.

---

## `extend()`

Adds each element from another iterable.

```python
numbers = [1, 2, 3]

numbers.extend([4, 5])
```

Result:

```python
[1, 2, 3, 4, 5]
```

### `append()` vs `extend()`

```python
numbers.append([4, 5])
```

```text
[1, 2, 3, [4, 5]]
```

```python
numbers.extend([4, 5])
```

```text
[1, 2, 3, 4, 5]
```

---

## `insert()`

Insert an element at a specific index.

```python
numbers = [1, 2, 3]

numbers.insert(1, 99)
```

Result:

```python
[1, 99, 2, 3]
```

Syntax:

```python
list.insert(index, value)
```

---

# 7. Removing Elements

## `remove()`

Removes the **first matching value**.

```python
numbers = [10, 20, 30, 20]

numbers.remove(20)
```

Result:

```python
[10, 30, 20]
```

If the value doesn't exist:

```python
ValueError
```

---

## `pop()`

Removes and **returns** an element.

```python
numbers = [10, 20, 30]

value = numbers.pop()
```

Result:

```python
value == 30
numbers == [10, 20]
```

Remove by index:

```python
value = numbers.pop(0)
```

---

## `del`

Remove by index:

```python
del numbers[0]
```

Remove a slice:

```python
del numbers[1:3]
```

Delete the entire list variable:

```python
del numbers
```

---

## `clear()`

Removes all elements:

```python
numbers.clear()
```

Result:

```python
[]
```

### Removing methods comparison

| Method     | Removes by  | Returns removed value? |
| ---------- | ----------- | ---------------------- |
| `remove()` | value       | No                     |
| `pop()`    | index       | Yes                    |
| `del`      | index/slice | No                     |
| `clear()`  | everything  | No                     |

---

# 8. Searching and Membership

## `in`

```python
numbers = [10, 20, 30]

20 in numbers
```

```python
True
```

```python
50 in numbers
```

```python
False
```

Negation:

```python
50 not in numbers
```

---

## `index()`

Returns the index of the first matching element.

```python
numbers = [10, 20, 30, 20]

numbers.index(20)
```

Result:

```python
1
```

If the value doesn't exist:

```python
ValueError
```

Can specify a starting position:

```python
numbers.index(20, 2)
```

---

## `count()`

Counts occurrences:

```python
numbers = [10, 20, 20, 30, 20]

numbers.count(20)
```

Result:

```python
3
```

---

# 9. Length

```python
numbers = [10, 20, 30]

len(numbers)
```

Result:

```python
3
```

Common pattern:

```python
if len(numbers) > 0:
    ...
```

Usually this can be simplified to:

```python
if numbers:
    ...
```

---

# 10. Iterating Over Lists

Basic loop:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

With index:

```python
for index in range(len(numbers)):
    print(index, numbers[index])
```

Prefer `enumerate()` when you need both:

```python
for index, number in enumerate(numbers):
    print(index, number)
```

Starting from `1`:

```python
for index, number in enumerate(numbers, start=1):
    print(index, number)
```

---

# 11. Modifying a List in a Loop

This is generally safe when modifying elements by index:

```python
numbers = [1, 2, 3]

for i in range(len(numbers)):
    numbers[i] *= 2
```

Result:

```python
[2, 4, 6]
```

But modifying the **size** of a list while iterating over it is dangerous.

Avoid:

```python
for number in numbers:
    if number < 0:
        numbers.remove(number)
```

Prefer:

```python
numbers = [
    number
    for number in numbers
    if number >= 0
]
```

---

# 12. List Concatenation

Lists can be combined using `+`.

```python
a = [1, 2]
b = [3, 4]

result = a + b
```

Result:

```python
[1, 2, 3, 4]
```

This creates a **new list**.

---

# 13. Repeating Lists

```python
numbers = [1, 2]

numbers * 3
```

Result:

```python
[1, 2, 1, 2, 1, 2]
```

Be careful with nested lists:

```python
matrix = [[0] * 3] * 3
```

This does **not** create three independent inner lists.

Changing one row can affect all rows.

Prefer:

```python
matrix = [[0] * 3 for _ in range(3)]
```

---

# 14. Sorting

## `sort()`

Modifies the original list.

```python
numbers = [5, 2, 8, 1]

numbers.sort()
```

Result:

```python
[1, 2, 5, 8]
```

Descending:

```python
numbers.sort(reverse=True)
```

---

## `sorted()`

Returns a new sorted list.

```python
numbers = [5, 2, 8, 1]

result = sorted(numbers)
```

Original:

```python
[5, 2, 8, 1]
```

Result:

```python
[1, 2, 5, 8]
```

### Important

```python
numbers.sort()
```

returns:

```python
None
```

Don't do:

```python
numbers = numbers.sort()
```

because `numbers` will become `None`.

---

# 15. Sorting with `key`

Useful for lists containing dictionaries.

```python
employees = [
    {"name": "Ivan", "salary": 3200},
    {"name": "Maria", "salary": 2800},
    {"name": "Georgi", "salary": 3500}
]
```

Sort by salary:

```python
employees.sort(
    key=lambda employee: employee["salary"]
)
```

Descending:

```python
employees.sort(
    key=lambda employee: employee["salary"],
    reverse=True
)
```

Or create a new list:

```python
sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"]
)
```

---

# 16. Reversing

## `reverse()`

Modifies the original list:

```python
numbers.reverse()
```

## `reversed()`

Returns an iterator:

```python
reversed_numbers = list(reversed(numbers))
```

## Slicing

Another option:

```python
reversed_numbers = numbers[::-1]
```

---

# 17. Copying Lists

This is extremely important.

```python
a = [1, 2, 3]
b = a
```

`b` is **not a copy**.

Both variables refer to the same list.

```python
b.append(4)

print(a)
```

Result:

```python
[1, 2, 3, 4]
```

---

## Shallow Copy

```python
b = a.copy()
```

or:

```python
b = a[:]
```

or:

```python
b = list(a)
```

For a flat list, these give an independent list.

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

# a -> [1, 2, 3]
# b -> [1, 2, 3, 4]
```

---

# 18. Nested Lists and Shallow Copy

Consider:

```python
a = [
    [1, 2],
    [3, 4]
]

b = a.copy()
```

The outer list is copied, but the inner lists are still shared.

```python
b[0].append(99)
```

Now:

```python
a
```

also contains:

```python
[1, 2, 99]
```

For a true deep copy:

```python
import copy

b = copy.deepcopy(a)
```

---

# 19. List Comprehensions

A list comprehension creates a new list.

Basic:

```python
numbers = [1, 2, 3, 4]

squares = [
    number ** 2
    for number in numbers
]
```

Equivalent loop:

```python
squares = []

for number in numbers:
    squares.append(number ** 2)
```

---

## Filtering

```python
even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]
```

---

## Filtering + transformation

```python
result = [
    number * 2
    for number in numbers
    if number > 2
]
```

---

## Conditional expression

```python
labels = [
    "even" if number % 2 == 0 else "odd"
    for number in numbers
]
```

---

## Nested comprehension

Possible, but readability can suffer:

```python
matrix = [
    [1, 2],
    [3, 4]
]

flattened = [
    number
    for row in matrix
    for number in row
]
```

Result:

```python
[1, 2, 3, 4]
```

Don't use complex comprehensions just because you can.

---

# 20. Lists of Dictionaries

Extremely common in Data work.

```python
employees = [
    {"name": "Ivan", "salary": 3200},
    {"name": "Maria", "salary": 2800},
    {"name": "Georgi", "salary": 3500}
]
```

Extract names:

```python
names = [
    employee["name"]
    for employee in employees
]
```

Filter employees:

```python
high_paid = [
    employee
    for employee in employees
    if employee["salary"] > 3000
]
```

Extract names of high-paid employees:

```python
names = [
    employee["name"]
    for employee in employees
    if employee["salary"] > 3000
]
```

---

# 21. Lists of Lists

Example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Access row:

```python
matrix[0]
```

Access individual value:

```python
matrix[1][2]
```

Result:

```python
6
```

Iterate:

```python
for row in matrix:
    for value in row:
        print(value)
```

---

# 22. Flattening a Nested List

Given:

```python
nested = [
    [1, 2],
    [3, 4],
    [5, 6]
]
```

Using loops:

```python
flat = []

for row in nested:
    for value in row:
        flat.append(value)
```

Using comprehension:

```python
flat = [
    value
    for row in nested
    for value in row
]
```

Result:

```python
[1, 2, 3, 4, 5, 6]
```

---

# 23. Useful Built-in Functions

## `sum()`

```python
numbers = [10, 20, 30]

sum(numbers)
```

Result:

```python
60
```

## `min()`

```python
min(numbers)
```

## `max()`

```python
max(numbers)
```

## `len()`

```python
len(numbers)
```

## `sorted()`

```python
sorted(numbers)
```

## `any()`

Returns `True` if at least one element is truthy:

```python
numbers = [1, 3, 5, 8]

any(number % 2 == 0 for number in numbers)
```

## `all()`

Returns `True` if every element is truthy:

```python
all(number > 0 for number in numbers)
```

---

# 24. `map()`

`map()` applies a function to every element.

```python
numbers = [1, 2, 3]

result = list(
    map(lambda x: x * 2, numbers)
)
```

Result:

```python
[2, 4, 6]
```

Often a comprehension is more readable:

```python
result = [x * 2 for x in numbers]
```

---

# 25. `filter()`

`filter()` keeps elements satisfying a condition.

```python
numbers = [1, 2, 3, 4, 5]

result = list(
    filter(lambda x: x % 2 == 0, numbers)
)
```

Result:

```python
[2, 4]
```

Equivalent comprehension:

```python
result = [
    x
    for x in numbers
    if x % 2 == 0
]
```

---

# 26. `zip()`

Combines multiple iterables.

```python
names = ["Ivan", "Maria", "Georgi"]
salaries = [3200, 2800, 3500]

for name, salary in zip(names, salaries):
    print(name, salary)
```

Create a list of pairs:

```python
pairs = list(zip(names, salaries))
```

Result:

```python
[
    ("Ivan", 3200),
    ("Maria", 2800),
    ("Georgi", 3500)
]
```

---

# 27. `enumerate()`

Useful when you need the index and value.

```python
names = ["Ivan", "Maria", "Georgi"]

for index, name in enumerate(names):
    print(index, name)
```

Result:

```text
0 Ivan
1 Maria
2 Georgi
```

Start from `1`:

```python
for index, name in enumerate(names, start=1):
    print(index, name)
```

---

# 28. Unpacking Lists

```python
numbers = [10, 20, 30]

a, b, c = numbers
```

Now:

```python
a == 10
b == 20
c == 30
```

Extended unpacking:

```python
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers
```

Result:

```python
first  # 1
middle # [2, 3, 4]
last   # 5
```

---

# 29. List as a Stack

Lists can be used as stacks.

Push:

```python
stack.append(value)
```

Pop:

```python
value = stack.pop()
```

This follows:

```text
LIFO
Last In, First Out
```

Example:

```python
stack = []

stack.append("A")
stack.append("B")
stack.append("C")

stack.pop()  # C
stack.pop()  # B
```

---

# 30. List as a Queue — Important Caveat

You technically can use:

```python
queue.append(value)
queue.pop(0)
```

but this is inefficient for large queues because removing the first element requires shifting the remaining elements.

For a proper queue, Python provides:

```python
from collections import deque
```

Then:

```python
queue = deque()

queue.append("A")
queue.append("B")

queue.popleft()
```

For Core Python fundamentals, understand the distinction; `deque` can be learned later.

---

# 31. Truthiness of Lists

Empty list:

```python
[]
```

is falsy.

Therefore:

```python
if not numbers:
    print("List is empty")
```

Instead of:

```python
if len(numbers) == 0:
    ...
```

Non-empty list:

```python
if numbers:
    print("List contains elements")
```

---

# 32. `None` vs Empty List

These are different:

```python
items = None
```

means:

> There is no list/value.

While:

```python
items = []
```

means:

> There is a list, but it contains zero elements.

Check separately:

```python
if items is None:
    ...
```

```python
if not items:
    ...
```

Be aware that `not items` is `True` for both `None` and `[]`.

---

# 33. Common List Patterns

## Filter

```python
result = [
    item
    for item in items
    if condition(item)
]
```

## Transform

```python
result = [
    transform(item)
    for item in items
]
```

## Filter + transform

```python
result = [
    transform(item)
    for item in items
    if condition(item)
]
```

## Find first matching item

```python
result = None

for item in items:
    if condition(item):
        result = item
        break
```

## Count manually

```python
count = 0

for item in items:
    if condition(item):
        count += 1
```

## Aggregate manually

```python
total = 0

for item in items:
    total += item
```

---

# 34. Common List Pitfalls

## Assignment is not copying

```python
a = [1, 2, 3]
b = a
```

`a` and `b` refer to the same list.

---

## `sort()` returns `None`

Wrong:

```python
numbers = numbers.sort()
```

Correct:

```python
numbers.sort()
```

or:

```python
numbers = sorted(numbers)
```

---

## `append()` adds one object

```python
items.append([1, 2])
```

does not add `1` and `2` separately.

---

## Modifying while iterating

Avoid changing the list's size during iteration.

Prefer filtering into a new list.

---

## Nested list multiplication

Avoid:

```python
matrix = [[0] * 3] * 3
```

Prefer:

```python
matrix = [[0] * 3 for _ in range(3)]
```

---

# 35. List Complexity — Basic Understanding

You don't need to memorize Big-O deeply yet, but these differences are useful.

| Operation          | Typical complexity |
| ------------------ | -----------------: |
| `list[index]`      |               O(1) |
| `append()`         |     O(1) amortized |
| `pop()` from end   |               O(1) |
| `insert(0, value)` |               O(n) |
| `pop(0)`           |               O(n) |
| `remove(value)`    |               O(n) |
| `value in list`    |               O(n) |
| `index(value)`     |               O(n) |
| `count(value)`     |               O(n) |
| `sort()`           |         O(n log n) |

This explains why lists are excellent for ordered data, but not always the best structure for membership lookups or queues.

---

# 36. List vs Other Collections

| Structure | Ordered | Mutable | Duplicates | Main use                   |
| --------- | ------- | ------- | ---------- | -------------------------- |
| `list`    | Yes     | Yes     | Yes        | Ordered collection         |
| `tuple`   | Yes     | No      | Yes        | Fixed collection           |
| `set`     | No*     | Yes     | No         | Unique values / membership |
| `dict`    | Yes**   | Yes     | Keys: No   | Key-value data             |

* Sets do not provide sequence-style indexing.

** Dictionaries preserve insertion order in modern Python.

---

# 37. Data Processing Example

Given:

```python
transactions = [
    {"user": "Ivan", "amount": 120},
    {"user": "Maria", "amount": 80},
    {"user": "Ivan", "amount": 200},
    {"user": "Georgi", "amount": 50},
    {"user": "Maria", "amount": 150}
]
```

Filter:

```python
large_transactions = [
    transaction
    for transaction in transactions
    if transaction["amount"] > 100
]
```

Extract users:

```python
users = [
    transaction["user"]
    for transaction in large_transactions
]
```

Extract amounts:

```python
amounts = [
    transaction["amount"]
    for transaction in large_transactions
]
```

Calculate total:

```python
total = sum(amounts)
```

Sort by amount:

```python
sorted_transactions = sorted(
    transactions,
    key=lambda transaction: transaction["amount"],
    reverse=True
)
```

This pattern is extremely close to the type of transformations you'll later perform with Pandas.

---

# 38. What You Should Know Before Moving On

### Fundamentals

* [ ] Create lists
* [ ] Indexing
* [ ] Negative indexing
* [ ] Slicing
* [ ] Modify elements
* [ ] `append()`
* [ ] `extend()`
* [ ] `insert()`
* [ ] `remove()`
* [ ] `pop()`
* [ ] `del`
* [ ] `clear()`
* [ ] `len()`
* [ ] `in`
* [ ] `index()`
* [ ] `count()`

### Iteration

* [ ] `for`
* [ ] `enumerate()`
* [ ] `range()`
* [ ] nested loops

### Transformation

* [ ] list comprehensions
* [ ] filtering
* [ ] transformation
* [ ] filtering + transformation
* [ ] `map()`
* [ ] `filter()`

### Organization

* [ ] `sort()`
* [ ] `sorted()`
* [ ] `reverse()`
* [ ] `reversed()`
* [ ] `key=`
* [ ] `lambda`

### Data structures

* [ ] lists of dictionaries
* [ ] lists of lists
* [ ] nested structures
* [ ] unpacking
* [ ] `zip()`

### Python behavior

* [ ] mutability
* [ ] references
* [ ] shallow copy
* [ ] nested-list references
* [ ] truthiness
* [ ] common list pitfalls

### Data mindset

You should be able to look at a list of records and comfortably perform:

```text
LIST
 ↓
filter
 ↓
transform
 ↓
extract
 ↓
aggregate
 ↓
sort
```

without needing an external library.
