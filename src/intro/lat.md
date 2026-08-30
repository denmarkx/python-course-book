# Lists

Lists are a container that can store multiple items (elements).

Create a list by using square brackets and separting its elements by square brackets.

```python,runnable
languages = ["Python", "Java", "C++", "Rust"]
print (languages)
```

```
Output:
['Python', 'Java', 'C++', 'Rust']
```

## "Array"
The term "array" is conflated in Python. In professional settings (ie. an interview), the difference between an array and a list *in Python* can be loosely stated as:

* List: 
    * Standard ordered collection
    * Items can be of different types
    * N-Dimensional
* Array (Standard Library): 
    * Requires importing the `array` module
    * All items must be the same data type
    * Strictly one-dimensional
* Array (numpy):
    * Requires external library: `numpy`
    * Used in Data Science and Machine Learning settings
    * N-Dimensional

Generally speaking, the term "array" and "list" are dependent on the context. However, this course will use them interchangeable unless specified otherwise.

## Accessing Elements
Accessing elements can be done by knowing the **index**. The index is another term for "position".

Consider the list from before:
```python
languages = ["Python", "Java", "C++", "Rust"]
```

The index begins at 0 and increments up as we move to the right. It is always a whole number.

| Element | Index |
| ------- | ----- |
| Python | 0 |
| Java | 1 |
| C++ | 2 |
| Rust | 3 |

To access an element at an index, we use square brackets:
```python
languages = ["Python", "Java", "C++", "Rust"]

print (languages[0]) # Python
print (languages[1]) # Java
print (languages[2]) # C++
print (languages[3]) # Rust
```

## Membership
To check if an item is in a list, we can use the `in` keyword. 

```python,runnable
languages = ["Python", "Java", "C++", "Rust"]

print ("Rust" in languages)
print ("C" not in languages)
```

```
Output:
True
True
```

This can be combined with a conditional statement:

```python,runnable
languages = ["Python", "Java", "C++", "Rust"]

if "Rust" in languages:
    print("Rust is in the languages list.")
```

```
Output:
Rust is in the languages list.
```


## Append, Insert, Remove, Pop

### Append
To add an item to the end of a list, we use the `append` method:
```python,runnable
languages = ["Python", "Java", "C++", "Rust"]

languages.append("C");
print (languages)
```

```
Output:
['Python', 'Java', 'C++', 'Rust', 'C']
```

### Insert
To insert an item at some point in the list, we use the `insert` method and specify the index where the new element will go.

For example, inserting `"C"` in between `C++` and `Rust` would look like this:

```python,runnable
languages = ["Python", "Java", "C++", "Rust"]

# Inserting C after C++ would mean
# placing C at index 3. "Rust" will get pushed back so it stays at the end.

languages.insert(3, "C")
print (languages)
```

```
Output:
['Python', 'Java', 'C++', 'C', 'Rust']
```

### Remove
To remove an item in the list, we use the `remove` method and specify the **value** (not the index):

```python,runnable
languages = ["Python", "Java", "C++", "Rust"]

languages.remove("Java")
print (languages)
```

```
Output:
["Python", "C++", "Rust"]
```

Note: `remove` does not remove duplicates:

```python,runnable
ls = [1, 2, 2, 3]

ls.remove(2)

print(ls) # [1, 2, 3]
```

```
Output:
[1, 2, 3]
```

### Pop
Popping an item from a list does two things:
* Removes the item at the end of the list.
* Returns that item.

```python,runnable
languages = ["Python", "Java", "C++", "Rust"]

removed = languages.pop()
print (removed) # Rust
print (languages)
```

```
Output:
Rust
['Python', 'Java', 'C++']
```

If you don't need what was removed, you can still do `languages.pop()` without assigning it to a variable.

## Common Methods
### Extend
The `extend` method can be used to add all items from another list to the end:

```python
languagesA = ["Python", "Java"]
languagesB = ["C++", "Rust"]

languagesA.extend(languagesB)
```

### Clear
`clear` removes all items.

```python,runnable
languages = ["Python", "Java", "C++", "Rust"]
languages.clear()
print (languages)
```

```
Output:
[]
```

### Count
`count` returns the total number of times an item appears in the list.

```python,runnable
ls = [1, 2, 2, 2, 2, 3, 4]
print (ls.count(2)) # 2 appears 4 times
```

```
Output:
4
```

### Len
`len` returns the total number of items in the list starting at 1.

```python
languages = ["Python", "Java", "C++", "Rust"]
print (len(languages)) # 4
```