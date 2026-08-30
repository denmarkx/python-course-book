# Functions
A function is some reusable block of code that is only run when it is called. Optionally, a function can return some data.

```python,runnable
# Function Definition
def greet():
	print ("Hi there!")

# Function Call
greet()
```

```
Output:
Hi there!
```

## Return
A function can optionally return data. This can be done using the `return` keyword:

```python,runnable
def greet():
	return "Hi there!"

print (greet())
```

```
Output:
Hi there!
```

If a function does not return any data, the return type is a `NoneType`:

```python,runnable
def greet():
	print ("Hi there!")

# Calls the greet() function
# and also prints the return value of greet.
print (greet()) # None
```

```
Output:
Hi there!
None
```

## Parameters and Arguments
Data can be passed into functions as a **parameter**. Parameters are specified after the function name within the parenthesis and separated by a comma.

An **argument** is the term used for the data specified in the call. In the example below, `name` is the parameter and `General the Jaguar` is the argument.

```python,runnable
def greet(name):
	print ("Hello,", name + "!")

greet("General the Jaguar")
```

```
Output:
Hello, General the Jaguar!
```

### Default Parameters
Parameters may be given a default value if no argument is specified.

```python,runnable
def greet(name="General the Jaguar"):
	print ("Hello,", name + "!")

greet()
greet("Rowdy the Roadrunner")

# You can also specify the parameter name explicitly:
greet(name="Rowdy the Roadrunner")
```

```
Output:
Hello, General the Jaguar!
Hello, Rowdy the Roadrunner!
Hello, Rowdy the Roadrunner!
```

Once a default parameter is specified, **all parameters following it must also be given a default value.**
```python,runnable
# Since "name" has a default value, 
# "punctuation" is required to have one as well.
def greet(greeting, name="General the Jaguar", punctuation='!'):
	print (greeting + ',', name + punctuation)

greet("Hello")

# The same goes for when explicitly writing
# the parameter name in the function call:
greet("Hello", name="Rowdy the Roadrunner", punctuation="?")

# Wrong! "punctuation" must be specified
# since "name" is explicitly written here.
# greet("Hello", name="Rowdy the Roadrunner")
```

```
Output:
Hello, General the Jaguar!
Hello, Rowdy the Roadrunner?
```
