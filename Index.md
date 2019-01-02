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

#### 산술 연산자 ` + , * ` : does NOT modify the original list

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

`*`: 반복하기







```python
>>> list_a = [3, 1, 6, 4, 5, 2]
>>> print(sorted(list_a)) # does not modify original list
[1, 2, 3, 4, 5, 6] 
```



