# Unpacking

## Argument Unpacking
Given some iterable, such as a list or tuple, we can expand each item into individual arguments when calling the function. This can be done with an asterisk (`*`).

For example, consider a function with parameters `length`, `width`, `height`.
```python,runnable
def volume(length, width, height):
	return length * width * height

# We could call as normal:
print (volume(5, 10, 15))

# ..but let's say we have a list (or tuple):
nums = (5, 10, 15)

# We can use an asterisk to expand each item in our
# list and have them correspond to length, width, and height. 
print (volume(*nums))
```

```
Output:
750
750
```

## Return Value Unpacking
We can unpack the return value of a function into single variables. This does NOT use the asterisk:

```python,runnable
def get_volume():
	# Python automatically turns this into a tuple:
	# (5, 10, 15)
	return 5, 10, 15

# Since we return 3 values, we can assign each to its own variable:
length, width, height = get_volume()
print (length, width, height)
```

```
Output:
5 10 15
```

## Nested Unpacking
Let's say we have a function that returns an string and a tuple:

```python,runnable
def get_mascot():
	return "TAMUSA", ("General the Jaguar", "Jaguar")

# We can mirror the structure of the return value:
university, (name, species) = get_mascot()
print (university)
print (name)
print (species)
```

```
Output:
TAMUSA
General the Jaguar
Jaguar
```
