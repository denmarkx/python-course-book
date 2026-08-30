# Tuples

Tuples are a container that can store multiple items (elements). The difference between tuples and lists are that tuples are **immutable**: you cannot add or remove items after the tuple has been created.

Create a tuple by using parenthesis and separting its elements by a comma:

```python,runnable
languages = ("Python", "Java", "C++", "Rust")
print (languages)
```

```
Output:
('Python', 'Java', 'C++', 'Rust')
```

Creating a tuple with just one element requires placing a comma at the end of the element sequence:

```python,runnable
wrong = ("Python")
print (wrong) # This is a string.

correct = ("Python",)
print (correct) # This is a tuple.
```

```
Output:
Python
('Python',)
```

## Why?
We use lists to serve as a container for data that changes over time. Tuples on the other hand, act as fixed records. Tuples also take a less amount of memory.

If you want a container that is read-only, contains duplicates, and a fixed size, use tuples.

## Accessing Elements
Similar to lists, a tuple can be accessed by square brackets (`[]`) and the index.

```python,runnable
languages = ("Python", "Java", "C++", "Rust")

print (languages[0]) # Python
print (languages[1]) # Java
print (languages[2]) # C++
print (languages[3]) # Rust
```

```
Output:
Python
Java
C++
Rust
```

## Element Assignment
Since tuples are read-only, you cannot change the inner contents. This will yield an error:

```python,runnable
languages = ("Python", "Java", "C++", "Rust")

# Error!
languages[1] = "Kotlin"
```

```
Output:
TypeError: 'tuple' object does not support item assignment
```

## Common Methods and Functions
Since tuples are immutable, there are only just a few methods and functions.

### Count
`count` returns how many times an item appears.

```python,runnable
nums = (1, 2, 2, 2, 2, 3, 4)
print (nums.count(2)) # 2 appears 4 times
```

```
Output:
4
```

### Len
`len` returns the size of the tuple.

```python,runnable
languages = ("Python", "Java", "C++", "Rust")
print (len(languages))
```
```
Output:
4
```
