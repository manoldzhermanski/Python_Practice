# Python Tuples — Cheatsheet

## 1. What is a Tuple?

A `tuple` is an **ordered, immutable collection** that can contain multiple values.

```python
numbers = (10, 20, 30, 40)
```

Tuples can contain different data types:

```python
data = (10, "Ivan", 3.14, True, None)
```

Tuples can contain other collections:

```python
data = (
    [1, 2, 3],
    {"name": "Ivan", "age": 25}
)
```

### Main characteristics

| Property           | Tuple |
| ------------------ | ----- |
| Ordered            | Yes   |
| Mutable            | No    |
| Allows duplicates  | Yes   |
| Indexed            | Yes   |
| Allows mixed types | Yes   |
| Supports slicing   | Yes   |
| Hashable           | Sometimes* |

\* A tuple is hashable only if all of its elements are hashable.

---

# 2. Creating Tuples

## Empty tuple

```python
empty = ()
```

or:

```python
empty = tuple()
```

---

## Tuple with values

```python
numbers = (1, 2, 3, 4, 5)
```

---

## Single-element tuple

This is an important special case.

```python
numbers = (10,)
```

The comma is what makes it a tuple.

This:

```python
numbers = (10)
```

is simply:

```python
10
```

---

## Parentheses are optional

Python can create tuples without explicit parentheses:

```python
numbers = 1, 2, 3
```

This is equivalent to:

```python
numbers = (1, 2, 3)
```

The **comma** is what creates the tuple.

---

# 3. Creating Tuples with `tuple()`

`tuple()` can convert an iterable into a tuple.

From a list:

```python
numbers = tuple([1, 2, 3])
```

Result:

```python
(1, 2, 3)
```

From a string:

```python
letters = tuple("hello")
```

Result:

```python
("h", "e", "l", "l", "o")
```

From a range:

```python
numbers = tuple(range(5))
```

Result:

```python
(0, 1, 2, 3, 4)
```

From a set:

```python
numbers = tuple({1, 2, 3})
```

The resulting order should not be relied upon because sets are unordered collections.

---

# 4. Indexing

Tuple indexes start at `0`.

```python
numbers = (10, 20, 30, 40, 50)
```

```python
numbers[0]    # 10
numbers[1]    # 20
numbers[4]    # 50
```

Negative indexes work from the end:

```python
numbers[-1]   # 50
numbers[-2]   # 40
numbers[-5]   # 10
```

### Index structure

```text
(10, 20, 30, 40, 50)
 ↑   ↑           ↑
 0   1          -1
```

Invalid indexes raise:

```python
IndexError
```

Example:

```python
numbers[10]
```

---

# 5. Immutability

The most important characteristic of a tuple is that it is **immutable**.

Once a tuple is created, its elements cannot be changed.

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

This raises:

```python
TypeError
```

You cannot use:

```python
numbers.append(40)
```

because tuples do not have `append()`.

You cannot use:

```python
numbers.remove(20)
```

because tuples do not have `remove()`.

---

# 6. What Does Immutable Mean?

Consider:

```python
numbers = (10, 20, 30)
```

You cannot modify an individual element:

```python
numbers[0] = 100
```

However, you can create a **new tuple**:

```python
numbers = (100, 20, 30)
```

You did not modify the original tuple.

You replaced the variable with a reference to a new tuple.

---

# 7. Tuple Slicing

Tuples support slicing just like lists.

Syntax:

```python
tuple[start:stop:step]
```

`stop` is exclusive.

```python
numbers = (0, 1, 2, 3, 4, 5)
```

## Basic slicing

```python
numbers[1:4]
```

Result:

```python
(1, 2, 3)
```

## From beginning

```python
numbers[:3]
```

Result:

```python
(0, 1, 2)
```

## To the end

```python
numbers[3:]
```

Result:

```python
(3, 4, 5)
```

## Copy using slicing

```python
copy = numbers[:]
```

## Step

```python
numbers[::2]
```

Result:

```python
(0, 2, 4)
```

## Reverse

```python
numbers[::-1]
```

Result:

```python
(5, 4, 3, 2, 1, 0)
```

---

# 8. Tuple Concatenation

Tuples can be combined using `+`.

```python
a = (1, 2)
b = (3, 4)

result = a + b
```

Result:

```python
(1, 2, 3, 4)
```

This creates a **new tuple**.

The original tuples are not modified.

---

# 9. Repeating Tuples

You can repeat a tuple using `*`.

```python
numbers = (1, 2)

result = numbers * 3
```

Result:

```python
(1, 2, 1, 2, 1, 2)
```

---

# 10. Membership

Use `in` to check whether an element exists.

```python
numbers = (10, 20, 30)
```

```python
20 in numbers
```

Result:

```python
True
```

```python
50 in numbers
```

Result:

```python
False
```

Negation:

```python
50 not in numbers
```

Result:

```python
True
```

---

# 11. Length

Use `len()`:

```python
numbers = (10, 20, 30)

len(numbers)
```

Result:

```python
3
```

---

# 12. Iterating Over Tuples

Basic loop:

```python
numbers = (10, 20, 30)

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

# 13. Tuple Methods

Tuples have only two main methods:

```python
count()
index()
```

This is because tuples are immutable and therefore do not need methods such as:

```text
append()
remove()
insert()
pop()
sort()
reverse()
clear()
```

---

# 14. `count()`

`count()` returns how many times a value occurs.

```python
numbers = (10, 20, 20, 30, 20)

numbers.count(20)
```

Result:

```python
3
```

If the value does not exist:

```python
numbers.count(99)
```

Result:

```python
0
```

---

# 15. `index()`

`index()` returns the index of the first matching value.

```python
numbers = (10, 20, 30, 20)

numbers.index(20)
```

Result:

```python
1
```

It returns the first occurrence.

You can specify a starting position:

```python
numbers.index(20, 2)
```

Result:

```python
3
```

If the value does not exist:

```python
numbers.index(99)
```

raises:

```python
ValueError
```

---

# 16. Tuple Unpacking

Tuple unpacking is one of the most important tuple features.

Given:

```python
employee = ("Ivan", 25, "IT")
```

You can unpack it:

```python
name, age, department = employee
```

Now:

```python
name
# "Ivan"

age
# 25

department
# "IT"
```

The number of variables must normally match the number of elements.

---

# 17. Extended Unpacking

You can use `*` to collect multiple elements.

```python
numbers = (1, 2, 3, 4, 5)

first, *middle, last = numbers
```

Result:

```python
first
# 1

middle
# [2, 3, 4]

last
# 5
```

Notice that `middle` is a **list**, not a tuple.

Another example:

```python
numbers = (1, 2, 3, 4, 5)

first, *rest = numbers
```

Result:

```python
first
# 1

rest
# [2, 3, 4, 5]
```

---

# 18. Swapping Variables

Tuples make variable swapping very easy.

Instead of:

```python
temp = a
a = b
b = temp
```

Python allows:

```python
a, b = b, a
```

Example:

```python
a = 10
b = 20

a, b = b, a
```

Now:

```python
a == 20
b == 10
```

This works because Python creates and unpacks a tuple behind the scenes.

---

# 19. Returning Multiple Values from Functions

A function can return multiple values:

```python
def get_employee():
    return "Ivan", 25, "IT"
```

The function is effectively returning a tuple.

```python
employee = get_employee()
```

Now:

```python
employee
```

is:

```python
("Ivan", 25, "IT")
```

You can unpack immediately:

```python
name, age, department = get_employee()
```

---

# 20. Tuples and Functions

Tuples are commonly used when a function needs to return several related values.

```python
def calculate_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)
```

Then:

```python
minimum, maximum, total = calculate_stats(
    [10, 20, 30]
)
```

---

# 21. Tuples in `for` Loops

Tuples are extremely common when iterating over dictionaries.

```python
employee = {
    "name": "Ivan",
    "salary": 3200
}
```

Using `.items()`:

```python
for key, value in employee.items():
    print(key, value)
```

Each iteration produces a key/value pair:

```python
("name", "Ivan")
("salary", 3200)
```

This is one reason understanding tuple unpacking is important.

---

# 22. `zip()` Produces Tuples

Given:

```python
names = ["Ivan", "Maria", "Georgi"]
salaries = [3200, 2800, 3500]
```

Using:

```python
result = zip(names, salaries)
```

and converting to a list:

```python
result = list(zip(names, salaries))
```

produces:

```python
[
    ("Ivan", 3200),
    ("Maria", 2800),
    ("Georgi", 3500)
]
```

Each pair is a tuple.

You can unpack them:

```python
for name, salary in zip(names, salaries):
    print(name, salary)
```

---

# 23. Tuples and Lists

Lists and tuples are very similar.

Both:

- are ordered
- support indexing
- support slicing
- allow duplicates
- allow mixed data types
- can be iterated over
- support `len()`
- support `in`
- support `count()`
- support `index()`

The major difference:

```text
list  -> mutable
tuple -> immutable
```

---

# 24. List vs Tuple

| Feature               | List | Tuple |
| --------------------- | ---- | ----- |
| Ordered               | Yes  | Yes   |
| Mutable               | Yes  | No    |
| Allows duplicates     | Yes  | Yes   |
| Indexed               | Yes  | Yes   |
| Slicing               | Yes  | Yes   |
| `append()`            | Yes  | No    |
| `remove()`            | Yes  | No    |
| `pop()`               | Yes  | No    |
| `sort()`              | Yes  | No    |
| `reverse()`            | Yes  | No    |
| `count()`              | Yes  | Yes   |
| `index()`              | Yes  | Yes   |
| Can be dictionary key  | No   | Sometimes |

---

# 25. When Should You Use a Tuple?

Use a tuple when the collection represents a group of values that should **not be modified**.

For example:

```python
coordinates = (42.6977, 23.3219)
```

The coordinates represent one fixed pair of values.

Another example:

```python
employee = ("Ivan", 25, "IT")
```

If the structure is meant to be fixed, a tuple can make that intention clear.

---

# 26. When Should You Use a List?

Use a list when the collection is expected to change.

For example:

```python
employees = [
    "Ivan",
    "Maria",
    "Georgi"
]
```

You may later:

```python
employees.append("Elena")
```

Therefore a list is appropriate.

---

# 27. Tuples as Dictionary Keys

Dictionary keys must be hashable.

A tuple can be used as a dictionary key if all its elements are hashable.

Example:

```python
locations = {
    (42.6977, 23.3219): "Sofia",
    (42.1354, 24.7453): "Plovdiv"
}
```

Access:

```python
locations[(42.6977, 23.3219)]
```

Result:

```python
"Sofia"
```

---

# 28. Why Can't Lists Usually Be Dictionary Keys?

This does not work:

```python
data = {
    [1, 2]: "value"
}
```

because lists are mutable and therefore unhashable.

This works:

```python
data = {
    (1, 2): "value"
}
```

because a tuple containing only hashable elements is hashable.

---

# 29. Hashability

A tuple is not automatically hashable.

This is hashable:

```python
a = (1, 2, 3)
```

This is not:

```python
a = ([1, 2], 3)
```

because the tuple contains a list.

Trying:

```python
data = {
    a: "value"
}
```

would raise:

```python
TypeError: unhashable type: 'list'
```

Rule:

> A tuple is hashable only when all of its elements are hashable.

---

# 30. Nested Tuples

Tuples can contain other tuples.

```python
data = (
    (1, 2),
    (3, 4),
    (5, 6)
)
```

Access:

```python
data[0]
```

Result:

```python
(1, 2)
```

Access nested value:

```python
data[0][1]
```

Result:

```python
2
```

---

# 31. Tuple Containing a Mutable Object

Immutable does not mean that everything inside a tuple is necessarily immutable.

Consider:

```python
data = (
    [1, 2, 3],
    "hello"
)
```

You cannot replace the list:

```python
data[0] = [4, 5, 6]
```

But you can modify the list itself:

```python
data[0].append(4)
```

Now:

```python
data
```

is:

```python
(
    [1, 2, 3, 4],
    "hello"
)
```

The tuple itself was not changed structurally.

The object stored inside it was mutated.

---

# 32. Converting Tuple to List

Use `list()`:

```python
numbers = (1, 2, 3)

numbers_list = list(numbers)
```

Result:

```python
[1, 2, 3]
```

This is useful when you need to modify the data.

Example:

```python
numbers = (1, 2, 3)

numbers = list(numbers)
numbers.append(4)
numbers = tuple(numbers)
```

Now:

```python
(1, 2, 3, 4)
```

---

# 33. Converting List to Tuple

Use `tuple()`:

```python
numbers = [1, 2, 3]

numbers_tuple = tuple(numbers)
```

Result:

```python
(1, 2, 3)
```

This is useful when you want to represent the data as an immutable collection.

---

# 34. Sorting Tuples

Tuples do not have a `.sort()` method because they are immutable.

However, you can use `sorted()`:

```python
numbers = (5, 2, 8, 1)

result = sorted(numbers)
```

Result:

```python
[1, 2, 5, 8]
```

Notice:

> `sorted()` returns a **list**, not a tuple.

If you specifically need a tuple:

```python
result = tuple(sorted(numbers))
```

Result:

```python
(1, 2, 5, 8)
```

---

# 35. Sorting Tuples with `key`

Consider:

```python
employees = (
    ("Ivan", 3200),
    ("Maria", 2800),
    ("Georgi", 3500)
)
```

Sort by salary:

```python
sorted_employees = sorted(
    employees,
    key=lambda employee: employee[1]
)
```

Result:

```python
[
    ("Maria", 2800),
    ("Ivan", 3200),
    ("Georgi", 3500)
]
```

Descending:

```python
sorted_employees = sorted(
    employees,
    key=lambda employee: employee[1],
    reverse=True
)
```

---

# 36. Tuple Comparison

Tuples can be compared.

Python compares elements from left to right.

```python
(1, 2) < (1, 3)
```

Result:

```python
True
```

Because:

```text
1 == 1
```

so Python compares:

```text
2 < 3
```

Another example:

```python
(2, 1) > (1, 100)
```

Result:

```python
True
```

The first elements already determine the result.

---

# 37. Tuple Equality

Tuples are equal when they contain the same values in the same order.

```python
(1, 2, 3) == (1, 2, 3)
```

Result:

```python
True
```

But:

```python
(1, 2, 3) == (3, 2, 1)
```

Result:

```python
False
```

Order matters.

---

# 38. Tuple Truthiness

An empty tuple is falsy:

```python
()
```

Therefore:

```python
if not values:
    print("Tuple is empty")
```

A non-empty tuple is truthy:

```python
if values:
    print("Tuple contains elements")
```

This works similarly to lists.

---

# 39. `None` vs Empty Tuple

These are different:

```python
values = None
```

means:

> There is no value.

While:

```python
values = ()
```

means:

> There is a tuple containing zero elements.

Check explicitly:

```python
if values is None:
    ...
```

Check whether it is empty:

```python
if not values:
    ...
```

Be aware that:

```python
not None
```

and:

```python
not ()
```

are both `True`.

---

# 40. Tuple Comprehensions — Important

Python does **not** have tuple comprehensions.

This:

```python
numbers = (x ** 2 for x in range(5))
```

is **not** a tuple comprehension.

It creates a **generator expression**.

To create a tuple:

```python
numbers = tuple(
    x ** 2
    for x in range(5)
)
```

Result:

```python
(0, 1, 4, 9, 16)
```

---

# 41. Generator Expression vs Tuple

This:

```python
result = (x * 2 for x in numbers)
```

creates a generator.

You can convert it:

```python
result = tuple(
    x * 2
    for x in numbers
)
```

The important distinction is:

```text
(x * 2 for x in numbers)      -> generator
tuple(x * 2 for x in numbers) -> tuple
```

---

# 42. Tuple Packing

Python automatically packs multiple values into a tuple.

```python
employee = "Ivan", 25, "IT"
```

This creates:

```python
("Ivan", 25, "IT")
```

You can also explicitly write:

```python
employee = ("Ivan", 25, "IT")
```

---

# 43. Tuple Unpacking in Loops

Very common:

```python
employees = [
    ("Ivan", 3200),
    ("Maria", 2800),
    ("Georgi", 3500)
]
```

Instead of:

```python
for employee in employees:
    print(employee[0], employee[1])
```

you can write:

```python
for name, salary in employees:
    print(name, salary)
```

This is cleaner and more readable.

---

# 44. Nested Tuple Unpacking

Given:

```python
employees = [
    ("Ivan", ("IT", 3200)),
    ("Maria", ("HR", 2800))
]
```

You can unpack:

```python
for name, (department, salary) in employees:
    print(name, department, salary)
```

---

# 45. Common Built-in Functions

Tuples work with many built-in functions.

## `len()`

```python
numbers = (10, 20, 30)

len(numbers)
```

---

## `min()`

```python
min(numbers)
```

---

## `max()`

```python
max(numbers)
```

---

## `sum()`

```python
sum(numbers)
```

---

## `sorted()`

```python
sorted(numbers)
```

Returns a list.

---

## `any()`

```python
numbers = (1, 3, 5, 8)

any(number % 2 == 0 for number in numbers)
```

Result:

```python
True
```

---

## `all()`

```python
all(number > 0 for number in numbers)
```

Result:

```python
True
```

---

# 46. `in` with Tuples

Membership checking is straightforward:

```python
departments = ("IT", "HR", "Finance")

if "IT" in departments:
    print("IT department exists")
```

---

# 47. Tuples and `*`

The `*` operator can be used for unpacking.

Given:

```python
numbers = (1, 2, 3)
```

You can unpack into a function:

```python
print(*numbers)
```

Output:

```text
1 2 3
```

Another example:

```python
def add(a, b, c):
    return a + b + c

numbers = (10, 20, 30)

result = add(*numbers)
```

Result:

```python
60
```

---

# 48. Tuples and `**`

Tuples themselves are not used with `**`.

`**` is used for unpacking dictionaries into keyword arguments.

Example:

```python
def employee_info(name, age, department):
    print(name, age, department)

employee = {
    "name": "Ivan",
    "age": 25,
    "department": "IT"
}

employee_info(**employee)
```

Understanding the difference is useful:

```text
*  -> iterable unpacking
** -> dictionary / mapping unpacking
```

---

# 49. Tuple Memory and Performance

Tuples are generally smaller and can be slightly faster to iterate over than lists.

For example:

```python
numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = (1, 2, 3, 4, 5)
```

The difference is usually not something you should optimize prematurely.

The more important reason to use tuples is **semantics**:

> The data should not be modified.

Choose based primarily on meaning, not tiny performance differences.

---

# 50. Common Tuple Patterns

## Unpacking

```python
name, age, department = employee
```

## Iterate with unpacking

```python
for name, salary in employees:
    ...
```

## Return multiple values

```python
return minimum, maximum
```

## Convert list to tuple

```python
tuple(numbers)
```

## Convert tuple to list

```python
list(numbers)
```

## Sort tuple

```python
sorted(numbers)
```

## Sort and return tuple

```python
tuple(sorted(numbers))
```

## Check membership

```python
value in values
```

## Count

```python
values.count(value)
```

## Find index

```python
values.index(value)
```

---
