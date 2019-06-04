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



### Declaring Variables (assign with `=`)

- String: `string = "Variable"`   (wrap with single or double quotes)
- Number: `num = 10`
- Declare multiple variables at once: `a, b, c = 10, 20, 'thirty'`
    - Here, the number of objects given on both sides must be the same
    - Values may be provided in either a tuple or list format. The above example can also be written as : `a, b, c = [10, 20, 'thirty']`
- Assign same values to multiple variables: `x = y = z = 10`
    - in this case, id(x), id(y), and id(z) will be identical
- Swapping variable values: `a, b = b, a`
- `type(variable_name)` to check the type of the variable



### Variables are stored in memory spaces

- Each variable is stored in its own space, hence has its own unique address
- Check with `id(variable_name)`

  ```python
  m = 200
  n = 200
  print("id(m):", id(m))  # -> id(m): 4414107808
  print("id(n):", id(n))  # -> id(n): 4414111008
  ```


### 



# Environment Variables

Before pushing codes and/or notes to GitHub, always check if there are any confidential info included, e.g telegram API tokens. Set these as environment variables.

### On Windows (via GitBash)

1. `code ~/.bashrc` => open `.bashrc` (where environment variables are stored) on VSCode

2. Add environment variables (preferably toward the end of the document) in this format:

   - `export TELEGRAM_TOKEN='123456'`
   - `export NAME='Jiwon'`
   - Environment variable names typically use all-caps and underscores
   - No spaces except for the one right after 'export'

3. Save `.bashrc` (on VSCode)

4. (back on GitBash) `source ~/.bashrc`  => apply changes within OS

5. `echo $TELEGRAM_TOKEN` => upon success, this will print whatever data is saved in the environment variable 'TELEGRAM_TOKEN'

6. To access environment variables in Python:

   ```python
   import os
   token = os.getenv('TELEGRAM_TOKEN')
   # where TELEGRAM_TOKEN is an environment variable stored in .bashrc
   ```

### On Windows (cmd창 용)

To store environment variables:

1. win_key + Pause => 고급 시스템 설정
2. => 고급 => 환경 변수 => 시스템 변수 => 새로 만들기 
3. => 저장

### On c9.io (Flask, Django)

1. Use bash terminal.

2. `c9 ~/.bashrc` to open .bashrc file, and append variables at the end of the document

3. Rest of the procedure is identical to that of Windows

##### With Django (via terminal)

1. Deactivate server
2. `c9 ~/.bashrc` to open .bashrc file, and append environment variables at the end of the document (`export ~~='~~'`)
3. `source ~/.bashrc`
   1. this will create a new virtual environment within the current virtual environment
4. `source deactivate`  to break from the additionally created virtual environment

### On Mac OS

Procedures are identical to that of Windows, except:

`.bashrc` ==> `.bash_profile`







