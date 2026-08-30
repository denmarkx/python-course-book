# Introduction
## Python Interpreter
When you run a Python program, Python reads the source code and translates it into an intermediate form called **bytecode**.

Afterwards, the **Python Virtual Machine** (PVM) interprets that bytecode, converts it into machine-specific instructions, and executes it.

There are a few different "stages" here, but the primary two to note are:
* **Compile Time**: Python to bytecode.
* **Runtime**: PVM executes the bytecode.

## Statements and Expressions
### Statements
A **statement** is executed to perform some action. Example: `x = 10` is an assignment statement which instructes Python to store 10 in `x`.

### Expressions
An **expression** is evaluated to produce some value. Example: `5 + 5` is an expression where the resulting value is `10`.

### Intersection
Statements can rely on expressions. In the code: `x = 5 + 5`, the entire line here is a statement and `5 + 5` is an expression.

## Code Organization
There are several different nouns to describe the structure of a codebase.

* A **module** is a single Python file.
* A **package** is some directory holding modules.
* A **library** is a collection of packages and modules.