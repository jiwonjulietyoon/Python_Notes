# Python notes to be categorized later..





## - Opening a webbrowser

```python
import webbrowser
webbrowser.open('some_url.com')
# c.f webbrowser.open_new(), webbrowser.open_new_tab()
```



## - Random Sampling

```python
import random

random.sample(target_list, 5)   # randomly select multiple items
random.choice(target_list)     # randomly select one
```





## - Renaming multiple files

```python
import os

print(os.listdir('.'))   #ls
os.chdir(r'C:\Users\student\chatbot\day1\list')   #cd
print(os.getcwd())   #pwd
# print(os.listdir('.'))   #ls

##### prepend "SSAFY_" 
for x in os.listdir('.'):
    os.rename(x, 'SSAFY_'+x)

##### get rid of the prepended "SSAFY_"    
for x in os.listdir('.'):
    os.rename(x, x[6:])
```





### - Dictionary Method: get('key')

python dictionary: `dict.get('key')`

- if key exists, return the value that corresponds to the 'key'
  - same results as `dict['key'`]
- if key does not exist, return 'None' (+ don't raise an error)

.

### - Pretty Print (pprint)

`from pprint import pprint as pp`

```python
url = f"https://api.telegram.org/{token}/getUpdates"
response = requests.get(url)
doc = response.json()
pp(doc)  # -> will print 'doc' in a relatively more legible JSON format
```

.

## - Faker

```python
from faker import Faker
fake = Faker()

print(fake.name())
print(fake.job())
print(fake.address())
```

.

## Comments - Function

```python
>>> def mysum(a, b):
>>>    """Comments on this function"""

>>> mysum.__doc__
'Comments on this function'
```

.

## Encoding

The following line must be added as the __first__ line of the file:

`# -*- coding: encoding -*-`

where _encoding_ is one of the valid codecs supported by Python

.

## Breaking up a single command into multiple lines:

Insert a backslash(`\`) before hitting 'enter'

ex)

```python
a = 0
if a \  # backslash
== 0:
    print('a == 0')
```

- 단, `[]` `{}` `()` 는 `\` 없이도 여러 줄에 나누어 쓰는 것이 가능하다

```python
list_a = ['A', 'B',
        'C', 'D']
```

.

## datetime

```python
>>> import datetime
>>> today = datetime.datetime.now()
>>> print(today)
2019-01-02 12:38:23.704796
>>> print(f"Today is {today:%y}.{today:%m}.{today:%d}. / {today:%A}, {today:%b} {today:%d}, {today:%Y}")
Today is 19.01.02. / Wednesday, Jan 02, 2019
```

.

## dir(_object_)

Lists all methods that can be used on the _object_

.



## 복사: shallow copy vs deep copy

관건: Is the object mutable or immutable?

- mutable: list, dictionary
  - different from cloning! points to the same object. thus the original object can and will be altered when the secondary variable/pointer is altered.
- immutable: string, int, tuple
  - copied/cloned (복제). the original object cannot by altered

##### mutable

```python
mut = [1, 2, 3]
mut2 = mut

mut2[0] = 100

print("mut:", mut)     # -> mut: [100, 2, 3]
print("mut2:", mut2)   # -> mut2: [100, 2, 3]
print(mut is mut2)     # -> True
print("mut id", id(mut), "mut2 id", id(mut2))  # -> mut id 5705040 mut2 id 5705040


# thus, 
original_list = [1, 2, 3]
new_list = original_list   
# -> 'new_list' is a misnomer, as 'new_list' is NOT a mere copy of 'original_list'.
# 'new_list' and 'original_list' both refer to the exact same list, '[1, 2, 3]'
# to make a copy of lists,
new_list = original_list[:]
# or,
new_list = list(original_list) # not preferred, as list() is also used for type casting.

# the same goes for Python dictionaries
```

##### immutable

```python
immut = 13      # int : immutable
immut2 = immut  # immut2 is an actual copy of immut

immut2 = 12

print("immut:", immut)     # -> 13 (original is not modified)
print("immut2:", immut2)   # -> 12
print(immut is immut2)     # -> False
print("immut id", id(immut), "immut2 id", id(immut2)) # -> immut id 1837091136 immut2 id 1837091120
```

##### shallow copy vs deep copy

```python
import copy

##### 얕은 복사 copy()

A = B = [1, 2, 3]  # A equals whatever B is, and B equals [1, 2, 3]
                   # A is dependent on B (원본이 바뀌면, 복사한 내용도 바뀜)
B[0] = 100    #(A[0] = 100 동일한 결과가 나온다)
print(A, B)            # -> [100, 2, 3] [100, 2, 3] 
print(id(A), id(B))    # -> 4517153608 4517153608 (same)
    
    
##### 깊은 복사 deepcopy()
    
C = [1, 2, 3]      #  원본을 복사해서 복사본을 따로 만드는 것 - 원본 변경해도 복사본 바뀌지 않음
D = C[:]           #  (C and D are independent) -> 2차원 리스트 요소까지는 복사본을 뜨지 못함 ㅜ (2차원 요소는 마치 다른 새로운 리스트를 가리키는 포인터가 들어있는 거나 마찬가지인데, 슬라이싱은 포인터까지는 복사본을 만들어내지 못함)
D = copy.deepcopy(C) # 다차원 리스트까지 완전한 복사본을 만들어냄
C[0] = 100
print(C, D)          # -> [100, 2, 3] [1, 2, 3]
print(id(C), id(D))  # -> 4517153608 4516516744



# compare copy.copy() and copy.deepcopy() with 2차원 리스트!
```







