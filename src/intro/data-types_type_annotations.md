# Type Annotations
**Type Annotations** is an optional syntax used to describe the data type of some variable, parameter, or return value. Since Python is dynamically typed, these are not strictly enforced at runtime.

Variables can be annotated by using a colon (`:`) followed by the data type.

```python
x : int = 20
name : str = "General the Jaguar"
```

Function parameters and return types can also be annotated:
```python
def greet(name : str) -> str:
	return name
```
