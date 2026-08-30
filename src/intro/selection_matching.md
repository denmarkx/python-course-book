# Matching
> [!IMPORTANT]
> This is a feature is only applicable to Python 3.10+.

Consider the example from the "If and Else" section:

```python,runnable
grade = 'B'

if grade == 'A':
	print ("Awesome!")
elif grade == 'B':
	print ("Cool!")
elif grade == 'C':
	print ("Fair..")
else:
	print ("Oh no!")
```

```
Output:
Cool!
```

Instead of having several if and else statements, we can use a `match` statement and break down grade letters A, B, C into "cases" using the `case` keyword.

Before writing the full thing, let's look at when the grade letter is A or if it is NOT A, B, or C.

```python,runnable
grade = 'A'
match grade:
	# Equivalent to: if grade == 'A'
	case 'A':
		# ..then
		print ("Awesome!")

	# Equivalent to else.
	case _:
		print ("Oh no!")
```

```
Output:
Awesome!
```

Knowing the syntax, we can write our full matching code:
```python,runnable
grade = 'C'
match grade:
	# Equivalent to: if grade == 'A'
	case 'A':
		## ..then
		print ("Awesome!")

	case 'B':
		print ("Cool!")

	case 'C':
		print ("Fair..")

	# Equivalent to else.
	case _:
		print ("Oh no!")
```

```
Output:
Fair..
```
