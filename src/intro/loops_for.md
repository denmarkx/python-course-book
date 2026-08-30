# For Loops
Let's say we wanted to print out the numbers 0 through 5 (non-inclusive). 

We could write:

```python,runnable
print (0)
print (1)
print (2)
print (3)
print (4)
```

```
Output:
0
1
2
3
4
```

This gets a bit cumbersome when we want to print the numbers 0 through 20 (non-inclusive). For that, we can use a **for loop**. In Python, we can loop through some **iterable**.

To get an iterable of numbers, we can use the **range** function: `range(start, end, step)` where end is non-inclusive.

```python,runnable
for num in range(20):
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
7
8
9
10
11
12
13
14
15
16
17
18
19
```

We can use this to do all sorts of things. For example, the sum of numbers 1 to 10 (inclusive):

```python,runnable
sum = 0
for num in range(1, 11):
	sum += num
print (sum)
```
```
Output:
55
```
