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

## map(사용할함수, 대상리스트)

- 리스트의 각 아이템에 함수를 적용한 후, map 객체로 반환
- 최종적으로 사용한 타입으로 형변환할 필요가 있다

```python
result = map(lambda a: a**2, [3,4,5])
print(list(result))                    # -> [9, 16, 25]
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



























