# Multidimensional
A list or tuple is **multidimensional** if it contains another list or tuple. The best illustration for this is a matrix.

Consider the following *3x3* matrix:
\\[
\begin{matrix}
1 & 2 & 3 \\\\
4 & 5 & 6 \\\\
7 & 8 & 9
\end{matrix}
\\]

We can represent this in Python using a **2-dimensional** list.
```python
matrix = [
# Column (C)
#   C0  C1  C2
	[1, 2, 3], # Row 0
	[4, 5, 6], # Row 1
	[7, 8, 9], # Row 2
]
```

## Accessing Elements
To access the elements of `matrix`, we can use our standard indexing notation of square brackets.

The first index will target the row. The second will target the column.

For example, `5` is located at Row 1, Column 1:

```python,runnable
matrix = [
# Column (C)
#   C0  C1  C2
	[1, 2, 3], # Row 0
	[4, 5, 6], # Row 1
	[7, 8, 9], # Row 2
]

print (matrix[1]) # [4, 5, 6]
print (matrix[1][1]) # 5
```

```
Output:
[4, 5, 6]
5
```

## Looping
To loop through items in our matrix, we can use a nested list:

```python,runnable
matrix = [
# Column (C)
#   C0  C1  C2
	[1, 2, 3], # Row 0
	[4, 5, 6], # Row 1
	[7, 8, 9], # Row 2
]

for row in matrix:
	for num in row:
		print (num)
```
```
Output:
1
2
3
4
5
6
7
8
9
```
