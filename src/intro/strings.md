# Strings
Strings are used to store text larger than a single character. They can be surrounded by either single or double quotes.

```python
name = "General the Jaguar"
```

## Membership
We can use the `in` keyword to check if some substring exists within a string:

```python,runnable
name = "General the Jaguar"
print ("Jaguar" in name)
```

```
Output:
True
```

## Concatenation
**Concatenation** is a fancy way of saying "combine". To *concat* two strings, we use the `+` operator.

```python,runnable
first_name = "General"
the = "the"
last_name = "Jaguar"

full_name = first_name + " " + the + " " + last_name
print (full_name)

# ..or:
print ("General" + " the " + "Jaguar")

# Incorrect:
# wrong = "String" + 10
```

```
Output:
General the Jaguar
General the Jaguar
```

## Numbers
We can convert an integer to a string by using the `str()` function:

```python,runnable
x = 10
string = str(x)
print (string + "!")
```

```
Output:
10!
```

..and strings to integers by using `int()`:
```python,runnable
x = "10"
integerX = int(x)
print (int(x))
print (integerX + 1)
```

```
Output:
10
11
```

> [!CAUTION]
> If a string contains an integer (`x = "The number: 5`), you cannot directly do `int(x)`. The same goes for using `str()`.

## Quotation Marks
When writing a string, we wrap them in either single or double quotation marks. When we want to include that character inside the string (such as a quote), there are two approaches to take:
* Convert the outer quotation marks into single or double.
* **Escape** the character using a backslash: (`\`)

```python
# Using single quotation marks to wrap the string:
x = 'This is some sort of "quote".'

# Escaping the quotation marks using the backslash:
x = "This is some sort of \"quote\"."
```

## F-Strings
Formatting-Strings (F-Strings) are used to allow variables directly inside a string. This is done by prefixing the string with `f` and placing the variable inside curly braces (`{}`).

```python,runnable
name = "General the Jaguar"

string = f"My name is {name}!"
print (string)

# ..or:
print (f"My name is {name}!")
```

```
Output:
My name is General the Jaguar!
My name is General the Jaguar!
```

## Indexing and Slicing
### Indexing
Strings are a sequence of characters. Meaning, we can access a specific character by specifying its **index** (position). Indices begin at 0.

```python,runnable
name = "General the Jaguar"
print (name[0]) # G
print (name[1]) # e
```

```
Output:
G
e
```

Negative indices can be used to begin at the end of the string. These begin at -1.
```python,runnable
name = "General the Jaguar"
print (name[-1]) # r
print (name[-2]) # a
```

```
Output:
r
a
```

### Slicing
**Slicing** is used to get a specific "slice" of a string. The syntax for slicing is: `string[start:end:step]` where `end` is non-inclusive.

```python,runnable
name = "General the Jaguar"
print (name[0:7]) # General
print (name[8:11]) # the
print (name[12:18]) # Jaguar

# Stepping:
print (name[::2]) # Every second character
print (name[::-1]) # Reverses the string
```

```
Output:
General
the
Jaguar
GnrlteJga
raugaJ eht lareneG
```

## Common Functions
### split
`split(delimiter)` returns a [list](lat.md) that divides the string at some delimiter:

```python,runnable
x = "comma,separated,string"
print (x.split(',')) # ["comma", "separated", "string"]

x = "space separated string"
print (x.split(' ')) # ["space", "separated", "string"]
```

```
Output:
['comma', 'separated', 'string']
['space', 'separated', 'string']
```

### isdigit
`isdigit` returns True if the entire string contains digits.

```python,runnable
print ("100".isdigit())
```

```
Output:
True
```

### isalpha
`isalpha` returns True if the entire string contains only alphabetic characters.

```python,runnable
print ("Hello".isalpha())
```

```
Output:
True
```

### len
To get the length of the string (starting at 1), we use the `len` function:

```python,runnable
name = "General the Jaguar"
print (len(name))
```
```
Output:
18
```
