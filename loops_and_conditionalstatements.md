# Conditional Statements

## if ... elif ... else

##### syntax: `if`/`elif` + _condition_  , where _condition_ is a Boolean

```python
if True:
    print('True')        # -> True

if False:
    print('False')
      
if 1:
    print('1 = True')    # -> 1 = True

if 2:
    print('2 = True')    # -> 2 = True
    
if 0:
    print('0 = True')

if 'a':
    print('a = True')    # -> a = True
```

- _condition_ can include `and`, `or`, `in`, `not`, etc.

##### 'pass' means do nothing

```python
>>> if 1 > 2:
>>>     pass
>>> else:
>>>     print('Pass means do nothing')
Pass means do nothing
```

.

## short-hand version

=> _valueWhenTrue_ if _condition_ else _valueWhenFalse_

타 언어의 삼항 연산자와 동일하다

```python
>>> num = 5
>>> print('num > 5') if num > 5 else print('num <= 5')
num <= 5
```

```python
>>> userinput = int(input("Enter integer: "))
>>> positivevalue = userinput if userinput > 0 else 0
>>> print(positivevalue)
# (5 -> 5  /  -3 -> 0)
```

.

.

# while loop

조건식이 True인 경우 반복적으로 코드를 실행한다. 

따라서 반드시 종료조건을 설정해주어야 한다. (Or else, will result in an infinite loop)

##### break, continue

.

.

# for loop

##### for loops and dictionaries

for `dict1 = {'A': 65, 'B': 66, 'C': 67}`   :

```python
>>> for key in dict1:
>>>     print('key: ', key)
>>>     print('value: ', dict1[key])
key:  A
value:  65
key:  B
value:  66
key:  C
value:  67
```

```python
>>> print(dict1.items())
>>> for key, val in dict1.items():
>>>     print('key: ', key)
>>>     print('value: ', val)
dict_items([('A', 65), ('B', 66), ('C', 67)])
key:  A
value:  65
key:  B
value:  66
key:  C
value:  67
```

##### for loops and 다차원 리스트

```python
>>> a = [(1, (2.1, 2.2), 3), 
>>>      (10, 20, 30), 
>>>      (100, 200, 300)]

>>> for num in a:
>>>     print(num)    # 1차원 아이템 출력
(1, (2.1, 2.2), 3)
(10, 20, 30)
(100, 200, 300)

>>> for first, second, third in a:
>>>     print('first:', first)
>>>     print('second:', second) # argument 'third' is not used
first: 1
second: (2.1, 2.2) 
first: 10
second: 20 
first: 100
second: 200
# 3 arguments (first, second, third) : the length of each and every item in the list must also be '3'
```





























