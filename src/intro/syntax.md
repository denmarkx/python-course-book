# Syntax
Unlike other languages, Python does not require a `main` function. You'll often see programmers using an idiom that looks like this:

```python
def main():
	# ...

if __name__ == "__main__":
	main()
```

If we were to write this to a file, name it `Example.py`, and run it using `python Example.py`, Python will automatically set `__name__` as `__main__`.

# Comments
Comments are pieces within the code that do not run and are meant to serve as explanatory text.

## Single-line Comments
Single-line comments can be done using `#`.

```python
# This is a comment.
```

## Multi-line Comments
Multi-line comments begin with three quotation marks and end with three quotation marks. Any text in between will be treated as a comment.

```python
"""
This is a
multi-line comment.
"""
```