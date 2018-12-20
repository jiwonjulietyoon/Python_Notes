# Python Variables

### Rules of Thumb for Variable Names

- Each variable must have a unique name
- Begin with an alphabet or _(underscore) - may not begin with a number
- Normally use lowercase letters, numbers, and underscores (no spaces in between)
- May not use reserved keywords such as built-in functions, identifiers, modules, etc.



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





