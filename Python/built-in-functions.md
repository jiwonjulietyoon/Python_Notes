# Python Built-in Functions

## Full List of Built-in Functions

https://docs.python.org/3/library/functions.html

- __Input/Output__: print(), input()
- __Math__: abs(), divmod(), max(), min(), pow(), round(), sum()
- __Typecasting/Containers__: bool(), complex(), eval(), float(), int(), str(), dict(), frozenset(), hash(), list(), range(), set(), tuple()
- __Sorting/Pairing__: enumerate(), map(), filter(), zip(), reversed(), sorted()
- __Info__: len(), dir(), help(), id(), type(), isinstance(), issubclass()
- __Char/Num Expression__: ascii(), chr(), ord(), bin(), hex(), oct()
- all()
- any()
- breakpoint()
- bytearray(), bytes()
- callable()
- classmethod(), staticmethod()
- compile()
- delattr(), getattr(), hasattr(), setattr()
- exec()
- format()
- globals(), locals()
- iter()
- memoryview()
- next()
- object()
- open()
- property()
- repr()
- slice()
- super()
- vars()



## print()

##### str vs int

`print('string')`, `print('3')` => str

`print(3)`, `print(3+2)` => int

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

##### Escape Sequence : \

```python
print('Single Quote: \'')  # also works for double quotes
print('Backslash: \\')
print('Line\nBreak')
print('Tab\tTab\tTab')
print('Percent: %d%%' % 100)
```

##### print(*objects, sep=' ', end='\n')

Default: objects are separated with a space and followed by a line break

The following code will result in "Life.is.short!You,need,Python":

```python
print('Life', 'is', 'short', sep='.', end='!')
print('You', 'need', 'Python', sep=',')
```

.

## input(_[prompt]_)

```python
my_input = input('Enter anything here: ')
print('Input is: ', my_input)
```

- Inputs, including plain numbers, are always saved as a 'string' type
- Use `eval()` to automatically convert number inputs into an 'int' type

.

.

## abs(number)

Return absolute value of number (int, float, or complex).

For complex numbers, return the magnitude. 

- e.g) `abs(3 + 4j) == 5.0`

.

## divmod(dividend, divisor)

Return a tuple of (quotient, remainder)

- Both quotient/remainder are integers if the given dividend/divisor are both integers
- Else, both quotient/remainder are float (remainder is not precise)

.

## max(iterable[, key, default])

**[Most Cases]** Without _key_ and _default_, return the maximum value among the given group of iterables. If there are multiple maximum items, return the first one encountered.

**[Setting _Default_]** Specifies which value should be returned when the given iterable is empty. When the given iterable is empty AND no _default_ is provided, a ValueError is raised.

- `max([], default="empty iterable")` ==> `empty iterable`

**[Setting _Key_]** Key function where each iterable item is passed through, and comparison is performed based on the return values

```python
# Example 1 : Find the maximum according to the sum of all digits

def addDigits(num):
    Sum = 0
    while(num):
        Sum += num % 10
        num = num // 10
    return Sum

sample = [111, 9, 23, 55]

max(sample, key=addDigits)  # -> 55
```

```python
# Example 2: Find the maximum according to the dictionary values

sample = {'a': 10, 'b': 20, 'c': 15}

max(sample.items(), key=lambda x: x[1])        # -> ('b', 20)
max(sample.items(), key=lambda x: x[1])[1]     # -> 20
```

.

## pow(base, power[, modulo])

`pow(x, y)` is essentially the same as `x**y`.

- If `x` and/or `y` is a float, or if `y` is a negative integer, the return value will be a float.

`pow(x, y, z)` will give same results as `pow(x, y) % z`, except much more efficient.

- e.g) `pow(2, 3, 5) == 3`

.

## round()

round(_number_[, _precision(integer)_])

- if _precision_ is not given, round to nearest integer

e.g) `round(2.33333, 2)`  => `2.33`

.

## sum(iterable[, additional])

Returns the sum of all values in the _iterable_ and the _additional_ number. Takes at most 2 arguments, INCLUDING _additional_. (_additional_ defaults to 0)

- `sum(3, 4, 5)` will raise a TypeError. `sum((3, 4, 5))` will work.

```python
sample = [1, 2, 3, 4, 5]
sum(sample, 100)          # -> 115
```

.

.

## int()

- 숫자형 자료형을 integer type으로 형변환한다 (e.g float => integer)
- float => integer 의 과정에서, 소수점 이하의 정보는 반올림 없이 유실된다.
  - `print(int(1.8), type(int(1.8)))` => `1 <class 'int'>`  (1.8 => 1)
- 문자열은 integer type으로 형변환할 수 없다.
  - `print(int('abc'))` => this will raise a 'ValueError'
- `int(str, integer)` where `str` consists of digits only and `integer` defaults to `10`
  - => return `int(str)` with `integer` as the base
  - e.g) `int('11111', 2)` => `31`
  - e.g2) `int('00011', 2)` => `3`   (no need to `lstrip` the 0's beforehand)

.

## str()

- 어떤 자료형이든 다 string type으로 형변환한다
  - `print(str(12345), type(str(12345)))`  => `12345 <class 'str'>`

.

## float()

- 숫자형 자료형을 float type으로 형변환한다 (e.g integer => float)
  - `print(float(3))` => `3.0`
- int()와 마찬가지로, 문자열은 float()을 사용할 수 없다 (ValueError 발생)

.

## dict()

##### dict(**kwargs)

- Create a new dictionary out of **kwargs. If there is no argument, create a blank dictionary

##### dict(iterable, **kwargs)

- **iterable**: Each item in the iterable must itself be an iterable with exactly two objects. The first object of each item becomes a key in the new dictionary, and the second object the corresponding value. If a key occurs more than once, the last value for that key becomes the corresponding value in the new dictionary.
- **kwargs**: If keyword arguments are given, the keyword arguments and their values are added to the dictionary created from the positional argument. If a key being added is already present, the value from the keyword argument replaces the value from the positional argument.

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

## bool(x)

Return `True` or `False` based on the value of `x`.

- `0, 0.0, (), [], {}, '', None` will convert to `False`
- All else will convert to `True`

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

.

## enumerate(_iterable_[, start=0])

Returns an enumerate object, after pairing each item with a count number (starting at 0 by default). 

The _iterable_ object must support iteration, i.e. ordered and indexed. E.g. list, tuple, string, etc.

The count number and object item are paired into tuples.

Example 1)

```python
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

Example 2)

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

Example 3) Goal : Returning a new list after deleting the 0th, 4th, and 5th items

```python
colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
fruit = [value for (index, value) in enumerate(colors) if index not in (0, 4, 5)]
print(fruit)        # -> ['Banana', 'Coconut', 'Deli']
```

.

## map(적용할함수, 대상iterable)

- Iterable의 모든 요소에 함수를 적용한 후, map 객체로 반환한다.
- 반환값은 map_object이므로, 최종적으로 사용할 타입으로 형변환해야 한다.

```python
# Task: 아래의 리스트를 문자열 '123'으로 만들기
a = [1, 2, 3]

# Step 1: a의 각 요소를 str 타입으로 형변환하기 (can't join int elements)
a_str = list(map(str, a))
a_str = [str(x) for x in a]  # list comprehension

# Step 2: join
''.join(a_str)
```

사용자 정의 함수도 map으로 적용할 수 있다:

```python
def cube(n):
    return n**3

a = [1, 2, 3]
list(map(cube, a))    # -> [1, 8, 27]

------------
# Note) Using Lambda:
list(map(lambda x: x**3, a))
```

Map은 Lambda와 함께 사용될 때가 많다.

```python
result = map(lambda a: a**2, [3,4,5])
print(list(result))                    # -> [9, 16, 25]
```

.

## zip(*iterables)

##### 복수의 iterable object 들의 요소들을 튜플로 짝지어서 zip object로 반환한다.

```python
num = [1, 2, 3]
alpha = ['A', 'B', 'C']
asc = [65, 66, 67]

list(zip(num, alpha, asc))  # -> [(1, 'A', 65), (2, 'B', 66), (3, 'C', 67)]
```

##### Dictionary - comprehension method에서 zip() 활용하기

```python
{x: y for x in num for y in alpha}  
# -> {1: 'C', 2: 'C', 3: 'C'}
# 이중 for loop -> key는 중복될 수 없으므로, 마지막으로 할당된 value로 덮어씌워진다.

{x: y for x, y in zip(num, alpha)}
# -> {1: 'A', 2: 'B', 3: 'C'}     desired result!
```

##### For loop와 함께 활용했을 때는 enumerate와 비슷한 효과를 낼 수 있다

```python
a = '123'
b = '567'

for digit_a, digit_b in zip(a, b):
    print(digit_a, digit_b)

#-------- Result: ----------
1 5
2 6
3 7
```

##### 사용되는 iterable object들의 길이가 다를 경우, 가장 짧은 것을 기준으로 구성된다.

```python
num1 = [1, 2, 3]
num2 = ['1', '2']
list(zip(num1, num2))     # -> [(1, '1'), (2, '2')]
```

Note) 가장 긴 것을 기준으로 구성하려면:

```python
from itertools import zip_longest
list(zip_longest(num1, num2, fillvalue=0))  # -> [(1, '1'), (2, '2'), (3, 0)]
```

##### Creating a Transposed 2D List

```python
>>> arr = [
>>>     [1, 2, 3, 4, 5],
>>>     [6, 7, 8, 9, 10],
>>>     [11, 12, 13, 14, 15],
>>>     [16, 17, 18, 19, 20],
>>>     [21, 22, 23, 24, 25]
>>> ]
>>> transposed_arr = list(zip(*arr))

>>> transposed_arr
[(1, 6, 11, 16, 21),
 (2, 7, 12, 17, 22),
 (3, 8, 13, 18, 23),
 (4, 9, 14, 19, 24),
 (5, 10, 15, 20, 25)]
```

.

## filter(기준function, iterable)

Iterable의 요소 중 function의 반환 결과가 True인 것들만 모아서 반환한다.

```python
def even(n):
    return not n%2

a = [1, 2, 3, 4]
list(filter(even, a))  # -> [2, 4]

# returns the same results as the following list comprehension methods:
[x for x in [1, 2, 3, 4] if even(x)]
[x for x in [1, 2, 3, 4] if not x%2]
```

.

## sorted(iterable[_, key=None, reverse=True_])

Similar to `max()`.

```python
def addDigits(num):
    Sum = 0
    while(num):
        Sum += num % 10
        num //= 10
    return Sum

sample = [2, 7, 11, 4, 21, 9, 100]

sorted(sample, key=addDigits, reverse=True)
```













## help(_[object]_)

prints help page of _object_

.

## type(_object_)

returns the type of _object_

.



## dir([_object_])

Lists all valid methods/attributes that can be used on the _object_.

When no argument is provided, returns the list of names in the current local scope.







.

.

# 문자열 내장 함수

(The following methods do __NOT__ modify the original string; strings are immutable)

- __len()__: 문자열 길이 반환
- __.count()__: 문자열에 있는 특정 문자의 개수를 반환
- __.find(), .index():__ 특정 문자의 인덱스 번호 반환
- __.join()__: 특정 기호를 문자열의 각 아이템 사이에 삽입
- __.upper()__: 모든 아이템을 대문자로 변경
- __.lower()__: 모든 아이템을 소문자로 변경
- **.capitalize():** capitalizes only the first letter of the string (the rest in lower-case)
- **.title():** capitalizes letters following every apostrophe or whitespace
- **.swapcase():** changes uppercase into lowercase and vice versa
- __.lstrip()__: 왼쪽으로 공백 (또는 지정 문자) 제거
- __.rstrip()__: 오른쪽으로 공백 (또는 지정 문자) 제거
- __.strip()__: 앞뒤로 공백 (또는 지정 문자) 제거
- __.replace()__: 특정 문자를 새로운 문자로 교체
- __.split()__: 특정 문자/기호/값을 기준으로 아이템을 쪼개기
- 확인 메소드 (True/False 반환): `.isaplha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .issuper(), .istitle(), .islower()`

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

- 여러 개가 존재하는 _value_ 라면, returns the first occurring index (_value_의 첫 번째 위치를 반환)
- _index_ 가 없다면 `-1`을 반환
  - c.f) **_str_.index('_value_') :**  _value_의 첫 번째 위치를 반환. 없으면 오류가 뜬다.

#### _str_.upper(), _str_.lower(), _str_.capitalize(), _str_.title(), _str_.swapcase()

```python
>>> text = 'Guns, Germs, and Steel'

>>> print(text.upper())
GUNS, GERMS, AND STEEL

>>> print(text.lower())
guns, germs, and steel

>>> print(text.capitalize())
Guns, germs, and steel

>>> print(text.title())
Guns, Germs, And Steel

>>> print(text.swapcase())
gUNS, gERMS, AND sTEEL
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

#### _str_.replace('_old_', '_new_'[, _count_])

- _count_: number of replacements to perform

```python
>>> text = 'Saturday Evening Post'
>>> print(text.replace('Saturday', 'Sunday'))
Sunday Evening Post
```

```python
>>> text = 'woooooooow'
>>> print(text.replace('o', '', 4))
woooow
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

The argument itself need not be _str_. Could also be a _list_ consisting of string elements only.

```python
>>> text = 'ABCDE'
>>> print('-'.join(text))
A-B-C-D-E
```

.

## 확인 메소드

`.isalpha()`: returns 	true if all characters in the string are alphabetic (no spaces, no digits, etc.) and there is at least one character.

`.isdigit(), .isnumeric(), .isdecimal()`: returns true if all characters in the string are *numbers, and there is at least one character.

- *The difference of the three methods comes from which specific unicode characters are considered "numbers"
- In typical settings, the three methods will return true if the given string is an integer number (not a float)

`.isspace()`: returns true if there are only whitespace characters in the string, and there is at least one character

`.isupper()`: returns true if all letters of the string (thus excluding whitespace and other punctuations) are uppercase

- likewise for `.islower()` and `.istitle()`







