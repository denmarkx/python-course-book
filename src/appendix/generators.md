# Generators
**Generators** are a way to produce elements on-demand (lazily) rather than storing all in memory immediately (eagerly).

Let's compare a generator with a list. Think of a list as a physical book. Every single page is printed and available upfront.

A generator would be more downloading a book page-by-page. The one page you are looking at is currently in memory. When you turn the page, it deletes itself and generates the next one.

Consider the following function below:

```python
def get_list_of_squares(n):
	result = []
	for i in range(n):
		results.append(i ** 2)
	return result
```

`get_list_of_squares` computes and stores everything immediately when called:

```python
list_version = get_list_of_squares(100)
```

A generator uses the `yield` keyword to store what will be used to compute each item in our sequence:

```python
def get_gen_of_squares(n):
    for i in range(n):
        yield i ** 2
```

When we print `list_version`, we get a list of squares. However, when we print the generator version, we get something else:
```python
gen_version = get_gen_of_squares(100)
print (gen_version)
# <generator object gen at 0x10254f760>
```

This is because our values have actually been generated yet! We only have the "recipe" to create them.

Let's look at the memory difference:

```python
import sys

list_version = get_list_of_squares(100)
gen_version = get_gen_of_squares(100)

print (sys.getsizeof(list_version)) # 920 bytes
print (sys.getsizeof(gen_version)) # 104 bytes
```

Our generator only takes ~104 bytes. The list version, however, takes ~920.

To pull values out of our generator, we can iterate through it:

```python
for square in gen_version:
	# Now, we actually materialize each element.
	print (square)
```

Since we have exhausted through our generator, if we run that loop again, nothing will get emitted.
```python
# Looping gen_version again:
for square in gen_version:
	print (square)
# Nothing printed!
```

This is because our generator forgets the value it generates immediately to save memory.

If we ever need to use it again, we can just create the generator again:
`gen = get_gen_of_squares(100)`.