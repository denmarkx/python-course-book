# Input and Output
## Output

To write some output to the terminal, we use the function `print`. Internally, `print` will append a newline character \n signifying that the line has ended.

To print some text without a newline, we use `print(<message>, end='')`.

```python,runnable
print ("Hello ", end="")
print ("World!")
```

```
Output:
Hello World!
```

## Formatting
To format some value in a string, we can use a **format specifier**. The basic syntax for format specifiers is:

```
[[fill][align]][width][.precision][type]
```

..although there are [several other options](https://docs.python.org/3/library/string.html#format-specification-mini-language).

Common values for `type` are the following:
| Specifier | Type |
| --------- | ---- |
| `s` | String |
| `d` | Decimal |
| `f` | Float |
| `b` | Binary |
| `x` | Hexadecimal |
| `o` | Octal
| `e` | Scientific Notation |
| `%` | Percentage |

Values for `align` are:
| Value | Alignment |
| ----- | --------- |
| `<` | Left |
| `>` | Right |
| `^` | Center |

The `width` is the total number of characters that the portion of the string will contain.

The `precision` determines the number of digits to the right of the decimal point. Additionally, it can be used for the maximum amount of characters of a string.

### Formatting Alternatives
Over time, Python has had numerous ways to use this format specifiers. For example: **f-strings**, **%-formatting**, and **.format**. 

The following example shows three ways of performing the same thing:
```python,runnable
import math

print(f"{math.pi:+012.4f}")
print("%+012.4f" % math.pi)
print("{:+012.4f}".format(math.pi))
```

```
Output:
+000003.1416
+000003.1416
+000003.1416
```

### Example
```python,runnable
import math

print(math.pi)
print(f"{math.pi:.2f}")
print(f"{math.pi:.4f}")
print(f"{math.pi:.10f}")
print(f"{math.pi:.2e}")
print(f"{math.pi:.4e}")
print(f"{math.pi:010.2f}")
print(f"{math.pi:>10.2f}")
print(f"{math.pi:<10.2f}")
print(f"{math.pi:^10.2f}")
print(f"{math.pi:+.2f}")
print(f"{math.pi:>12.3f}")
print(f"{math.pi:<12.3f}")
print(f"{math.pi:^12.3f}")
```

```
Output:
3.141592653589793
3.14
3.1416
3.1415926536
3.14e+00
3.1416e+00
0000003.14
      3.14
3.14      
   3.14   
+3.14
       3.142
3.142       
   3.142    
```

### Breakdown
```python,runnable
import math
print(f"{math.pi:+012.4f}")
```

```
Output:
+000003.1416
```

We can breakdown the pattern `+012.4f` as so:
```
+ 0 12 .4 f
│ │ │  │  │
│ │ │  │  └── floating-point notation
│ │ │  └───── 4 digits after the decimal
│ │ └──────── minimum width of 12 characters
│ └────────── pad with zeros
└──────────── show + for positive numbers
```

## Input
To accept input from the console, we can use the `input(<message>)` function:

```python,runnable
message = input("Please enter your name: ")
print("Your name is:", message)
```

```
Output:
Please enter your name: General the Jaguar
Your name is: General the Jaguar
```

Anything we receive from `input()` will always be a `str` type.
```python
number = input("Please enter a number: ")

# Since <number> is a string, we CANNOT perform mathematical operations.
# number + 5 : <str> + <int>
```

Thus, we must convert the string to some other value via type casting:
```python,runnable
number = int(input("Please enter a number: "))
numberSquared = number ** 2
print ("Number squared is:", numberSquared)
```

```
Output:
Please enter a number: 5
Number squared is: 25
```