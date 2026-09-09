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

# 25. Sorting Data

`sort_values()` is used to sort a DataFrame by one or more columns.

## Sorting in ascending order

```python
df.sort_values("salary")
```

By default, `ascending=True`.

---

## Sorting in descending order

Use `ascending=False`:

```python
df.sort_values("salary", ascending=False)
```

This puts the highest salary first.

---

## Sorting by multiple columns

We can provide a list of columns:

```python
df.sort_values(["department", "salary"])
```

Pandas first sorts by `department`, and then sorts rows within each department by `salary`.

---

## Different sorting directions

Each column can have its own sorting direction:

```python
df.sort_values(
    ["department", "salary"],
    ascending=[True, False]
)
```

This means:

```text
department → ascending
salary     → descending
```

---

## Sorting does not modify the original DataFrame

By default:

```python
sorted_df = df.sort_values("salary")
```

creates a sorted DataFrame while leaving `df` unchanged.

You can also assign the result back:

```python
df = df.sort_values("salary")
```

Although `inplace=True` is available:

```python
df.sort_values("salary", inplace=True)
```

it is often clearer to explicitly assign the result to a variable.

---

# 26. Adding New Columns

A new column can be created simply by assigning a value to a new column name.

## Assigning the same value to every row

```python
df["bonus"] = 500
```

Every row receives the value `500`.

---

## Creating a column from another column

Pandas allows vectorized operations on entire columns.

For example:

```python
df["annual_salary"] = df["salary"] * 12
```

If:

```text
salary
2500
3200
2800
```

the result is:

```text
annual_salary
30000
38400
33600
```

No `for` loop is required.

---

## Creating a column from multiple columns

We can use several columns in an expression:

```python
df["salary_with_bonus"] = df["salary"] + df["bonus"]
```

Or:

```python
df["annual_salary_with_bonus"] = (
    df["salary"] + df["bonus"]
) * 12
```

Pandas performs the calculation row by row.

---

# 27. Modifying Existing Columns

An existing column can be modified by assigning a new Series or calculation to it.

## Increase every salary by 500

```python
df["salary"] = df["salary"] + 500
```

Or:

```python
df["salary"] += 500
```

---

## Increase every salary by 10%

```python
df["salary"] = df["salary"] * 1.10
```

This applies the calculation to every row.

---

# 28. Modifying Specific Values with `loc`

`loc` can be used to modify specific cells.

For example:

```python
df.loc[0, "salary"] = 3000
```

This changes the salary of the row with index `0`.

---

## Modifying multiple rows

We can provide multiple labels:

```python
df.loc[[0, 2], "salary"] = 5000
```

This changes the salary of rows `0` and `2`.

---

# 29. Conditional Modification

`loc` becomes especially powerful when combined with filtering.

For example:

> Increase the salary of all IT employees by 10%.

```python
df.loc[
    df["department"] == "IT",
    "salary"
] *= 1.10
```

The condition:

```python
df["department"] == "IT"
```

selects the relevant rows.

The second part:

```python
"salary"
```

specifies which column should be modified.

Conceptually:

```text
filter rows
      ↓
select column
      ↓
modify values
```

---

# 30. Creating a Boolean Column

We can create a column containing `True` / `False` values.

For example:

```python
df["is_senior"] = df["age"] >= 30
```

The comparison is performed for every row.

Example:

```text
age    is_senior
25     False
30     True
28     False
22     False
35     True
27     False
31     True
```

This is often simpler than manually creating the column with `loc`.

---

## Creating a Boolean column with `loc`

The same result can also be achieved using `loc`:

```python
df["is_senior"] = False

df.loc[
    df["age"] >= 30,
    "is_senior"
] = True
```

This approach is useful when the values or conditions are more complex.

---

# 31. Removing Columns with `drop()`

`drop()` can be used to remove rows or columns.

## Removing a column

```python
df.drop("bonus", axis=1)
```

Here:

```text
axis=1 → columns
```

---

## Removing multiple columns

```python
df.drop(
    ["bonus", "annual_salary"],
    axis=1
)
```

---

## Removing a row

```python
df.drop(0, axis=0)
```

Here:

```text
axis=0 → rows
```

### Remember

```text
axis=0 → rows
axis=1 → columns
```

---

## `drop()` does not modify the original DataFrame by default

For example:

```python
new_df = df.drop("bonus", axis=1)
```

The original `df` remains unchanged.

You can assign the result back:

```python
df = df.drop("bonus", axis=1)
```

---

# 32. Renaming Columns

`rename()` can be used to change column names.

```python
df.rename(
    columns={
        "salary": "monthly_salary"
    }
)
```

Multiple columns can be renamed at once:

```python
df.rename(
    columns={
        "name": "employee_name",
        "salary": "monthly_salary"
    }
)
```

Again, `rename()` returns a new DataFrame by default.

You can assign it back:

```python
df = df.rename(
    columns={
        "salary": "monthly_salary"
    }
)
```

---

# 33. `unique()`

`unique()` returns all unique values in a Series.

It removes duplicate values while preserving the order in which values are first encountered.

### Example

If a column contains:

```text
IT
HR
IT
Marketing
IT
HR
Marketing
```

then:

```python
df["department"].unique()
```

returns:

```text
["IT", "HR", "Marketing"]
```

---

# 34. `nunique()`

`nunique()` returns the **number of unique values** in a Series.

```python
df["department"].nunique()
```

Result:

```text
3
```

---

# 35. `value_counts()`

`value_counts()` counts how many times each unique value occurs.

```python
df["department"].value_counts()
```

Example result:

```text
IT           3
HR           2
Marketing    2
```
---

## Sorting with `value_counts()`

By default, the most frequent values appear first.

```python
df["department"].value_counts()
```

To display the least frequent values first:

```python
df["department"].value_counts(ascending=True)
```

---

## `value_counts(normalize=True)`

By default, `value_counts()` returns absolute counts.

With:

```python
normalize=True
```

it returns proportions instead.

```python
df["department"].value_counts(normalize=True)
```

Example:

```text
IT           0.428571
HR           0.285714
Marketing    0.285714
```

To convert proportions into percentages:

```python
df["department"].value_counts(normalize=True) * 100
```

Result:

```text
IT           42.857143
HR           28.571429
Marketing    28.571429
```

---

## `value_counts()` and Missing Values

By default, `value_counts()` does not include `NaN` values.

```python
df["department"].value_counts()
```

If we also want to count missing values:

```python
df["department"].value_counts(dropna=False)
```

This becomes especially useful when performing data quality checks.

---

## `value_counts()` with Multiple Columns

We can use `value_counts()` on multiple columns:

```python
df[["department", "age"]].value_counts()
```

Instead of counting individual values, Pandas counts unique **combinations** of the selected columns.

For example:

```text
department    age
IT            25     1
IT            28     1
IT            35     1
HR            30     1
HR            27     1
...
```

---

# 36. `groupby()`

`groupby()` is one of the most important Pandas operations.

It allows us to:

> **Split data into groups, perform an operation on each group, and combine the results.**

For example:

> What is the average salary in each department?

```python
df.groupby("department")["salary"].mean()
```

Result:

```text
department
HR           3050
IT           3100
Marketing    2800
```

---

# 37. Grouping by Multiple Columns

We can group by more than one column:

```python
df.groupby(
    ["department", "age"]
)["salary"].mean()
```

This creates groups based on the combination of:

```text
department + age
```

This is similar to the combinations we saw with:

```python
df[["department", "age"]].value_counts()
```

but `groupby()` allows us to perform arbitrary aggregations on those groups.

---

# 38. Multiple Aggregations with `agg()`

`agg()` allows us to perform multiple aggregation operations at once.

For example:

```python
df.groupby("department")["salary"].agg(
    ["mean", "min", "max"]
)
```

This gives us:

```text
             mean    min    max
department
HR             ...    ...    ...
IT             ...    ...    ...
Marketing      ...    ...    ...
```

This is much more powerful than calculating each statistic separately.

---

## Named Aggregations

We can give meaningful names to the resulting columns:

```python
df.groupby("department").agg(
    average_salary=("salary", "mean"),
    minimum_salary=("salary", "min"),
    maximum_salary=("salary", "max")
)
```

This produces a DataFrame with descriptive column names:

```text
             average_salary    minimum_salary    maximum_salary
department
HR                  ...
IT                  ...
Marketing           ...
```

This style is especially useful when preparing data for reports or further analysis.

---

# 39. `idxmax()`

`idxmax()` returns the **index label** where the maximum value occurs.

This is especially useful when we don't just want the maximum value, but also want to know **where that value is located**.

For example:

```python
df["salary"].idxmax()
```

If the DataFrame is:

```text
      name  salary
0     Ivan    2500
1    Maria    3200
2    Peter    2800
3     Anna    2100
4   Georgi    4000
```

the result is:

```text
4
```

Because the highest salary (`4000`) is located at index `4`.

---

## `max()` vs `idxmax()`

These two methods answer different questions:

```python
df["salary"].max()
```

→ **What is the maximum value?**

```text
4000
```

While:

```python
df["salary"].idxmax()
```

→ **Where is the maximum value?**

```text
4
```

---

# 40. `idxmin()`

`idxmin()` works exactly like `idxmax()`, but finds the index where the **minimum value** occurs.

```python
df["salary"].idxmin()
```

If the lowest salary is `2100` at index `3`, the result is:

```text
3
```

To retrieve the entire row:

```python
df.loc[df["salary"].idxmin()]
```

Result:

```text
name       Anna
salary      2100
```

---

# 41. `idxmax() \ idxmin()` with `groupby()`

`idxmax()` becomes particularly powerful when combined with `groupby()`.

Suppose we want to find the employee with the **highest salary in each department**.

First:

```python
df.groupby("department")["salary"].idxmax()
```

This returns the index of the highest-paid employee in each department.

Conceptually:

```text
department
HR           → index 8
IT           → index 4
Marketing    → index 6
```

We can then use those indexes with `loc`:

```python
df.loc[
    df.groupby("department")["salary"].idxmax()
]
```

This returns the actual rows of the highest-paid employees.

---

# 42. `isna()` and `notna()`

Detect missing values

```python
df.isna()
```

```python
df.notna()
```

---

### Count missing values

```python
df.isna().sum()
```

```python
df.isna().sum().sum()
```

---

### Missing percentage

```python
df.isna().mean() * 100
```

---

### Filter missing values

```python
df[df["salary"].isna()]
```

### Filter non-missing values

```python
df[df["salary"].notna()]
```

---

# 43. `dropna()`

Remove missing values

```python
df.dropna()
```

Remove rows based on specific columns:

```python
df.dropna(subset=["salary"])
```

---

# 44. `fillna()`

Fill missing values

```python
df["salary"].fillna(0)
```

```python
df["department"].fillna("Unknown")
```

---

# 45. `dtypes()`

Pandas assigns a data type (dtype) to every column.

Check the data types of all columns:

```python
df.dtypes
```

Example:

```text
name           object
age             int64
salary        float64
department     object
```
Check the type of a specific column:

```python
df["salary"].dtype
```

Common Pandas Data Types

```text
dtype	Description
int64	Integer numbers
float64	Decimal numbers
object	Usually strings/text
bool	True / False
datetime64[ns]	Dates and timestamps
category	Categorical data
string	String/text data
```
# 46. astype()

astype() converts a column to a specified data type.

```python
df["age"] = df["age"].astype(float)
df["salary"] = df["salary"].astype(int)
```

Convert a column to strings:

```python
df["age"] = df["age"].astype(str)
```

**Important**

`astype()` expects the values to be convertible to the requested type.

For example:

```python
df["salary"] = df["salary"].astype(float)
```
will fail if the column contains:

```text
2500
3200
unknown
2800
```

because `"unknown"` cannot be converted to a number.

# 47 to_numeric()

`pd.to_numeric()` is useful when a column contains values that should be numeric but may also contain invalid values.

```python
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)
```

`errors="coerce"` converts invalid values to NaN.

Example:

```text
"2500"    → 2500.0
"3200"    → 3200.0
"unknown" → NaN
"2800"    → 2800.0
```

This is especially useful during data cleaning.

# 48. .str.upper()

Converts strings to uppercase.

```python
df["name"].str.upper()
```

# 49. .str.lower()

Converts strings to lowercase.

```python
df["name"].str.lower()
```

# 50. .str.title()

Converts strings to title case.

```python
df["name"].str.title()
```

# 51. .str.strip()

Removes whitespace from the beginning and end of strings.

```python
df["name"].str.strip()
```

# 52. .str.len()

Returns the number of characters in each string.

```python
df["name"].str.len()
```

# 53. .str.count()

Counts how many times a specific substring occurs.

```python
df["name"].str.count("a")
```

# 54. .str.contains()

Checks whether a string contains a specific substring.

```python
df["name"].str.contains("an")
```

The result is a Boolean Series:

True
False
True
False

Because it returns Boolean values, it can be used for filtering:

```python
df[df["name"].str.contains("an")]
Case-insensitive search
df["name"].str.contains(
    "an",
    case=False
)
```

This ignores uppercase/lowercase differences.

### Handling missing values

If the column can contain NaN:

```python
df["name"].str.contains(
    "an",
    case=False,
    na=False
)
```

na=False treats missing values as False.

# 55. .str.startswith()

Checks whether a string starts with a specific value.

```python
df["name"].str.startswith("A")
```

# 56. .str.endswith()

Checks whether a string ends with a specific value.

```python
df["name"].str.endswith("a")
```

# 57. .str.replace()

Replaces part of a string.

```python
df["department"].str.replace(
    "IT",
    "Information Technology"
)
```

# 58. .str.split()

Splits a string into multiple parts.

```python
df["name"].str.split(" ")
```

# 59. .str.slice()

Extracts part of a string using positions.

df["name"].str.slice(0, 3)

# 60. `map()`

`map()` applies a mapping or function to every value in a Series.

Mapping with a dictionary

```python
department_map = {
    "IT": "Technology",
    "HR": "Human Resources",
    "Marketing": "Marketing"
}

df["department"] = df["department"].map(
    department_map
)
```

Important behavior

**When using a dictionary, values that are not present in the dictionary become NaN.**

Example:

```python
df["department"].map({
    "IT": "Technology",
    "HR": "Human Resources"
})
```
If the DataFrame contains:

```text
IT
HR
Marketing
```
The result will contain:

```text
Technology
Human Resources
NaN
```

because "Marketing" was not included in the dictionary.

## map() with a function

```python
def double_salary(salary):
    return salary * 2

df["double_salary"] = df["salary"].map(
    double_salary
)
```

## map() with lambda

```python
df["double_salary"] = df["salary"].map(
    lambda salary: salary * 2
)
```
`map()` is especially useful when transforming individual values in one Series.

# 61. replace()

`replace()` replaces specified values.

Dictionary:

```python
df["department"] = df["department"].replace({
    "IT": "Technology",
    "HR": "Human Resources"
})
```

**Unlike map(), values that are not specified remain unchanged.**

Example:

```python
df["department"].replace({
    "IT": "Technology",
    "HR": "Human Resources"
})
```

If the original values are:

```text
IT
HR
Marketing
```

The result is:

```text
Technology
Human Resources
Marketing
```

**"Marketing" remains unchanged because it was not included in the dictionary.**

# 62. apply()

`apply()` applies a function to values in a Series or along an axis of a DataFrame.

## apply() on a Series

Example:

```python
df["salary"].apply(
    lambda salary: salary * 1.10
)
```

## apply() with a normal function

```python
def salary_category(salary):
    if salary < 2500:
        return "Low"
    elif salary < 3500:
        return "Medium"
    else:
        return "High"

df["salary_category"] = df["salary"].apply(
    salary_category
)
```
## apply(axis=1) — Working with Rows

`apply(axis=1)` allows a function to process an entire row.

This is useful when the calculation depends on multiple columns.

Example:

```python
def is_senior(row):
    return (
        row["salary"] >= 3000
        and row["years_experience"] >= 5
    )

df["is_senior"] = df.apply(
    is_senior,
    axis=1
)
```

Each row contains the values from one employee.

For example:

```text
name              Ivan
salary            2500
department        IT
years_experience  2
```

Inside the function:

```text
row["salary"]
returns:
2500

and

row["years_experience"]
returns:
2
```
---

# 63.  Pandas `join()`

`join()` combines DataFrames, primarily using their **indexes**.

### Basic Syntax

```python
df1.join(df2)
```

By default, `join()` performs a **left join**.

---

### Basic Example

```python
employees = pd.DataFrame({
    "name": ["Ivan", "Maria", "Peter"],
    "salary": [2500, 3200, 2800]
}, index=[1, 2, 3])

departments = pd.DataFrame({
    "department": ["IT", "HR", "Marketing"]
}, index=[1, 2, 3])

result = employees.join(departments)

print(result)
```

The indexes are used to match rows.

---

### `how=`

`join()` supports four main join types:

```python
df1.join(df2, how="left")    # default
df1.join(df2, how="right")
df1.join(df2, how="inner")
df1.join(df2, how="outer")
```

| Join    | Description                            |
| ------- | -------------------------------------- |
| `left`  | Keep all rows from the left DataFrame  |
| `right` | Keep all rows from the right DataFrame |
| `inner` | Keep only matching indexes             |
| `outer` | Keep all indexes from both DataFrames  |

---

### Joining a Column to an Index

`join()` can match a column from the left DataFrame to the **index of the right DataFrame**.

```python
employees = pd.DataFrame({
    "employee_id": [1, 2, 3],
    "name": ["Ivan", "Maria", "Peter"],
    "department_id": [10, 20, 10]
})

departments = pd.DataFrame({
    "department_id": [10, 20],
    "department": ["IT", "HR"]
})

departments = departments.set_index("department_id")

result = employees.join(
    departments,
    on="department_id",
    how="left"
)
```

The relationship is:

```text
employees["department_id"]
            ↓
     departments.index
```

---

### `set_index()`

Convert a column into the DataFrame index:

```python
departments = departments.set_index("department_id")
```

This is often useful before using `join()`.

---

### `reset_index()`

Convert the index back into a regular column:

```python
df.reset_index()
```

To remove the old index:

```python
df.reset_index(drop=True)
```

---

### Overlapping Column Names

If both DataFrames contain columns with the same name, use `lsuffix` and `rsuffix`:

```python
result = df1.join(
    df2,
    lsuffix="_left",
    rsuffix="_right"
)
```

* `lsuffix` → suffix for overlapping columns from the left DataFrame
* `rsuffix` → suffix for overlapping columns from the right DataFrame

---

### Joining Multiple DataFrames

```python
result = df1.join([df2, df3])
```

Useful when multiple DataFrames share the same index.

---

### `join()` vs `merge()`

`merge()` is generally used for **column-based** relationships:

```python
employees.merge(
    departments,
    on="department_id",
    how="left"
)
```

`join()` is mainly used for **index-based** relationships:

```python
employees.join(departments)
```

Or:

```python
employees.join(
    departments,
    on="department_id"
)
```

In the last example:

```text
employees["department_id"] → departments.index
```

### Quick Rule

```text
column ↔ column  → merge()
index  ↔ index   → join()
column ↔ index   → join()
```

---

# 64. `concat()`

`concat()` is used to combine multiple Pandas objects along a particular axis.

```python
pd.concat([df1, df2])
```

The two main directions are:

```text
axis=0 → rows
axis=1 → columns
```

---

## `axis=0` — Concatenate Rows

By default, `concat()` combines DataFrames vertically.

```python
result = pd.concat([df1, df2])
```

Example:

```python
df1 = pd.DataFrame({
    "name": ["Ivan", "Maria"],
    "salary": [2500, 3200]
})

df2 = pd.DataFrame({
    "name": ["Peter", "Anna"],
    "salary": [2800, 2100]
})

result = pd.concat([df1, df2])
```

---

## `ignore_index=True`

By default, the original indexes are preserved.

```python
result = pd.concat([df1, df2])
```

This can produce:

```text
    name  salary
0   Ivan    2500
1  Maria    3200
0  Peter    2800
1   Anna    2100
```

Use `ignore_index=True` to create a new sequential index:

```python
result = pd.concat(
    [df1, df2],
    ignore_index=True
)
```

Result:

```text
    name  salary
0   Ivan    2500
1  Maria    3200
2  Peter    2800
3   Anna    2100
```

This is especially useful when combining datasets that should form one continuous table.

---

## `axis=1` — Concatenate Columns

With `axis=1`, DataFrames are combined horizontally.

```python
result = pd.concat(
    [df1, df2],
    axis=1
)
```

Conceptually:

```text
df1 | df2
```

Example:

```python
names = pd.DataFrame({
    "name": ["Ivan", "Maria", "Peter"]
})

salaries = pd.DataFrame({
    "salary": [2500, 3200, 2800]
})

result = pd.concat(
    [names, salaries],
    axis=1
)
```

Result:

```text
    name  salary
0   Ivan    2500
1  Maria    3200
2  Peter    2800
```

With `axis=1`, Pandas aligns the DataFrames using their **indexes**.

---

## Different Columns

When concatenating rows, DataFrames do not need to have identical columns.

```python
df1 = pd.DataFrame({
    "name": ["Ivan", "Maria"],
    "salary": [2500, 3200]
})

df2 = pd.DataFrame({
    "name": ["Peter", "Anna"],
    "department": ["IT", "HR"]
})

result = pd.concat(
    [df1, df2],
    ignore_index=True
)
```

Result:

```text
    name  salary department
0   Ivan  2500.0        NaN
1  Maria  3200.0        NaN
2  Peter     NaN         IT
3   Anna     NaN         HR
```

Missing values are filled with `NaN`.

---

## `join="outer"`

`outer` is the default behavior.

```python
result = pd.concat(
    [df1, df2],
    join="outer"
)
```

It keeps **all columns** from all DataFrames.

Conceptually:

```text
columns(df1) ∪ columns(df2)
```

---

## `join="inner"`

`inner` keeps only columns that exist in **all DataFrames**.

```python
result = pd.concat(
    [df1, df2],
    join="inner"
)
```

Conceptually:

```text
columns(df1) ∩ columns(df2)
```

Example:

```python
df1 = pd.DataFrame({
    "name": ["Ivan"],
    "salary": [2500]
})

df2 = pd.DataFrame({
    "name": ["Maria"],
    "salary": [3200],
    "department": ["HR"]
})

result = pd.concat(
    [df1, df2],
    join="inner",
    ignore_index=True
)
```

Result:

```text
    name  salary
0   Ivan    2500
1  Maria    3200
```

---

## `keys=`

`keys` can be used to identify where each part of the concatenated data came from.

```python
result = pd.concat(
    [df1, df2],
    keys=["Group A", "Group B"]
)
```

This creates a **MultiIndex**:

```text
          name  salary
Group A  0     Ivan    2500
         1     Maria   3200
Group B  0     Peter   2800
         1     Anna    2100
```

This can be useful when combining datasets from different sources, periods, or categories.

---

# 65. `pivot_table()`

`pivot_table()` is used to create **summary tables** from a DataFrame.

```python
df.pivot_table(
    values="column",
    index="row_dimension",
    columns="column_dimension",
    aggfunc="aggregation_function"
)
```

The most important arguments are:

| Argument     | Description                   |
| ---------    | -------------------------     |
| `values`     | Column(s) to aggregate        |
| `index`      | Column(s) used as rows        |
| `columns`    | Column(s) used as columns     |
| `aggfunc`    | Aggregation function          |
| `fill_value` | Use to replace missing values |
| `margins`    | `margins=True` adds totals (`All`) to the pivot table.
---

## Multiple `values`

We can aggregate multiple columns at the same time.

```python
employees.pivot_table(
    values=["salary", "years_experience"],
    index="department",
    columns="gender",
    aggfunc="mean"
)
```

This calculates:

* average salary
* average years of experience

for every department/gender combination.

---

## Multiple Aggregations

We can apply multiple aggregation functions:

```python
employees.pivot_table(
    values="salary",
    index="department",
    aggfunc=["mean", "min", "max"]
)
```

---