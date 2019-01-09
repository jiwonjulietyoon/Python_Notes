# Index

- Numbered position of elements/items in an ordered array (e.g. string, list, tuple)
- Index of first item = 0
- Index of last item = -1

##### Indexing: accessing one item

If `list_a = [1, 2, 3, 4, 5]`, then `list_a[1] = 2`

##### Slicing: accessing multiple consecutive items

`items[Start:Stop[:Step]]`

- Start index: include
- Stop index: not include
- Step index: (optional) increment. cannot be 0.
- `items[m:n]` => from index m, and up to but not including index n

Ex) `slicing = 'ABCDEFG'`

- `slicing[1:4]` => 'BCD'
- `slicing[:5]` => 'ABCDE'  (may omit Start index if it is 0)
- `slicing[3:]` => 'DEFG' (may omit Stop index if it is the last)
- `slicing[-3:-1]` => 'EF' (negative index: count from the right, start with -1)
- `slicing[:]` => 'ABCDEFG' (return entire string)

Ex2) `step = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

- `step[::2]` => [1, 3, 5, 7, 9]
- `step[1::2]` => [2, 4, 6, 8, 10]
- `step[::3]` => [1, 4, 7, 10]
- `step[::-1]` => [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

##### Note) 문자열의 아이템은 독립적으로 수정할 수 없다

`text = '12345'` 일 때, `text[1] = '0'` 등 할당 기호를 사용한 독립 수정은 불가하다 (에러 유발)

문자열을 직접 수정할 수는 없으나, 슬라이싱으로 재결합한 새로운 문자열 생성은 가능하다
```python
>>> title = 'Brave Old World'
>>> new_title = title[:6] + 'New' + title[-6:]
>>> print(new_title)
Brave New World
```

.

.

# LIST

list_ex = [item1, item2, item3, ...]

- items may be a number, string, list, dictionary, defined variable, etc.

## Creating various lists

```python
empty_list_1 = []
empty_list_2 = list()

list_str = ['a', 'b', 'c']
list_int = [1, 2, 3]
list_mixed = ['a', 1, 2, 'b']
# item으로 변수(따옴표로 감싸지지 않은 문자열)를 넣을 수는 있으나, the variable must already have been defined!

list_f1 = list('A')          # -> ['A']
list_f2 = list('ABCDE')      # -> ['A', 'B', 'C', 'D', 'E']
list_f3 = list(['A', 'B'])   # -> ['A', 'B']
list_f4 = list([1])          # -> [1]   // type(list_f4[0]) == int
list_f5 = list([12345])      # -> [12345]
list_f6 = list([1, 2, 3])    # -> [1, 2, 3]
list_f7 = list(1)            # => TypeError: 'int' is not iterable
```

#### 다차원 리스트

- 1차원: `list_1 = ['a', 'b', 'c']`
- 2차원: `list_2 = ['a', ['X', 'Y', 'Z'], 'b', 'c']`
  - (two levels of lists)
- 3차원: `list_3 = ['a', 'b', ['X', 'Y', 'Z', [1, 2, 3]], 'c']`
  - (three levels of lists)

.

## List - Indexing & Slicing

```python
a = [1, 2, 3, 4, 5, 6]

print(a[len(a)-1])  # -> 6 (last index)
print(a[:3])        # -> [1, 2, 3]
print(a[3:])        # -> [4, 5, 6]
```

#### 다차원 리스트

```python
list_a = ['a', 'b', ['X', 'Y', 'Z', [1, 2, 3]], 'c']

print(list_a[2])       # -> 2차원 리스트: ['X', 'Y', 'Z', [1, 2, 3]]
print(list_a[2][3])    # -> 1차원 리스트: [1, 2, 3]
print(list_a[2][3][0]) # -> single item: 1
print(list_a[2][:2])   # -> ['X', 'Y']
```

.

## List - Adding Items

### 산술 연산자 ` + , * ` : does NOT modify the original list

##### `+` : 연결하기

- list_1 + list_2 => list_2의 아이템들만 뽑아서 list_1 끝에 붙여넣기

  - `print(['a', 'b', 'c'] + [1, 2, 3])` => `['a', 'b', 'c', 1, 2, 3]`

- 리스트는 리스트끼리만 더할 수 있다. list + str => TypeError

- 리스트를 str로 형변환하면 list + str 의 효과를 낼 수 있다

  - ```python
    a = [1, 2, 3, 4, '5']
    print(str(a[3]) + 'string')    # -> 4string
    print(str(a[4]) + 'string2')   # -> 5string2
    ```

##### `*`: 반복하기

`print([5, ['a', 'b'], 6] * 2)` => `[5, ['a', 'b'], 6, 5, ['a', 'b'], 6]`

### 리스트 내장 함수: modifies the original list

##### list.append(_arg_) -> 인자를 통째로 list 끝에 append (add one item at a time)

- takes exactly one argument

  - ```python
    app = [1, 2, 3]
    app.append('a')
    print(app)       # -> [1, 2, 3, 'a']
    
    # app.append(1, 2)  => TypeError: append() takes exactly one argument
    ```

- the 'one' argument could be a list => results in a 2차원 리스트

  - ```python
    app.append(['m', 'n'])
    print(app)      # -> [1, 2, 3, 'a', ['m', 'n']]
    ```

- append() in a for loop:

  - ```python
    app_test = []
    for x in range(0,4):
        app_test.append(x)
        
    print(app_test)     # -> [0, 1, 2, 3]
    ```

##### list.extend(_[new_list]_) -> 인자의 아이템만 뽑아서 list 끝에 아이템으로 추가 ('+' 연산자와 유사)

- only takes an iterable(list, range, tuple, string) as the argument

  - ```python
    ext = [1, 2, 3]
    ext.extend(['e', 'x', 't'])
    print(ext)      # -> [1, 2, 3, 'e', 'x', 't']
    
    ext.extend('end')
    print(ext)      # -> [1, 2, 3, 'e', 'x', 't', 'e', 'n', 'd']
    ```

- another way to 'extend': use the `+=` operator

  - ```python
    ext = [1, 2, 3]
    tup = (4, 5, 6)
    ext += tup      # 'ext + tup' would raise an error
    print(ext)      # -> [1, 2, 3, 4, 5, 6]
    ```

  - 

##### list.insert(_index_, _new_item_) -> 인자를 지정 위치에 아이템으로 추가

- insert ONE item at a time

  - ```python
    ins = [1, 2, 4, 5]
    ins.insert(2, 3)
    print(ins)     # -> [1, 2, 3, 4, 5]
    ```

- insert as first item of the list: `list.insert(0, first_item)`
- insert as last item of the list: `list.insert(len(list), last_item)`
- If _index_ is out of range (greater than the length of current list), add as the last item

.

## List  - 아이템 수정하기 - modifies original list

##### via Indexing

```python
a = ['x', 'y', 'v']
a[2] = 'z'
print(a)   # -> ['x', 'y', 'z']
```

##### via Slicing

```python
b = ['a', 'b', 'C', 'D', 'E', 'f']
b[2:-1] = ['c', 'd', 'e']      # 양변이 가리키는 아이템 개수는 동일하지 않아도 됨
print(b)   # -> ['a', 'b', 'c', 'd', 'e', 'f']
```

.

## List - 아이템 삭제하기 - modifies original list

##### list[ : ] = []

```python
c = [1, 2, 3, 'm', 'n', 4, 5]
c[3:5] = []
print(c)     # -> [1, 2, 3, 4, 5]

# c.f
e = [1, 2, 3]
e[1] = []
print(e)     # -> [1, [], 3]   (empty list is inserted)
```

##### del list[index]

```python
d = [1, 2, 3, 'm', 'n', 4, 5]
del d[3:5]
print(d)     # -> [1, 2, 3, 4, 5]
```

- `del` can also delete the list completely

  - e.g) `del thislist`

- Deleting every other item using 'del'

  1. ```python
     del_step = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     del del_step[::2]
     print(del_step)      # -> [2, 4, 6, 8, 10]
     ```

  2. ```python
     del_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     for x in range(5):
         del del_range[x]
     print(del_range)      # -> [2, 4, 6, 8, 10]
     ```

     - `range(5)`는 `(0, 1, 2, 3, 4)` 이긴 하지만, for loop이 돌면서 하나씩 삭제된다는 점 유의!
     - e.g) `del_range[0] => [2, 3, 4, 5, 6, 7, 8, 9, 10]`
     - e.g) `del_range[1] => [2, 4, 5, 6, 7, 8, 9, 10]`

##### list.clear()   :  empties the list

```python
thislist = ['a', 'b']
thislist.clear()
print(thislist)          # -> []
```

##### list.remove('_item_')

- only deletes the first occurring 'item' (not all)

- only accepts one argument

- ```python
  f = [1, 2, 3, 2, 4, 2, 5]
  f.remove(2)
  print(f)          # -> [1, 3, 2, 4, 2, 5]
  ```

##### list.pop(_[index]_)   : _index_ 위치에 있는 아이템을 반환한 후 리스트에서 삭제하기

- If the argument, _index_, is not provided, returns and removes the last item from the list.

```python
g = [1, 2, 3, 4, 5]
print(g.pop())      # -> 5
print(g)            # -> [1, 2, 3, 4]
```

- The popped item can be stored into a variable

  - ```python
    g = [1, 2, 3, 4, 5]
    popped = g.pop()
    print(popped)   # -> 5
    ```

.

## List - 아이템 정렬하기 - modifies original list

##### list.sort()

- default: ascending order (`list.sort(reverse=False)`)

  - descending order (`list.sort(reverse=True)`)

- ```python
  a = [3, 6, 1, 5, 4, 2]
  
  a.sort()
  print(a)     # -> [1, 2, 3, 4, 5, 6]
  
  a.sort(reverse=True)
  print(a)     # -> [6, 5, 4, 3, 2, 1]
  ```

- c.f. `sorted(list)` : returns sorted list without modifying the original list

  - ```python
    list_a = [3, 1, 6, 4, 5, 2]
    print(sorted(list_a))       # -> [1, 2, 3, 4, 5, 6] 
    ```

##### list.reverse()   : flips order of items; 아이템 순서를 반대로 뒤집기

- Note) `.reverse()` != `sort(reverse=True)`

- ```python
  a = [3, 6, 1, 5, 4, 2]
  a.reverse()
  print(a)     # -> [2, 4, 5, 1, 6, 3]
  ```

- c.f `reverse(list)` : returns reversed list without modifying the original list

  - The return value is NOT a list! => need to convert into a list `list(reversed(list_name))`

.

## List - Count

##### list.count('_item_')     : count specific items

```python
a = [1, 2, 3, 3, 3, 3, '3', '3', '3', 4, 5]
print(a.count(3))      # -> 4
print(a.count('3'))    # -> 3
```

##### len(list)      : count total number of items in the list

```python
a = [1, 2, 3, 3, 3, 3, '3', '3', '3', 4, 5]
print(len(a))          # -> 11
```

.

## List Comprehension

=> Concise way of creating lists based on existing lists

`evenlist = [i for i in range(1, 11) if i%2==0]`
`cubiclist = [i**3 for i in range(1, 11)]`

#### Ex) Before: For Loop

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
pair = []

for girl in girls:
    for boy in boys:
        pair.append((boy, girl))
```

#### Ex) After: List Comprehension

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']

pair = [(boy, girl) for boy in boys for girl in girls]
```

##### Pythagoras: x < y < z < 50 일 때 피타고라스 방정식의 해를 찾기

```python
pythagoras = [(x, y, z) for x in range(1, 50) for y in range(x+1, 50) for z in range(y+1, 50) if x**2+y**2==z**2]
```

##### Getting rid of all vowels

```python
words = 'Life is too short, you need python!'
vowels = 'aeiou'
words2 = "".join([w for w in words if w not in vowels])
print(words2) # -> Lf s t shrt, y nd pythn!
```









.

.

# TUPLE

tuple_ex = (item1, item2, item3)

- can NOT edit/delete tuple items! 
- 'Tuple' object does NOT support item assignment (수정) and deletion

##### Creating a Tuple

```python
t1 = ()
t2 = (1, 2, 3)
t3 = 1, 2, 3
t4 = 1,          # t4 = 1  이라고만 쓰면 t4는 tuple이 아닌 int 가 된다.
```

##### Tuple Indexing, Slicing

```python
t1 = (1, 2, 3, 4, 5) 
print(t1[2], type(t1[2]))     # -> 3 <class 'int'>
print(t1[:3], type(t1[:3]))   # -> (1, 2, 3) <class 'tuple'>
```

##### `+`, `*` Operators

```python
t1 = (1, 2, 3, 4)
t2 = (100, 200)
print(t1 + t2)        # -> (1, 2, 3, 4, 100, 200)
print(t2 * 3)         # -> (100, 200, 100, 200, 100, 200)
```

.

.

# DICTIONARY

dict_ex = {key1:value1, key2:value2, ...}

- Key: 문자, 숫자, 튜플
- Value: 문자, 숫자, 리스트, 딕셔너리 등 any data type
- Item = {key:value} 하나의 쌍
- unordered, changeable, indexed

##### Creating a Dictionary

```python
d1 = dict()
d2 = {}
```

##### 1차원 딕셔너리 : 모든 아이템이 각각 하나의 값으로만 이루어짐

```python
d1 = {'A': 65, 'B': 66, 'C': 67, 'Z': ''}  # key/value can't be empty
print(d1)                                  # => ''라도 넣어야 함
```

##### 다차원 딕셔너리 : 아이템에 리스트, 딕셔너리 등이 있음

```python
d3 = {'a': [1, 2, 3], 
      'b': 100, 
      'c': {1: 300}}
d4 = {'a': [1, 2, 3, [10, 20, (0, 0)]], 
      'b': 100, 
      'c': {1: 300, 2: [1, 2, {'A': 'B'}]}}
```

##### Key vs Value

| key                                                          | value                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| - can't be redundant (변수명 중복 불가인 것처럼) <br>-  key 이름을 중복 작성하면, 가장 마지막에 할당된 아이템으로 덮어쓰기 된다 <br>- List는 쓸 수 없다. 수정 불가능한 Tuple은 쓸 수 있다. | - 모든 자료형을 쓸 수 있다<br>- key가 있으면 반드시 value도 있어야 한다. |

##### Dictionaries are unordered, but indexed by 'key' (no index numbers)

```python
d1 = {'num': [1, 2], 
      'alpha': ('a', 'b', 'c'), 
      'month': {'Jan': 1, 'Feb': 2}}

print(d1['alpha'][1])               # -> b
print(d1['month']['Feb'])           # -> 2
print(d1.get('month'))              # -> {'Jan': 1, 'Feb': 2}
print(d1.get('month').get('Jan'))   # -> 1
```

.

## Dictionary - Adding Items

##### Adding a new {key: value}

```python
d2 = {}
d2['Jan'] = '1st'
d2['Feb'] = '2nd'
print(d2)             # -> {'Jan': '1st', 'Feb': '2nd'}
```

##### Replacing the value of an existing key

```python
d3 = {1:'a', 2:'b', 3:'d'}
d3[3] = 'c'
print(d3)             # -> {1: 'a', 2: 'b', 3: 'c'}
```

.

## Dictionary - Deleting Items

##### del dict['_key_']   : delete single {key: value} item

```python
d4 = {11:'a', 22:'b', 33:'A'}
del d4[33]
print(d4)             # -> {11: 'a', 22: 'b'}
```

##### dict.clear()   : empty entire dictionary

```python
d4.clear()
print(d4)             # -> {}
```

.

## Dictionary - dict.keys(), dict.values(), dict.items(), in operator

```python
d5 = {'num': [1, 2], 
      'alpha': ('a', 'b', 'c'), 
      'month': {'Jan': 1, 'Feb': 2}}
```

##### dict.keys()   : 딕셔너리의 key 값만 반환

```python
print(d5.keys(), type(d5.keys())) 
     # -> dict_keys(['num', 'alpha', 'month']) <class 'dict_keys'>
```

##### dict.values()   : 딕셔너리의 value 값만 반환

```python
print(d5.values(), type(d5.values()))
     # -> dict_values([[1, 2], ('a', 'b', 'c'), {'Jan': 1, 'Feb': 2}]) <class 'dict_values'>
```

##### dict.items()   : 딕셔너리의 key:value 쌍들을 반환

```python
print(d5.items(), type(d5.items()))
     # -> dict_items([('num', [1, 2]), ('alpha', ('a', 'b', 'c')), ('month', {'Jan': 1, 'Feb': 2})]) <class 'dict_items'>
```

##### _key_ in _dict_  : 딕셔너리 key가 존재하는지 여부를 True/False로 알려줌

```python
print('num' in d5)    # -> True
```

.

.

# SET

set_ex = {item1, item2, item3}

- items may NOT be redundant => 값의 중복을 제거해주는 자료형
- 가능한 item: string, tuple (hashable types - 고정된 길이를 가짐)
  - Note) list, dict types are UNhashable
- unordered, unindexed => no indexing, no slicing

##### Creating a Set

```python
s1 = set()                  # only way to create an empty set
s2 = set([1, 2, (10, 20)])  # set(1, 2, 3) : error => one argument only
s3 = set((1, 2, (10, 20)))
s4 = {1, 2, 3, 4, 5}

s5 = set('abcde')
print(s5)  # -> {'e', 'b', 'd', 'c', 'a'}  (unordered -> random order)

s6 = set({'k1': 'v1', 'k2': 'v2'})
print(s6)  # -> {'k1', 'k2'} (딕셔너리 타입을 지정하면 key값만 뽑아서 아이템으로 저장)
```

##### 중복 값 제거 기능

```python
redundant_list = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5]
print(set(redundant_list))          # -> {1, 2, 3, 4, 5}

new_list = list(set(redundant_list))
print(new_list)                     # -> [1, 2, 3, 4, 5]
```

##### Indexing, Slicing 하려면 list/tuple 등 인덱싱 가능한 자료형으로 변환을 먼저 해야 함

```python
s1 = {1, 2, 3, 4, 5}
a_list = list(s1)[:3]  # ==> [1, 2, 3]
print(set(a_list))     # ->  {1, 2, 3}
```

.

## SET 집합 연산 : 차집합(-), 교집합(&), 합집합(|)

##### 차집합, '`-`', `s1.difference(s2)` => elements unique to `s1`

```python
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
print(s1 - s2)              # -> {1, 2}
print(s1.difference(s2))    # -> {1, 2}
```

##### 교집합, '`&`', `s1.intersection(s2)`

```python
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
print(s1 & s2)              # -> {3, 4, 5}
print(s1.intersection(s2))  # -> {3, 4, 5}
print(s2.intersection(s1))  # -> {3, 4, 5}
```

##### 합집합, '|', s1.union(s2)  - 중복되는 아이템은 한번만 포함

```python
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
print(s1 | s2)          # -> {1, 2, 3, 4, 5, 6, 7}
print(s1.union(s2))     # -> {1, 2, 3, 4, 5, 6, 7}
```

.

## Set - Adding Items

##### set.add()    : add one item that is hashable (길이 고정)

```python
s1 = {1, 2, 3}
s1.add((1, 2))
print(s1)       # -> {(1, 2), 1, 2, 3}
```

- 추가 가능: 숫자, 문자, 문자열, 튜플
- 추가 불가능: 리스트, 딕셔너리

##### set.update()  : add multiple items in a string, list, tuples, etc.

- 아이템만 개별적으로 뽑아서 추가한다 (from strings, tuples, lists)
- list, tuple 등에 들어있지 않은 숫자는 제외 (int, float 등 단독적으로 추가 불가)

```python
s1 = {1, 2, 3}
s1.update('abc')
print(s1)      # -> {1, 2, 3, 'a', 'c', 'b'}

s1 = {1, 2, 3}
s1.update((10, 20))
print(s1)      # -> {1, 2, 3, 10, 20}

s1 = {1, 2, 3}
s1.update({'k1':'v1', 'k2':'v2'})
print(s1)      # -> {1, 2, 3, 'k1', 'k2'} (dict => key값만 뽑아서 추가)
```

.

## Set - Delete Items

##### set.remove() vs set.discard()

- set.discard() : no error is raised even if item is not present in the set

```python
s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

s2.discard(10)  # same result as s2.remove(10)
print(s2)       # -> {1, 2, 3, 4, 5, 6, 7, 8, 9}


#s2.remove(0)   # -> KeyError: 0 is not present in s2
s2.discard(0)   # -> nothing happens
```



