# Various functions

Argument (O), Return Value (O)

```python
def get_sum(a, b, c):
    return a+b+c

print(get_sum(1,2,3))        # -> 6
```

Argument (X), Return Value (X)

```python
def my_print():
    print('Hello World')
    
my_print()                   # -> Hello World
```

Argument (O), Return Value (X)

```python
def print_sum(a, b, c):
    print('sum:', a+b+c)

print_sum(1,2,3)             # -> sum: 6
```

Argument (X), Return Value (O)

```python
def always_returns_Hi():
    return 'Hi'

print(always_returns_Hi())   # -> Hi
```

.

# Docstring
```python
>>> def mysum(a, b):
>>>     """Comments on this function
>>>     The docstring should describe what the function does, not how.
>>>     Docstrings can be accessed by the __doc__ attribute on objects."""

>>> print(mysum.__doc__)
Comments on this function
    The docstring should describe what the function does, not how.
    Docstrings can be accessed by the __doc__ attribute on objects.
```

.

# Passing arguments

Example) Simple function that prints the sum of 3 arguments (default argument values)

```python
>>> def print_sum(a=1, b=2, c=3):
>>>     print(f'sum: {a + b + c:2} // a: {a:2}, b: {b:2}, c:{c:2}')
>>> 
>>> print_sum()
sum:  6 // a:  1, b:  2, c: 3
>>> 
>>> print_sum(10)
sum: 15 // a: 10, b:  2, c: 3
>>>                 
>>> print_sum(10, 20)
sum: 33 // a: 10, b: 20, c: 3
>>>                 
>>> print_sum(b=55, c=12, a=8)
sum: 75 // a:  8, b: 55, c:12
```

.

## `*args` : arbitrary number of arguments to pass

Insert an asterisk in front of the parameter (parameter name need not be `args`)

```python
def get_sum_args(*args):
    Sum = 0
    for x in args:
        Sum += x
    return Sum

print(get_sum_args(1,2,3,4,5))     # -> 15
```

Parameters may be a combination of fixed-length and variable-length arguments

```python
def calc(a, *b):
    if a == '+':
        res = 0
        for x in b:
            res += x
    elif a == '*':
        res = 1
        for x in b:
            res *= x
    print(f'[{a}]', res)

calc('+', 10, 20, 30)          # -> [+] 60
calc('*', 4, 5, 6)             # -> [*] 120
```

.

## `**kwargs`: keyword arguments (딕셔너리 형태로 저장됨)

`**kwargs` is converted into a dictionary

```python
>>> def test(**kwargs):
>>>     return kwargs
>>> print(test(name='Kim', age=20))
{'name': 'Kim', 'age': 20}
```

```python
>>> def my_fake_dict(**kwargs):
>>>     result = []
>>>     for x in kwargs:
>>>         result.append(f'{x}: {kwargs[x]}')
>>>     print(', '.join(result))
>>> my_fake_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag')
한국어: 안녕, 영어: hi, 독일어: Guten Tag
```



Using `*args` and `**kwargs`:

```python
>>> def my_func(*num, **time):
>>>     Sum = 0
>>>     for x in num:
>>>         Sum += x
>>>     print('sum of num:', Sum)
>>>     print('time:', time)
>>> 
>>> my_func(1,2,3, day='Sat', date='Dec 15')
sum of num: 6
time: {'day': 'Sat', 'date': 'Dec 15'}
```

```python
>>> def my_func2(*num, **time):
>>>     return time.keys()
>>> print(my_func2(1,2,3, day='Sat', date='Dec 15'))
dict_keys(['day', 'date'])
```

.

## Multiple return values are combined into a tuple

```python
>>> def sum_product(a, b):
>>>     return a+b, a*b
>>> print(sum_product(3,4))
(7, 12)

>>> s, p = sum_product(4,5)
>>> print('sum:', s)
sum: 9
>>> print('product:', p)
product: 20
```

##### `_`: ignore value

```python
>>> def calculate(a,b):
>>>     v1 = a+b
>>>     v2 = a*b
>>>     v3 = a-b
>>>     v4 = a/b
>>>     return v1, v2, v3, v4

>>> _, prod, diff, _ = calculate(6,4)
>>> print('product:', prod)
product: 24
>>> print('difference:', diff)
difference: 2
```

Note) 한 함수 내에서 `return`을 여러 번 쓸 경우, 에러는 나지 않지만 처음으로 쓴 `return`값만 실제로 반환된다.

.

## Lambda

간결한 함수의 정의 (익명 함수)

```python
lambda_ex = lambda a: a**2
lambda_ex(4)                # -> 16
```

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

.

## High Order Function

##### 함수 복제하기

```python
def my_func(a, b):
    print(a+b)

res2 = my_func

print(res2)         # -> <function my_func at 0x00909DF8>
print(my_func)      # -> <function my_func at 0x00909DF8>
```

- `res2` and `my_func` point to the same function

- `res2` now functions exactly the same as `my_func`

##### 함수를 다른 함수의 인자로 전달하기

```python
from operator import add, mul

jiwook = add
nayoung = mul

def dowoo(func, num1, num2):
    return func(num1, num2)

dowoo(jiwook, 20, 20)    # -> 40
dowoo(nayoung, 3, 4)     # -> 12
```



























