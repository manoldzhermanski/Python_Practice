# Python Sets

A `set` is an unordered, mutable collection of unique elements.

Sets are useful when working with unique values, membership checks,
and operations between collections.

## Creating a Set

~~~~python
numbers = {1, 2, 3, 4}
~~~~

An empty set must be created using `set()`:

~~~~python
numbers = set()
~~~~

Using `{}` creates an empty dictionary, not a set.

## Main Characteristics

- Contains only unique elements
- Unordered
- Mutable
- Elements must be hashable
- Does not support indexing

~~~~python
values = {1, 2, 2, 3}

print(values)
# {1, 2, 3}
~~~~

## Membership

Sets are useful for checking whether a value exists:

~~~~python
"IT" in departments
~~~~

~~~~python
"Finance" not in departments
~~~~

## Set Operations

Given:

~~~~python
a = {"IT", "HR", "Sales"}
b = {"IT", "HR", "Finance"}
~~~~

### Union

All unique elements from both sets:

~~~~python
a | b
~~~~

or:

~~~~python
a.union(b)
~~~~

Result:

~~~~text
{"IT", "HR", "Sales", "Finance"}
~~~~

### Intersection

Elements present in both sets:

~~~~python
a & b
~~~~

or:

~~~~python
a.intersection(b)
~~~~

Result:

~~~~text
{"IT", "HR"}
~~~~

### Difference

Elements present in `a` but not in `b`:

~~~~python
a - b
~~~~

or:

~~~~python
a.difference(b)
~~~~

Result:

~~~~text
{"Sales"}
~~~~

Note that:

~~~~python
b - a
~~~~

is different:

~~~~text
{"Finance"}
~~~~

### Symmetric Difference

Elements present in either set, but not both:

~~~~python
a ^ b
~~~~

or:

~~~~python
a.symmetric_difference(b)
~~~~

Result:

~~~~text
{"Sales", "Finance"}
~~~~

## Modifying Sets

### Add an Element

~~~~python
departments.add("Finance")
~~~~

### Remove an Element

~~~~python
departments.remove("Finance")
~~~~

`remove()` raises `KeyError` if the element does not exist.

### Remove Safely

~~~~python
departments.discard("Finance")
~~~~

`discard()` does nothing if the element does not exist.

### Add Multiple Elements

~~~~python
departments.update({"Finance", "Marketing"})
~~~~

## Set Comprehension

Sets can be created using comprehensions:

~~~~python
unique_departments = {
    employee["department"]
    for employee in employees
}
~~~~

This is useful when extracting unique values from a collection.

## When to Use Sets

Use a set when you need:

- Unique values
- Fast membership checks
- Union, intersection, and difference operations
- Duplicate removal
- Comparison between collections

Example:

~~~~python
departments = {
    employee["department"]
    for employee in employees
}
~~~~

## Important

A set:

- Does not preserve duplicates
- Does not support indexing
- Does not guarantee element order
- Can contain only hashable elements

For example:

~~~~python
employees = {["Ivan", 4200]}  # TypeError
~~~~

Lists and dictionaries cannot be elements of a set because they are mutable
and therefore unhashable.
