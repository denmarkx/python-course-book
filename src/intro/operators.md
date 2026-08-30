# Operators
An **operator** is used to perform some operation on variables and values. There are several types, but we are mainly concerned with **arithmetic**, **assignment**, **comparison**, and **logical** operators.

Operators can be used directly between values, variables, and both. They follow the standard **order of operations** used in mathematics.

```python
# Variable + Variable
x = 10
y = 5
sum = x + y

# Value + Variable
sum = 10 + y

# Value + Value
sum = 10 + 5
```

## Arithmetic Operators
Performs common math operations:

| Operator | Name | Description |
| -------- | ---- | ----------- |
| + | Addition | Adds two values |
| - | Subtraction | Subtracts two values |
| * | Multiplication | Multiplies two values |
| / | Division | Divides two values |
| % | Modulo | Division remainder |

## Assignment Operators
Assigns some value to a variable:

| Operator | Description |
| -------- | ----------- |
| = | Assignment |
| += | Increment |
| -= | Decrement |
| *= | Multiply |
| /= | Divide |
| %= | Modulo |


The assignment operators involving arithmetic is a short hand way of writing code:

```python
x = 5

# Shorter way:
x += 10

# ..is the same as writing:
x = x + 10
```

## Comparison Operators
Compares two values or variables. These return a boolean.


| Operator | Description |
| -------- | ----------- |
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |


Example:
```python,runnable
x = 1
print (x == 1) # True

y = 20
print (x > y) # False

print (1 != 0) # True
```

```
Output:
True
False
True
```

## Logical Operators
Logical operators are used to combine comparison operations. These also return a boolean.

| Operator | Description |
| -------- | ----------- |
| and | True if both statements are true. |
| or | True if one of the statements is true. |
| not | Returns false is statement is true. |

Example:
```python,runnable
x = 5
y = 20

# true (both statements are true):
print (x == 5 and y == 20)

# false: (neither statement is true).
print (x == 2 or y == 1)
```

```
Output:
True
False
```
