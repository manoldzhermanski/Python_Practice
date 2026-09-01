# 🐼 Pandas Cheat Sheet

A practical Pandas reference built progressively throughout the course.

The goal is not only to memorize syntax, but to understand **how Pandas represents, accesses, inspects, and manipulates tabular data**.

---

# 1. What is Pandas?

**Pandas** is a Python library used for working with structured and tabular data.

It is commonly used for:

* Data analysis
* Data cleaning
* Data transformation
* Exploratory Data Analysis (EDA)
* Working with CSV and Excel files
* Preparing data for Machine Learning

Pandas is built on top of **NumPy** and provides higher-level structures for working with labeled data.

```python
import pandas as pd
```

The conventional alias for Pandas is:

```python
pd
```

---

# 2. Pandas Data Structures

Pandas primarily works with two data structures:

```text
Pandas
│
├── Series
│
└── DataFrame
```

## Series

A **Series** is a one-dimensional labeled array.

You can think of it as:

```text
Index   Value
0       10
1       20
2       30
3       40
```

Example:

```python
import pandas as pd

numbers = pd.Series([10, 20, 30, 40])

print(numbers)
```

Output:

```text
0    10
1    20
2    30
3    40
dtype: int64
```

A Series has:

* Values
* An index
* A data type

---

# 3. Creating a Series

## From a Python list

```python
numbers = pd.Series([10, 20, 30, 40])
```

## With a custom index

```python
numbers = pd.Series(
    [10, 20, 30],
    index=["a", "b", "c"]
)

print(numbers)
```

Output:

```text
a    10
b    20
c    30
dtype: int64
```

The index does not have to be numeric.

---

# 4. Accessing Series Elements

A Series can be accessed using its index.

```python
numbers = pd.Series(
    [10, 20, 30],
    index=["a", "b", "c"]
)

print(numbers["a"])
```

Output:

```text
10
```

You can also access by positional index:

```python
print(numbers.iloc[0])
```

Output:

```text
10
```

### Important

There is a difference between:

```python
numbers["a"]
```

and:

```python
numbers.iloc[0]
```

The first uses the **label** `"a"`.

The second uses the **position** `0`.

We will study `loc` and `iloc` in much greater detail later.

---

# 5. DataFrame

A **DataFrame** is a two-dimensional labeled data structure.

It is the structure we will use most frequently when working with datasets.

You can think of a DataFrame as a table:

```text
        name     age    salary
0       Ivan     25     2500
1       Maria    30     3200
2       Peter    28     2800
```

Each column is essentially a **Series**.

```text
DataFrame
│
├── name   → Series
├── age    → Series
└── salary → Series
```

---

# 6. Creating a DataFrame

## From a Dictionary

One of the most common ways to create a DataFrame is from a dictionary.

```python
data = {
    "name": ["Ivan", "Maria", "Peter"],
    "age": [25, 30, 28],
    "salary": [2500, 3200, 2800]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    name  age  salary
0   Ivan   25    2500
1  Maria   30    3200
2  Peter   28    2800
```

The dictionary keys become the **column names**.

The lists become the **column values**.

---

# 7. DataFrame Index

Every DataFrame has an index.

By default, Pandas creates:

```text
0
1
2
...
```

Example:

```python
df = pd.DataFrame({
    "name": ["Ivan", "Maria", "Peter"],
    "age": [25, 30, 28]
})
```

The resulting index is:

```text
0
1
2
```

You can provide your own index:

```python
df = pd.DataFrame(
    {
        "name": ["Ivan", "Maria", "Peter"],
        "age": [25, 30, 28]
    },
    index=["employee_1", "employee_2", "employee_3"]
)
```

Result:

```text
              name  age
employee_1    Ivan   25
employee_2   Maria   30
employee_3   Peter   28
```

---

# 8. Basic DataFrame Properties

Pandas provides several useful properties for quickly understanding a DataFrame.

---

## `df.shape`

Returns:

```text
(rows, columns)
```

Example:

```python
print(df.shape)
```

Output:

```text
(3, 2)
```

This means:

```text
3 rows
2 columns
```

---

## `df.columns`

Returns the column names.

```python
print(df.columns)
```

Example output:

```text
Index(['name', 'age'], dtype='object')
```

---

## `df.index`

Returns the DataFrame index.

```python
print(df.index)
```

---

## `df.dtypes`

Returns the data type of each column.

```python
print(df.dtypes)
```

Example:

```text
name    object
age      int64
dtype: object
```

The exact dtype can vary depending on the data and Pandas version.

---

# 9. Inspecting a DataFrame

Before working with a dataset, we should first **inspect it**.

This is an important Data Analysis habit:

```text
Load data
    ↓
Inspect data
    ↓
Understand structure
    ↓
Clean data
    ↓
Analyze data
```

---

## `df.head()`

Displays the first 5 rows by default.

```python
df.head()
```

You can specify the number of rows:

```python
df.head(10)
```

---

## `df.tail()`

Displays the last 5 rows by default.

```python
df.tail()
```

Or:

```python
df.tail(10)
```

---

# 10. `df.info()`

`info()` provides a concise summary of the DataFrame.

```python
df.info()
```

It shows information such as:

* Number of rows
* Column names
* Number of non-null values
* Data types
* Memory usage

Example:

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   name    3 non-null      object
 1   age     3 non-null      int64
 2   salary  3 non-null      int64
```

`info()` is especially useful when working with an unfamiliar dataset.

---

# 11. `df.describe()`

`describe()` generates descriptive statistics for numerical columns.

```python
df.describe()
```

For example:

```text
             age       salary
count    3.000000     3.000000
mean    27.666667  2833.333333
std      2.516611   351.188458
min     25.000000  2500.000000
max     30.000000  3200.000000
```

It can provide statistics such as:

* `count`
* `mean`
* `std`
* `min`
* `25%`
* `50%`
* `75%`
* `max`

We will study these statistics and their meaning later.

---

# 12. Selecting a Single Column

A DataFrame column can be selected using:

```python
df["age"]
```

Example:

```python
ages = df["age"]

print(ages)
```

The result is a **Series**.

This demonstrates an important relationship:

```text
DataFrame
    ↓
select one column
    ↓
Series
```

---

# 13. Selecting Multiple Columns

Multiple columns can be selected using a list of column names:

```python
df[["name", "salary"]]
```

Notice the double brackets:

```python
df["name"]              # One column → Series

df[["name", "salary"]]  # Multiple columns → DataFrame
```

This distinction is extremely important.

---

# 14. Reading a CSV File

Real datasets are usually stored in files rather than manually created dictionaries.

Pandas provides:

```python
pd.read_csv()
```

Example:

```python
df = pd.read_csv("employees.csv")
```

---

# 15. Selecting Columns

A DataFrame column can be selected using its column label.

## Single column

```python
df["age"]
```

Selecting a single column returns a **Series**.

```python
ages = df["age"]

print(type(ages))
```

---

## Multiple columns

Multiple columns can be selected by passing a list of column names.

```python
df[["name", "age", "salary"]]
```

---

# 16. `loc[]`

`loc[]` is used for **label-based selection**.

It selects data using the labels of rows and columns.

```python
df.loc[row_label]
```

Example:

```python
df.loc[2]
```

This selects the row whose index label is `2`.

---

## Selecting a specific value

We can provide both a row label and a column label:

```python
df.loc[2, "salary"]
```

This means:

```text
row label → 2
column label → salary
```

The result is the value stored at that position.

---

## Selecting specific rows

Multiple row labels can be provided as a list:

```python
df.loc[[0, 2, 4]]
```

This selects rows with labels:

```text
0
2
4
```

---

## Selecting specific rows and columns

```python
df.loc[
    [0, 2, 4],
    ["name", "salary"]
]
```

This selects:

```text
Rows:
0, 2, 4

Columns:
name, salary
```

---

# 17. `iloc[]`

`iloc[]` is used for **position-based selection**.

It selects data based on the integer position of rows and columns.

```python
df.iloc[row_position]
```

For example:

```python
df.iloc[2]
```

selects the **third row**, because positions start at `0`.

```text
Position 0 → first row
Position 1 → second row
Position 2 → third row
```

---

## Selecting a specific value

We can specify both the row and column position:

```python
df.iloc[2, 1]
```

This means:

```text
row position → 2
column position → 1
```

---

## Selecting specific rows

```python
df.iloc[[0, 2, 4]]
```

This selects the first, third and fifth rows by position.

---

## Selecting specific rows and columns

```python
df.iloc[
    [0, 2, 4],
    [0, 2]
]
```

This selects:

```text
Rows:
positions 0, 2, 4

Columns:
positions 0 and 2
```

---

# 18. `loc` vs `iloc`

The most important distinction:

```text
loc
↓
LABEL

iloc
↓
POSITION
```

Consider a DataFrame with custom index labels:

```python
df = pd.DataFrame({
    "name": ["Ivan", "Maria", "Peter", "Anna"],
    "salary": [2500, 3200, 2800, 2100]
}, index=["EMP101", "EMP205", "EMP309", "EMP412"])
```

The DataFrame looks like:

```text
          name    salary
EMP101    Ivan      2500
EMP205    Maria     3200
EMP309    Peter     2800
EMP412    Anna      2100
```

### `loc`

```python
df.loc["EMP309"]
```

means:

> Find the row whose **label** is `"EMP309"`.

---

### `iloc`

```python
df.iloc[2]
```

means:

> Find the row at **position 2**.

Both return the row containing Peter, but they get there differently.

```text
loc["EMP309"]
       ↓
find this LABEL

iloc[2]
       ↓
find this POSITION
```

---

# 19. `loc` and `iloc` with Columns

The same concept applies to columns.

Suppose:

```text
          name    age    salary
EMP101    Ivan     25     2500
EMP205    Maria    30     3200
EMP309    Peter    28     2800
```

The column labels are:

```text
"name"
"age"
"salary"
```

Their positions are:

```text
0 → name
1 → age
2 → salary
```

Therefore:

```python
df.loc["EMP309", "salary"]
```

uses **labels**.

While:

```python
df.iloc[2, 2]
```

uses **positions**.

Both select the same value:

```text
2800
```

---

# 20. Slicing with `iloc`

`iloc` follows normal Python-style slicing.

```python
df.iloc[0:3]
```

selects positions:

```text
0
1
2
```

The ending position `3` is **not included**.

This is the same slicing rule used by Python lists.

---

## Selecting rows and columns with `iloc`

```python
df.iloc[0:3, 0:2]
```

means:

```text
Rows:
positions 0, 1, 2

Columns:
positions 0, 1
```

---

# 21. Slicing with `loc`

`loc` uses labels when slicing.

For example:

```python
df.loc["EMP101":"EMP309"]
```

selects:

```text
EMP101
EMP205
EMP309
```

Unlike normal Python slicing, the ending label is **included** when using label-based slicing.

### Important difference

```python
df.iloc[0:3]
```

→ ending position `3` is excluded.

```python
df.loc["EMP101":"EMP309"]
```

→ ending label `"EMP309"` is included.

---

# 22. Boolean Indexing / Filtering

Pandas allows us to filter rows using conditions.

For example:

```python
df[df["age"] > 25]
```

This selects all rows where `age` is greater than `25`.

The expression:

```python
df["age"] > 25
```

produces a Boolean Series:

```text
False
True
True
False
...
```

Pandas keeps the rows where the result is `True`.

---

## Filtering with comparison operators

Common operators include:

```text
>       greater than
<       less than
>=      greater than or equal to
<=      less than or equal to
==      equal to
!=      not equal to
```

Examples:

```python
df[df["age"] >= 30]
```

```python
df[df["salary"] < 3000]
```

```python
df[df["department"] == "IT"]
```

```python
df[df["department"] != "IT"]
```

---

# 23. Multiple Conditions

Multiple conditions can be combined using:

```text
&    AND
|    OR
~    NOT
```

## AND

```python
df[
    (df["age"] > 25) &
    (df["salary"] > 3000)
]
```

Both conditions must be `True`.

---

## OR

```python
df[
    (df["department"] == "IT") |
    (df["department"] == "HR")
]
```

At least one condition must be `True`.

---

## NOT

```python
df[
    ~(df["department"] == "IT")
]
```

This selects rows where the department is **not** IT.

---

# 24. Combining Filtering and Column Selection

Filtering and column selection can be combined.

For example, to display only the names and salaries of employees earning more than `3000`:

```python
df.loc[
    df["salary"] > 3000,
    ["name", "salary"]
]
```

This is often preferable to:

```python
df[df["salary"] > 3000][["name", "salary"]]
```

because `loc` allows us to specify both the **rows** and **columns** in one operation.

---
