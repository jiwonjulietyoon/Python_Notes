# Data Type - Numbers (숫자형)

## 	`int` (integers; 정수)

- `type(10)` => `int`

- Maximum integer in Python:

  - ```python
    >>> import sys
    >>> print(sys.maxsize)
    2147483647
    ```

- 2진수: `0b`    //   8진수: `0o`     //   16진수: `0x` 

  - ```python
    >>> print(0b10) # binary
    2
    >>> print(0o10) # octal
    8
    >>> print(10) # decimal
    10
    >>> print(0x10) # hexadecimal
    16
    ```

.

## `float` (부동소수점, 실수)

- `type(1.5)`, `type(-3.0)` => both are `float`

- `2.5e10 == 2.5 X 10^10 == 25000000000.0`

- 코딩 내에서 최대한 소수점 실수를 사용하지 않도록 하는 게 바람직하다.

  - Due to a 'floating point rounding error' -- 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않는다
  - => floating point numbers cannot be expressed accurately
    - More on this: https://floating-point-gui.de/basic/

- Bending around the floating point rounding error:

  1. Comparing the absolute value

     ```python
     >>> a = 0.1
     >>> b = 0.3
     >>> abs(a*3 - b) < 1e-10
     True
     # abs(a*3 - b) == 5.551115123125783e-17
     ```

  2. Comparing the absolute value to the float epsilon value

     ```python
     >>> import sys
     >>> abs(a*3-b) <= sys.float_info.epsilon
     True
     ```

  3. Using the math module

     ```python
     >>> import math
     >>> math.isclose(a*3, b)
     True
     ```

.

## `complex` numbers (복소수)

복소수는 허수부를 `j`로 표현한다.

```python
>>> a = 3 - 4j
>>> type(a)
complex
>>> a.real
3.0
>>> a.imag
-4.0
>>> a.conjugate
<built-in method conjugate of complex object at 0x05602C80>
```

.

# Boolean: True or False

- 비교/논리 연산 등에 주로 활용
  - 다음은  `False`로 변환된다: `0, 0.0, (), [], {}, '', None`
  - All else will convert to `True`

.

# None Type

.

.

# Operators (연산자 - 숫자형)

## 산술연산자 : 숫자 계산을 위한 문법 기호 

==> `+, -, *, /, //, %, **`

##### Addition  `+` , Subtraction  `-` 

```python
type(1+2)        # int   +/- int   = int
type(1.1-2.2)    # float +/- float = float
type(1+2.0)      # int   +/- float = float
```

##### Multiplication `*`

```python
type(2*3)       # int * int   = int
type(2*3.0)     # int * float = float
```

##### Division `/`

```python
type(9/3)       # 9/3 ==> 3.0
type(5/3)       # int / int = float (always, regardless of result)
```

##### Quotient `//`

- returns the largest integer smaller than the division result

  ```python
  print(5//3)      # 5/3 = 1.6667  => 1
  print(-3//4)     # -3/4 = -0.75  => -1
  ```

##### Remainder `%`

```python
print(5%3)   # 5 / 3 = 1 ... 2
```

##### Power `**` (equivalent to '^')

```python
>>> print(2**3, type(2**3))    
8 <class 'int'>                    # int ** int = <class 'int'>

>>> print(3**2, type(3**2))
9 <class 'int'>

>>> print(9**0.5, type(9**0.5)) 
3.0 <class 'float'>                # int ** float = <class 'float'>

>>> print(27**(1/3), type(27**(1/3)))
3.0 <class 'float'>

>>> print(-1**4, (-1)**4)          # operation order: () > **
-1 1
```

##### divmod(_dividend_, _divisor_)

```python
>>> print(divmod(7, 3))
(2, 1)

>>> quotient, remainder = divmod(7, 3)
>>> print(f"Quotient is {quotient}; remainder is {remainder}")
Quotient is 2; remainder is 1
```

.

## 비교 연산자

- ==> `==, !=, <=, >=, <, >`
- compares __VALUES__ of two items (does __not__ compare data type)
- output: Boolean (True or False)

```python
>>> print(1 == 1.0)
True
>>> print(1 != 1.0)
False
```

.

## 논리 연산자 

- ==> `and, or`

##### and

```python
print(True and True)   # -> True
print(10>9 and 1>0)    # -> True
```

##### or

```python
print(True or False)   # -> True
print(10<9 or 1<0)     # -> False
```

.

## 복합 연산자 (할당 연산자)

- ==> `+=, -=, *=, /=, //=, %=, **=`

example) `**=`

```python
>>> number = 5
>>> number **= 2
>>> print(number)
25
```

Note) `+=` and `*=` are also supported for string types

```python
>>> plus = 'abcd'
>>> plus += 'e'
>>> print(plus)
abcde

>>> times = 'abcd'
>>> times *= 3
>>> print(times)
abcdabcdabcd
```

.

.

# Operators (연산자 - 문자형)

## 산술 연산자: Concatenate or Repeat

##### string + string

```python
print('one'+'two')     # -> onetwo    (no space)
print('one', 'two')    # -> one two   (automatically spaced)
```

##### string * int

```python
print('repeat'*3)      # repeatrepeatrepeat
```

.

## 비교 연산자: 문자의 크기를 비교 (ASCII code)

```python
print('a' > 'A')         # True
print('a' > 'z')         # False
print('Z' > 'a')         # False
print('apple' > 'applE') # True
print('apple' > 'appl')  # True
print('apple' > 'appla') # True
```

.

## in 연산자 : Containment Test

`'a' in 'apple'` => `True`

`5 in range(5)` => `False`

.

## `==` operator vs `is` operator

While `==` tests if two variables have the same __value__, `is` tests if the two variables point to the same __object__ (i.e. whether they are stored at the exact same memory location).

Ex 1) `x` and `y` are two separate lists that happen to have the same values:

```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)       # -> True
print(x is y)       # -> False
print(id(x), id(y)) # -> 90343744 92716328 (different identifiers)
```

Ex 2) `a` and `b` are both assigned to the same object:

```python
a = b = [1, 2, 3]
print(a == b)       # -> True
print(a is b)       # -> True
print(id(a), id(b)) # -> 90344984 90344984 (same memory locations)
```

.

## Order of Operators

1. `( )` Parentheses
2. Slicing
3. Indexing
4. `**` 제곱연산자
5. `+, -`  단항연산자 & 음수/양수 부호
6. `*, /, %` 산술연산자
7. `+, -` 산술연산자
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `or`

.

.

# Type Conversion (Typecasting)

## Implicit Type Conversion (암시적)

사용자가 의도하지 않았으나, 파이썬 내부적으로 자동으로 형변환 되는 경우

Examples)

- `True + 3` => `4`  (`True` is converted into `1`, an int type, so as to perform the addition)

- ```python
  num_int = 3
  num_float = 5.0
  num_complex = 1 + 2j
  print(type(num_int + num_float))     # -> <class 'float'>
  print(type(num_int + num_complex))   # -> <class 'complex'>
  ```

## Explicit Type Conversion (명시적)

Use built-in-functions such as `int()`, `float()`, `str()`

(see section under 'built-in functions')

.

.





















//