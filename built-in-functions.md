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
print("""Use 3 double quotes
to print multiple lines without writing \\n.
F-string interpolation - {} - also works here.""")
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

.

## int()
- 숫자형 자료형을 integer type으로 형변환한다 (e.g float => integer)
- float => integer 의 과정에서, 소수점 이하의 정보는 반올림 없이 유실된다.
    - `print(int(1.8), type(int(1.8)))` => `1 <class 'int'>`  (1.8 => 1)
- 문자열은 integer type으로 형변환할 수 없다.
    - `print(int('abc'))` => this will raise a 'ValueError'

.

## float()
- 숫자형 자료형을 float type으로 형변환한다 (e.g integer => float)
    - `print(float(3))` => `3.0`
- int()와 마찬가지로, 문자열은 float()을 사용할 수 없다 (ValueError 발생)

.

## str()
- 어떤 자료형이든 다 string type으로 형변환한다
    - `print(str(12345), type(str(12345)))`  => `12345 <class 'str'>`

.

## eval()
- 자료형을 함수가 스스로 판단해서 자동으로 맞춰준다.

    - `print(type(eval('1234')))`  =>  `<class 'int'>`
- input()와 함께 사용될 때가 많다.
    - eval() 사용하지 않을 때, input()로 입력 받은 데이터는 디폴트로 string type이 된다.
    - eval() 사용할 때:
    ```python
    >>> input = eval(input("Enter a number: "))
    Enter a number: 1111
    >>> print('input:', input, type(input))
    1111 <class 'int'>
    ```

.

## round()
round(_number_[, _precision(integer)_])

- if _precision_ is not given, round to nearest integer

e.g) `round(2.33333, 2)`  => `2.33`

.

## range()

```python
>>> print(list(range(5)))
[0, 1, 2, 3, 4]

>>> print(list(range(1, 5)))
[1, 2, 3, 4]

>>> print(list(range(1, 10, 2)))  # 3rd parameter : increment
[1, 3, 5, 7, 9]

>>> print(list(range(5, 0, -1)))
[5, 4, 3, 2, 1]
```

.

## enumerate(_iterable_[, start=0])

Returns an enumerate object, after pairing each item with a count number (starting at 0 by default). 

The _iterable_ object must support iteration, i.e. ordered and indexed. E.g. list, tuple, string, etc.

The count number and object item are paired into tuples.

Example)

```python
>>> list_ex = ['a', 'b', 'c', 'd', 'e']
>>> for index, value in enumerate(list_ex):
>>>     print(index, value)
0 a
1 b
2 c
3 d
4 e
```

Example 2) Goal : Returning a new list after deleting the 0th, 4th, and 5th items

```python
colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
fruit = [value for (index, value) in enumerate(colors) if index not in (0, 4, 5)]
print(fruit)        # -> ['Banana', 'Coconut', 'Deli']
```











.

.

# 문자열 내장 함수

(The following functions do __NOT__ modify the original string)

- __len()__: 문자열 길이 반환
- __count()__: 문자열에 있는 특정 문자의 개수를 반환
- __find()__: 특정 문자의 인덱스 번호 반환
- __join()__: 특정 기호를 문자열의 각 아이템 사이에 삽입
- __upper()__: 모든 아이템을 대문자로 변경
- __lower()__: 모든 아이템을 소문자로 변경
- __lstrip()__: 왼쪽으로 공백 (또는 지정 문자) 제거
- __rstrip()__: 오른쪽으로 공백 (또는 지정 문자) 제거
- __strip()__: 앞뒤로 공백 (또는 지정 문자) 제거
- __replace()__: 특정 문자를 새로운 문자로 교체
- __split()__: 특정 문자/기호/값을 기준으로 아이템을 쪼개기

#### len(_str_)

```python
>>> text = 'ABCDEFG'
>>> print(len(text))
7
```

#### _str_.count('_value_')

```python
>>> text = 'Guns, Germs, and Steel'
>>> print(text.count('G'))
2
>>> print(text.count('Guns'))
1
```

#### _str_.find('_value_')

```python
>>> text = 'Guns, Germs, and Steel'
>>> print(text.find('S'))
17
>>> print(text.find('G')) # 여러 개가 존재하는 value라면, first occurring index
0
```

- 여러 개가 존재하는 _value_ 라면, returns the first occurring index

#### _str_.upper() and _str_.lower()

```python
>>> text = 'Guns, Germs, and Steel'
>>> print(text.upper())
GUNS, GERMS, AND STEEL
>>> print(text.lower())
guns, germs, and steel
```

#### _str_.lstrip(), _str_.rstrip(), and _str_.strip()

공백 제거:

```python
>>> text = '    0000Guns, Germs, and Steel0000    '
>>> '|'+text.lstrip()+'|'
'|0000Guns, Germs, and Steel0000    |'
    
>>> '|'+text.rstrip()+'|'
'|    0000Guns, Germs, and Steel0000|'
    
>>> '|'+text.strip()+'|'
'|0000Guns, Germs, and Steel0000|'
```

지정 문자 제거 (괄호 안에 제시된 문자들의 조합을 고려):

```python
>>> text = 'zxxxxz xzxGuns, Germs, and Steelxzx  zzzz'
>>> '|'+text.lstrip('xz ')+'|'
'|Guns, Germs, and Steelxzx  zzzz|'

>>> '|'+text.rstrip('xz ')+'|'
'|zxxxxz xzxGuns, Germs, and Steel|'

>>> '|'+text.strip('xz ')+'|'
'|Guns, Germs, and Steel|'
```

#### _str_.replace('_old_', '_new_')

```python
>>> text = 'Saturday Evening Post'
>>> print(text.replace('Saturday', 'Sunday'))
Sunday Evening Post
```

#### _str_.split(['_value_']) 

- str을 value 기준으로 쪼갠 다음, 리스트 형태로 반환
- If '_value_' is not provided, words are separated by arbitrary strings of whitespace characters

```python
>>> text = 'A-B-C-D'
>>> print(text.split('-'))
['A', 'B', 'C', 'D']
>>> print(type(text.split('-')))
<class 'list'>
```

#### '_value_'.join(_str_)

```python
>>> text = 'ABCDE'
>>> print('-'.join(text))
A-B-C-D-E
```


