# Scope and Globals
The area in which we define variables is referred to as the **scope**. Scope is the area where we place "code blocks" in the indented portion following a colon (`:`).

Once a variable reaches the end of the scope it's in, the variable can no longer be used. The duration of a variable being considered valid for use is called its **lifetime**.

For example:
```python
def greet(): # "greet" scope start
	name = "General the Jaguar"
	print (name)
	# "greet" scope end

# The variable "name" cannot be used here.
# We would have to define it again.
```

## Global Variables
Variables that are created outside of a function are **global variables**.

```python
# "name" is a global variable.
name = "General the Jaguar"
def greet():
	print (name)
```

We can create a variable with the same name as a global variable inside a function. The global variable will retain its original value. The new variable will be local to the function (function-local):
```python,runnable
# "name" is a global variable.
name = "General the Jaguar"

def greet():
	# "name" is a local variable.
	name = "Rowdy the Roadrunner"
	print (name)

print (name)
```

```
Output:
General the Jaguar
```

## global
We can define a global variable inside a function using the `global` keyword.
```python,runnable
def greet():
	global name
	name = "General the Jaguar"
	print (name)

greet()

# Since "name" is a global variable, we can use it
# outside of the "greet" function scope:
print(name)
```

```
Output:
General the Jaguar
General the Jaguar
```

If we want to change the value of a global variable inside a function, we can also use the `global` keyword:
```python,runnable
name = "General the Jaguar"

def greet():
	global name
	name = "Rowdy the Roadrunner"
	print (name)

print (name)
greet()
print (name)
```
```
Output:
General the Jaguar
Rowdy the Roadrunner
Rowdy the Roadrunner
```
