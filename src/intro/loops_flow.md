# Loop Flow
There are two primary ways to control the flow of the loop while it is in progress: **break** and **continue**.

## Break
An easy way to read `break` is if you want to "break out of the loop" and stop it from progressing at a certain point.

For example, if we were looping through the first 10 integers starting from 0, but want to stop at 7:

```python,runnable
for num in range(10):
	if num == 7:
		break
	print (num)
```

```
Output:
0
1
2
3
4
5
6
```

## Continue
**Continue** is used if we want to *skip* an iteration.

For example, under the same scenario, let's skip the number 7 only.

```python,runnable
for num in range(10):
	if num == 7:
		continue
	print (num)
```
```
Output:
0
1
2
3
4
5
6
8
9
```
