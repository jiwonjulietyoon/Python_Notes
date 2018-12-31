# Python Built-in Functions

## print()

##### str vs int

`print('string')`, `print('3')` => str

`print(3)`, `print(3+2)` => int

.

##### Multiple entries/objects

`print('Multiple' 'Entries' 'WITHOUT' 'Commas')` => No spaces btw entries

`print('Multiple', 'Entries', 'WITH', 'Commas')` => 1 space for each comma

`print(2, 3)` works, but `print(2 3)` leads to a SyntaxError (missing comma)

`print('Python',123,'Comma')` => str + int combination is also possible

+) Multiple lines within a single print function:

```python
print('''Use 3 single (or double) quotes
to print multiple lines without writing \\n''')
```

+) Multiple print functions in a single line are joined with a semicolon: `print('Line 1'); print('Line 2')`

.

##### Escape Sequence : \

```python
print('Single Quote: \'')  # also works for double quotes
print('Backslash: \\')
print('Line\nBreak')
print('Tab\tTab\tTab')
print('Percent: %d%%' % 100)
```

.

##### print(*objects, sep=' ', end='\n')

Default: objects are separated with a space and followed by a line break

The following code will result in "Life.is.short!You,need,Python":

```python
print('Life', 'is', 'short', sep='.', end='!')
print('You', 'need', 'Python', sep=',')
```

.

## help(_[object]_)

prints help page of _object_

.

## type(_object_)

returns the type of _object_

.

## input(_[prompt]_)

```python
my_input = input('Enter anything here: ')
print('Input is: ', my_input)
```

- Inputs, including plain numbers, are always saved as a 'string' type
- Use `eval()` to automatically convert number inputs into an 'int' type

