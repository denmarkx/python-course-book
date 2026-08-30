# While Loop
Alternatively, we can use a **while loop** which has the syntax of:

```
while <condition>:
	<code block>
```

Which can be read as: "while the condition is true, execute the code block".

The condition is updated within the code block. For example, printing out numbers 0 to 4 (inclusive):

```python,runnable
i = 0

# While i is less than 5:
while i < 5:
	print(i)
	i += 1 # Increment i by 1
```

```
Output:
0
1
2
3
4
```

At the beginning, `i=0`. On the next loop, `i=1`, then 2, 3, 4, and stopping when `i=5` because `5 < 5 = False`.

> [!WARNING]
> It is important that you remember to update the condition inside the while loop! Otherwise, the loop will repeat forever.
