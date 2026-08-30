# The nonlocal Keyword
Consider the following example: we know that there are two *local* variables called "name" here.

```python,runnable
def outer_func():
	# "name" is a local variable
	# attached the the "outer_func" scope.
	name = "General the Jaguar"

	def inner_func():
		# "name" is a local variable
		# attached to the "inner_func" scope
		name = "Rowdy the Roadrunner"

	inner_func()
	print (name)
outer_func()
```

```
Output:
General the Jaguar
```

Let's say we wanted the `inner_func` to modify the `name` variable from the `outer_func` scope instead of creating a new `name` variable.

We can use the `nonlocal` keyword for this:
```python,runnable
def outer_func():
	# "name" is a local variable
	# attached the the "outer_func" scope.
	name = "General the Jaguar"

	def inner_func():
		nonlocal name
		# The variable "name" belongs to
		# the "outer_func" scope.
		name = "Rowdy the Roadrunner"

	inner_func()
	print (name)

outer_func()
```
```
Output:
Rowdy the Roadrunner
```
