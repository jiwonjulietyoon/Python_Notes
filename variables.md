# Python Variables

### Rules of Thumb for Variable Names (식별자)

- Each variable must have a unique name
- Begin with an alphabet or _(underscore) - may not begin with a number
- Normally use lowercase letters, numbers, and underscores (no spaces in between)
- May not use reserved keywords as well as built-in functions, identifiers, modules, etc.
    - List of reserved keywords:
    ```python
    >>> import keyword
    >>> print(keyword.kwlist)
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    ```
    - Using reserved keywords as a variable name will not automatically raise an error. However, doing so will result in newly defining the reserved keyword, thus not being able to make use of the keyword's original functionality.
    - To cancel/delete variables, use: `del variable_name`



### Declaring Variables

- String: `string = "Variable"`   (wrap with single or double quotes)
- Number: `num = 10`
- Declare multiple variables at once: `a, b, c = 10, 20, 'thirty'`
- Declare multiple variables with same value: `x = y = z = 10`



### Variables are stored in memory spaces

- Each variable is stored in its own space, hence has its own unique address

  ```python
  m = 200
  n = 200
  print("id(m):", id(m))  # -> id(m): 4414107808
  print("id(n):", id(n))  # -> id(n): 4414111008
  ```


### Other

- Swapping variable values: `a, b = b, a`





