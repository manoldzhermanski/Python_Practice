# NumPy Cheat Sheet

> A practical NumPy reference for Data Science, Data Analysis, and Data Engineering.

---

## Table of Contents

1. [What is NumPy?](#what-is-numpy)
2. [Installation and Import](#installation-and-import)
3. [NumPy Arrays](#numpy-arrays)
4. [Array Attributes](#array-attributes)
5. [Creating Arrays](#creating-arrays)
6. [Data Types](#data-types)
7. [Indexing](#indexing)
8. [Slicing](#slicing)
9. [Boolean Indexing](#boolean-indexing)
10. [Fancy Indexing](#fancy-indexing)
11. [Changing Array Shape](#changing-array-shape)
12. [Combining and Splitting Arrays](#combining-and-splitting-arrays)
13. [Arithmetic Operations](#arithmetic-operations)
14. [Comparison Operations](#comparison-operations)
15. [Aggregation Functions](#aggregation-functions)
16. [Axis](#axis)
17. [Mathematical Functions](#mathematical-functions)
18. [Rounding](#rounding)
19. [Handling Missing Values](#handling-missing-values)
20. [Sorting](#sorting)
21. [Searching](#searching)
22. [Conditional Operations](#conditional-operations)
23. [Broadcasting](#broadcasting)
24. [Vectorization](#vectorization)
25. [Random Numbers](#random-numbers)
26. [Linear Algebra Basics](#linear-algebra-basics)
27. [Copy vs View](#copy-vs-view)
28. [Saving and Loading Arrays](#saving-and-loading-arrays)
29. [Useful Patterns](#useful-patterns)
30. [NumPy vs Python Lists](#numpy-vs-python-lists)

---

# What is NumPy?

**NumPy** stands for **Numerical Python**.

It is a Python library designed for numerical computing and provides:

* Fast multidimensional arrays
* Mathematical operations
* Statistical functions
* Linear algebra
* Random number generation
* Array manipulation
* Vectorized operations
* Broadcasting

The main object in NumPy is the:

```python
numpy.ndarray
```

Example:

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers)
```

Output:

```text
[10 20 30 40]
```

---

# Installation and Import

## Install NumPy

```bash
pip install numpy
```

## Import NumPy

The standard convention is:

```python
import numpy as np
```

Then NumPy functions can be accessed through `np`:

```python
np.array([1, 2, 3])
np.mean([1, 2, 3])
np.zeros(5)
```

---

# NumPy Arrays

The fundamental NumPy structure is the `ndarray`.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])
```

You can create arrays from Python lists:

```python
numbers = np.array([1, 2, 3, 4, 5])
```

From tuples:

```python
numbers = np.array((1, 2, 3, 4))
```

From nested lists:

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

This creates a 2-dimensional array:

```text
[[1 2 3]
 [4 5 6]]
```

---

# Dimensions

NumPy arrays can have multiple dimensions.

## 1D Array

```python
arr = np.array([1, 2, 3, 4])
```

Conceptually:

```text
[1 2 3 4]
```

---

## 2D Array

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

Conceptually:

```text
1 2 3
4 5 6
```

---

## 3D Array

```python
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
```

Think of a 3D array as multiple 2D matrices stacked together.

---

# Array Attributes

NumPy arrays have several useful attributes.

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

## `ndim`

Number of dimensions:

```python
arr.ndim
```

Output:

```text
2
```

---

## `shape`

Size of each dimension:

```python
arr.shape
```

Output:

```text
(2, 3)
```

Meaning:

```text
2 rows
3 columns
```

---

## `size`

Total number of elements:

```python
arr.size
```

Output:

```text
6
```

---

## `dtype`

Data type of the elements:

```python
arr.dtype
```

Example:

```text
int64
```

---

## `itemsize`

Number of bytes used by each element:

```python
arr.itemsize
```

---

## `nbytes`

Total memory consumed by the array elements:

```python
arr.nbytes
```

---

# Creating Arrays

NumPy provides many functions for creating arrays.

---

## `np.array()`

```python
arr = np.array([1, 2, 3, 4])
```

---

## `np.zeros()`

Create an array filled with zeros:

```python
np.zeros(5)
```

Output:

```text
[0. 0. 0. 0. 0.]
```

2D:

```python
np.zeros((2, 3))
```

Output:

```text
[[0. 0. 0.]
 [0. 0. 0.]]
```

---

## `np.ones()`

```python
np.ones(5)
```

Output:

```text
[1. 1. 1. 1. 1.]
```

2D:

```python
np.ones((2, 3))
```

---

## `np.full()`

Create an array filled with a specific value:

```python
np.full(5, 7)
```

Output:

```text
[7 7 7 7 7]
```

2D:

```python
np.full((2, 3), 7)
```

---

## `np.empty()`

Creates an array without initializing its values:

```python
np.empty(5)
```

The values are whatever happens to be present in memory.

Do not use `empty()` when you need initialized values.

---

# `np.arange()`

Similar to Python's `range()`.

```python
np.arange(5)
```

Output:

```text
[0 1 2 3 4]
```

Start and stop:

```python
np.arange(2, 10)
```

Output:

```text
[2 3 4 5 6 7 8 9]
```

Step:

```python
np.arange(0, 10, 2)
```

Output:

```text
[0 2 4 6 8]
```

---

# `np.linspace()`

Creates evenly spaced numbers between two values.

```python
np.linspace(0, 10, 5)
```

Output:

```text
[ 0.   2.5  5.   7.5 10. ]
```

The third argument specifies the number of values.

This is especially useful in mathematical and visualization tasks.

---

# Identity Matrix

```python
np.eye(3)
```

Output:

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

---

# Data Types

NumPy arrays usually contain elements of the same data type.

```python
arr = np.array([1, 2, 3])

print(arr.dtype)
```

Possible output:

```text
int64
```

---

## Common NumPy Data Types

| Type            | Description           |
| --------------- | --------------------- |
| `int8`          | 8-bit integer         |
| `int16`         | 16-bit integer        |
| `int32`         | 32-bit integer        |
| `int64`         | 64-bit integer        |
| `float32`       | 32-bit floating point |
| `float64`       | 64-bit floating point |
| `bool`          | Boolean               |
| `str` / Unicode | Strings               |

---

## Specify a dtype

```python
arr = np.array([1, 2, 3], dtype=np.float64)
```

---

## Convert dtype with `astype()`

```python
arr = np.array([1.2, 2.5, 3.8])

integers = arr.astype(int)
```

Result:

```text
[1 2 3]
```

Be careful: converting floats to integers truncates the decimal part.

---

# Indexing

NumPy indexing starts at `0`, just like Python lists.

```python
arr = np.array([10, 20, 30, 40])
```

First element:

```python
arr[0]
```

Output:

```text
10
```

Last element:

```python
arr[-1]
```

Output:

```text
40
```

---

# 2D Indexing

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

Access first row:

```python
arr[0]
```

Output:

```text
[10 20 30]
```

Access first row, first column:

```python
arr[0, 0]
```

Output:

```text
10
```

Access second row, third column:

```python
arr[1, 2]
```

Output:

```text
60
```

---

# Slicing

NumPy slicing works similarly to Python lists.

```python
arr = np.array([10, 20, 30, 40, 50])
```

First three elements:

```python
arr[:3]
```

Output:

```text
[10 20 30]
```

Elements from index 2:

```python
arr[2:]
```

Output:

```text
[30 40 50]
```

Every second element:

```python
arr[::2]
```

Output:

```text
[10 30 50]
```

Reverse:

```python
arr[::-1]
```

Output:

```text
[50 40 30 20 10]
```

---

# 2D Slicing

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

First two rows:

```python
arr[:2]
```

First two columns:

```python
arr[:, :2]
```

Output:

```text
[[1 2]
 [4 5]
 [7 8]]
```

Second column:

```python
arr[:, 1]
```

Output:

```text
[2 5 8]
```

Second row:

```python
arr[1, :]
```

Output:

```text
[4 5 6]
```

---

# Boolean Indexing

Boolean indexing is one of the most important NumPy concepts.

```python
arr = np.array([10, 20, 30, 40, 50])
```

Create a condition:

```python
arr > 25
```

Output:

```text
[False False  True  True  True]
```

Use the condition to filter:

```python
arr[arr > 25]
```

Output:

```text
[30 40 50]
```

---

## Multiple Conditions

Use `&` for AND:

```python
arr[(arr > 20) & (arr < 50)]
```

Use `|` for OR:

```python
arr[(arr < 20) | (arr > 40)]
```

Use `~` for NOT:

```python
arr[~(arr > 25)]
```

### Important

Do **not** use Python's `and` / `or` for element-wise NumPy conditions.

Wrong:

```python
arr > 20 and arr < 50
```

Correct:

```python
(arr > 20) & (arr < 50)
```

---

# Fancy Indexing

You can select specific indices using another array/list of indices.

```python
arr = np.array([10, 20, 30, 40, 50])

arr[[0, 2, 4]]
```

Output:

```text
[10 30 50]
```

---

# Changing Array Shape

## `reshape()`

```python
arr = np.arange(6)

arr.reshape(2, 3)
```

Output:

```text
[[0 1 2]
 [3 4 5]]
```

The total number of elements must remain the same.

Valid:

```python
np.arange(12).reshape(3, 4)
```

Invalid:

```python
np.arange(10).reshape(3, 4)
```

because:

```text
10 != 12
```

---

## Using `-1`

NumPy can infer one dimension:

```python
arr = np.arange(12)

arr.reshape(3, -1)
```

Result:

```text
(3, 4)
```

Or:

```python
arr.reshape(-1, 4)
```

Result:

```text
(3, 4)
```

---

# Flattening Arrays

Convert a multidimensional array into 1D.

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

Using `flatten()`:

```python
arr.flatten()
```

Output:

```text
[1 2 3 4 5 6]
```

Using `ravel()`:

```python
arr.ravel()
```

Both produce a 1D representation, but `ravel()` may return a view instead of a copy.

---

# Transpose

Transpose rows and columns:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr.T
```

Output:

```text
[[1 4]
 [2 5]
 [3 6]]
```

Equivalent:

```python
np.transpose(arr)
```

---

# Combining Arrays

## `np.concatenate()`

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.concatenate((a, b))
```

Output:

```text
[1 2 3 4 5 6]
```

---

## Concatenate 2D Arrays

```python
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])
```

Rows:

```python
np.concatenate((a, b), axis=0)
```

Columns:

```python
np.concatenate((a, b), axis=1)
```

---

# `vstack()`

Stack arrays vertically:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.vstack((a, b))
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

---

# `hstack()`

Stack arrays horizontally:

```python
np.hstack((a, b))
```

Output:

```text
[1 2 3 4 5 6]
```

---

# Splitting Arrays

## `np.split()`

```python
arr = np.arange(6)

np.split(arr, 3)
```

Produces:

```text
[0 1]
[2 3]
[4 5]
```

---

## `array_split()`

Unlike `split()`, `array_split()` can handle uneven splits.

```python
arr = np.arange(7)

np.array_split(arr, 3)
```

---

# Arithmetic Operations

NumPy supports element-wise arithmetic.

```python
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
```

Addition:

```python
a + b
```

Output:

```text
[11 22 33]
```

Subtraction:

```python
a - b
```

Multiplication:

```python
a * b
```

Division:

```python
a / b
```

Power:

```python
a ** 2
```

---

# Scalar Operations

You can perform operations against every element.

```python
arr = np.array([10, 20, 30])

arr + 5
```

Output:

```text
[15 25 35]
```

```python
arr * 2
```

Output:

```text
[20 40 60]
```

```python
arr / 10
```

Output:

```text
[1. 2. 3.]
```

---

# Comparison Operations

```python
arr = np.array([10, 20, 30])
```

Greater than:

```python
arr > 15
```

Output:

```text
[False  True  True]
```

Equal:

```python
arr == 20
```

Output:

```text
[False  True False]
```

Not equal:

```python
arr != 20
```

Less than:

```python
arr < 25
```

---

# Aggregation Functions

NumPy provides many functions for summarizing data.

```python
arr = np.array([10, 20, 30, 40, 50])
```

## Sum

```python
np.sum(arr)
```

Output:

```text
150
```

---

## Mean

```python
np.mean(arr)
```

Output:

```text
30.0
```

---

## Median

```python
np.median(arr)
```

---

## Minimum

```python
np.min(arr)
```

---

## Maximum

```python
np.max(arr)
```

---

## Standard Deviation

```python
np.std(arr)
```

---

## Variance

```python
np.var(arr)
```

---

## Product

```python
np.prod(arr)
```

---

# Aggregation Methods

Many NumPy functions are also available as array methods.

```python
arr.sum()
arr.mean()
arr.min()
arr.max()
arr.std()
arr.var()
```

Both approaches are common.

---

# Axis

Understanding `axis` is extremely important.

Consider:

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

Shape:

```text
(2, 3)
```

There are:

```text
2 rows
3 columns
```

---

## `axis=0`

Perform the operation down the rows.

```python
arr.sum(axis=0)
```

Output:

```text
[50 70 90]
```

Because:

```text
10 + 40 = 50
20 + 50 = 70
30 + 60 = 90
```

Think:

> `axis=0` → operate vertically → result for each column.

---

## `axis=1`

Perform the operation across columns.

```python
arr.sum(axis=1)
```

Output:

```text
[60 150]
```

Because:

```text
10 + 20 + 30 = 60
40 + 50 + 60 = 150
```

Think:

> `axis=1` → operate horizontally → result for each row.

---

# Mathematical Functions

NumPy provides many mathematical functions.

## Square Root

```python
np.sqrt(arr)
```

---

## Exponential

```python
np.exp(arr)
```

---

## Natural Logarithm

```python
np.log(arr)
```

---

## Base-10 Logarithm

```python
np.log10(arr)
```

---

## Absolute Value

```python
np.abs(arr)
```

---

## Sine

```python
np.sin(arr)
```

---

## Cosine

```python
np.cos(arr)
```

---

# Rounding

## `np.round()`

```python
arr = np.array([1.2345, 2.6789])

np.round(arr, 2)
```

Output:

```text
[1.23 2.68]
```

---

## `np.floor()`

Rounds down:

```python
np.floor([1.2, 2.9, 3.1])
```

---

## `np.ceil()`

Rounds up:

```python
np.ceil([1.2, 2.1, 3.1])
```

---

# Handling Missing Values

NumPy represents missing numerical values using `np.nan`.

```python
arr = np.array([10, 20, np.nan, 40])
```

Check for NaN:

```python
np.isnan(arr)
```

Output:

```text
[False False  True False]
```

---

## `np.nanmean()`

Normal mean:

```python
np.mean(arr)
```

will produce:

```text
nan
```

Use:

```python
np.nanmean(arr)
```

to ignore NaN values.

---

## Other NaN-aware Functions

```python
np.nansum(arr)
np.nanmean(arr)
np.nanmedian(arr)
np.nanmin(arr)
np.nanmax(arr)
np.nanstd(arr)
```

These functions are especially useful when working with real-world datasets.

---

# Sorting

```python
arr = np.array([50, 10, 40, 20, 30])

np.sort(arr)
```

Output:

```text
[10 20 30 40 50]
```

The original array is not modified.

---

## In-place sorting

```python
arr.sort()
```

Now `arr` itself is sorted.

---

# `argsort()`

Returns the indices that would sort the array.

```python
arr = np.array([50, 10, 40, 20])

np.argsort(arr)
```

Output:

```text
[1 3 2 0]
```

Because:

```text
arr[1] = 10
arr[3] = 20
arr[2] = 40
arr[0] = 50
```

This is very useful when you need to sort one array while keeping another array aligned.

---

# Searching

## `np.where()`

Find positions where a condition is true.

```python
arr = np.array([10, 20, 30, 40])

np.where(arr > 20)
```

Returns the indices where the condition is true.

---

## Replace Based on a Condition

```python
np.where(arr > 20, 1, 0)
```

Result:

```text
[0 0 1 1]
```

Meaning:

```text
if value > 20 → 1
otherwise → 0
```

---

# `np.argmax()`

Returns the index of the maximum value.

```python
arr = np.array([10, 50, 20, 30])

np.argmax(arr)
```

Output:

```text
1
```

---

# `np.argmin()`

Returns the index of the minimum value.

```python
np.argmin(arr)
```

Output:

```text
0
```

---

# Conditional Operations

## `np.any()`

Checks whether at least one element is `True`.

```python
arr = np.array([10, 20, 30])

np.any(arr > 25)
```

Output:

```text
True
```

---

## `np.all()`

Checks whether all elements satisfy the condition.

```python
np.all(arr > 5)
```

Output:

```text
True
```

---

# Broadcasting

Broadcasting allows NumPy to perform operations between arrays with compatible shapes.

Example:

```python
arr = np.array([10, 20, 30])

arr + 5
```

NumPy effectively treats `5` as if it were:

```text
[5, 5, 5]
```

Result:

```text
[15 25 35]
```

---

## Broadcasting with 2D Arrays

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

arr + np.array([1, 2, 3])
```

Result:

```text
[[11 22 33]
 [41 52 63]]
```

The 1D array is broadcast across the rows.

---

# Vectorization

One of NumPy's biggest advantages is **vectorized operations**.

Instead of:

```python
numbers = [1, 2, 3, 4]

result = []

for number in numbers:
    result.append(number * 2)
```

With NumPy:

```python
numbers = np.array([1, 2, 3, 4])

result = numbers * 2
```

Result:

```text
[2 4 6 8]
```

This is:

* shorter
* easier to read
* generally faster for numerical workloads

---

# Avoiding Unnecessary Loops

Instead of:

```python
for i in range(len(arr)):
    arr[i] = arr[i] * 2
```

Prefer:

```python
arr = arr * 2
```

Instead of:

```python
result = []

for value in arr:
    if value > 50:
        result.append(value)
```

Use:

```python
result = arr[arr > 50]
```

This style is fundamental to working effectively with NumPy.

---

# Random Numbers

NumPy provides a modern random number generator API.

Recommended:

```python
rng = np.random.default_rng()
```

---

## Random Integers

```python
rng.integers(1, 10)
```

Generate multiple:

```python
rng.integers(1, 10, size=5)
```

Possible result:

```text
[4 8 1 7 3]
```

---

## Random Floats

```python
rng.random()
```

Multiple:

```python
rng.random(5)
```

Values are between:

```text
0 <= x < 1
```

---

## Random Array

```python
rng.random((2, 3))
```

---

# Reproducible Random Numbers

For reproducible results:

```python
rng = np.random.default_rng(42)
```

Then:

```python
rng.integers(1, 100, size=5)
```

Using the same seed produces the same sequence.

This is important for:

* experiments
* testing
* machine learning
* debugging

---

# Random Choice

Choose random values from an array:

```python
arr = np.array(["A", "B", "C", "D"])

rng.choice(arr)
```

Multiple:

```python
rng.choice(arr, size=3)
```

---

# Linear Algebra Basics

NumPy can perform basic linear algebra operations.

---

## Dot Product

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.dot(a, b)
```

Calculation:

```text
1×4 + 2×5 + 3×6 = 32
```

---

## Matrix Multiplication

Use `@`:

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

A @ B
```

Or:

```python
np.matmul(A, B)
```

---

## Determinant

```python
A = np.array([
    [1, 2],
    [3, 4]
])

np.linalg.det(A)
```

---

## Inverse

```python
np.linalg.inv(A)
```

Only use this when the matrix is invertible.

---

# Copy vs View

This is an important NumPy concept.

---

## View

A view shares the same underlying data.

```python
arr = np.array([1, 2, 3, 4])

view = arr[1:3]

view[0] = 100
```

Now:

```python
arr
```

may be:

```text
[1 100 3 4]
```

because the slice is a view of the original array.

---

## Copy

Use `.copy()` when you want independent data:

```python
copy = arr[1:3].copy()
```

Now changing `copy` will not modify `arr`.

---

# Saving and Loading Arrays

## Save a Single Array

```python
np.save("data.npy", arr)
```

Load:

```python
arr = np.load("data.npy")
```

---

## Save Multiple Arrays

```python
np.savez(
    "data.npz",
    values=arr,
    other=another_array
)
```

Load:

```python
data = np.load("data.npz")
```

Access:

```python
data["values"]
data["other"]
```

---

# Working with Text Files

You can also save arrays as text:

```python
np.savetxt("data.csv", arr, delimiter=",")
```

Load:

```python
arr = np.loadtxt("data.csv", delimiter=",")
```

For serious CSV/data analysis workflows, however, **Pandas is usually more appropriate**.

---

# Useful Patterns

## Find values above a threshold

```python
arr[arr > 100]
```

---

## Find values within a range

```python
arr[(arr >= 50) & (arr <= 100)]
```

---

## Replace negative values

```python
arr[arr < 0] = 0
```

---

## Count values satisfying a condition

```python
np.sum(arr > 100)
```

Because `True` behaves like `1` and `False` like `0`.

---

## Calculate the percentage above a threshold

```python
percentage = np.mean(arr > 100) * 100
```

---

## Normalize values

A simple min-max normalization:

```python
normalized = (arr - arr.min()) / (arr.max() - arr.min())
```

Result:

```text
0 <= normalized <= 1
```

---

## Find unique values

```python
np.unique(arr)
```

---

## Count unique values

```python
values, counts = np.unique(arr, return_counts=True)
```

Example:

```python
arr = np.array([1, 2, 2, 3, 3, 3])

values, counts = np.unique(arr, return_counts=True)
```

Result:

```text
values = [1 2 3]
counts = [1 2 3]
```

---

# NumPy vs Python Lists

Python list:

```python
numbers = [1, 2, 3, 4]
```

NumPy array:

```python
numbers = np.array([1, 2, 3, 4])
```

There are important differences.

| Feature                 | Python List          | NumPy Array                  |
| ----------------------- | -------------------- | ---------------------------- |
| Data types              | Can be mixed         | Usually homogeneous          |
| Numerical operations    | Limited              | Excellent                    |
| Vectorization           | No                   | Yes                          |
| Multidimensional data   | Possible but awkward | Native                       |
| Mathematical operations | Requires loops       | Built-in                     |
| Performance             | General-purpose      | Optimized for numerical data |
| Memory efficiency       | Generally lower      | Generally better             |
| Data Science            | Limited              | Fundamental                  |

---

# Python List vs NumPy Array Example

Python:

```python
numbers = [1, 2, 3]

numbers * 2
```

Result:

```python
[1, 2, 3, 1, 2, 3]
```

This means list repetition.

NumPy:

```python
numbers = np.array([1, 2, 3])

numbers * 2
```

Result:

```text
[2 4 6]
```

This means numerical multiplication.

This distinction is extremely important.

---