# Looping

To loop through tuples and lists, we can use a `for` loop and the `in` keyword:

```python,runnable
# List
languages = ["Python", "Java", "C++", "Rust"]

for language in languages:
	print(language)

# Tuples
numbers = (1, 2, 3, 4)

for num in numbers:
	print (num)
```

```
Output:
Python
Java
C++
Rust
1
2
3
4
```

## Enumerate
If you need to keep track of the index alongside the element when looping through a list or tuple, you can use the `enumerate` function:

```python,runnable
languages = ["Python", "Java", "C++", "Rust"]

for i, language in enumerate(languages):
	print (i, language)
```

```
Output:
0 Python
1 Java
2 C++
3 Rust
```

## List Comprehension
Let's say we wanted to make a list with some sort of filter. Consider: `nums = [1, 2, 3, 99, 1000, 41, 5, 94]`.

We want to create a new list that filters out the odd numbers. We could do something like this:

```python,runnable
odds = []

nums = [1, 2, 3, 99, 1000, 41, 5, 94]
for num in nums:
	if (num % 2 == 0):
		odds.append(num)

print (odds)
```

```
Output:
[2, 1000, 94]
```

This is okay, but there is a simpler way to do it that is a bit faster.

**List Comprehension** is a one-line way to loop through a list, edit or filter the elements, and output a new list.

The previous example can be rewritten as:
```python,runnable
odds = [x for x in nums if x % 2 == 0]
print(odds)
```

```
Output:
[2, 1000, 94]
```

Where we iterate through each num (`x`) in `nums` and if `x % 2 == 0`, we place `x` in the list.

## Zip
When we need to iterate through two or more lists in parallel, we can use the `zip` function.

```python,runnable
courseIds = [2336, 3344]
courseNames = ["Data Structures", "Computer Architecture"]

for courseId, courseName in zip(courseIds, courseNames):
	print (courseId, courseName)
```

```
Output:
2336 Data Structures
3344 Computer Architecture
```