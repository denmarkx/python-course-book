# Nested Functions
In Python, a function can be defined within a function. An inner function is only accessible within the function that contains it.

```python,runnable
def outer(message):
	# Nested function:
	def inner():
		print (message)

	# Call inner function.
	inner()

# Call outer function.
outer("Hi there!")

"""
Since the inner function is defined
within the outer function, we cannot
call it outside of the function.
"""
# inner() # Error!
```

```
Output:
Hi there!
```

## Closure
A **closure** is a function that remembers and keeps access to the variables from the outer scope, even after the outer function is done.

```python,runnable
def power(exponent):
	def calculate(base):
		# Remembers the "exponent" variable
		# from the outer function.
		return base ** exponent

	# Returns the function: "calculate".
	# This does NOT call the calculate function.
	return calculate

# Returns the "calculate" function where
# "exponent" is remembered as 2.
square = power(2)

# Returns the "calculate" function where
# "exponent" is remembered as 3.
cube = power(3)

print(square(4))
print(cube(4))
```
```
Output:
16
64
```
