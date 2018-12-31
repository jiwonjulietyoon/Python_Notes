# Python Formatting: %, .format, f"string"

## % Formatting

##### - %d : int (integer)

`print('%d + %d = %d' % (2, 3, 2+3))` =>    2 + 3 = 5

`print('%d degrees' % 17.8)` =>  17 degrees (소수점 이하의 자리는 유실됨)

`%-10.8d` => `-`(align left), `10`(min field width), `.8`(fill; 인자 앞에 남는 자리는 0으로 채움)

- ex) `print('|%-10.8d|' % 555)`    => |00000555  |

##### - %f : float

`print('%f degrees' % 17.8` => 17.800000 degrees  (디폴트: 소수점 이하 6자리)

`print('%f degrees' % 17)` => 17.000000 degrees

`%-10.3f` => `-`(align left), `10`(min field width), `.3`(precision; 소수점 이하 자리수)

- ex) `print('|%-10.3f|' % 17.8)`    => |17.800    |
- ex) `print('|%3.4f|' % 123.45)` => |123.4500|
  - 'min field width' 보다 표현되어야 할 자리수가 더 많다면, min field width는 무시된다

##### -%s : string

전달할 인자로는 int, float, str 다 가능하다

`%-10.8s` => `-`(align left), `10`(min field width), `.8`(인자로부터 가져올 문자 개수)

- ex) `print('|%-10.8s|' % 'ABCDEFGHIJKL')` => |ABCDEFGH  |
- ex) `print('|%.4s|' % 12.345)` => |12.3| (인자로 숫자가 전달되면, 문자열로 인식된다)

.

## .format()

```python
print('first = {} / last = {}'.format('Jiwon', 'Yoon'))
```

```python
first = 'Jiwon'
last = 'Yoon'
print('first = {} / last = {}'.format(first, last))
```

```python
i0 = 'zero'
i1 = 'one'
i2 = 'two'
print('Index1 = {1} / Index0 = {0} / Index2 = {2}'.format(i0, i1, i2))
```

- => `Index1 = one / Index0 = zero / Index2 = two`

```python
print('1 = {one} / 2 = {two}'.format(one='eins', two='zwei'))
```

- => `1 = eins / 2 = zwei`

```python
two = 'zwei'
three = 'drei'
print('1 = {one} / 2 = {1} / 3 = {0}'.format(three, two, one='eins'))
```

- => `1 = eins / 2 = zwei / 3 = drei`
- Variables that are NOT already defined  (e.g `one='eins'`) must be positioned as the last parameter

##### Format Specifier

{A:B>C}

- A: index number or variable name
- B: fill character (공백 대체 문자) - align과 C를 지정해야 사용 가능
- '>', '<', '^': right, left, center align - C를 지정해야 사용 가능
- C: minimum field width

`print('|{:->10}|'.format('juliet'))` => `|----juliet|`

`print('|{:!^10}|'.format('juliet'))` => `|!!juliet!!|`

`print('|{:*<10}|'.format('juliet'))` => `|juliet****|`

```python
num = 30
print('나는 {choc:*^8}과자를 {0:!^10}개 먹었다.'.format(num, choc='초코'))
# output: 나는 ***초코***과자를 !!!!30!!!!개 먹었다.
```

```python
print('Curly Bracket 기호: {{}}'.format())
# output: Curly Bracket 기호: {}
```

.

## f'string' - String Interpolation (Python 3.6+)

```python
>>> num1 = 5
>>> num2 = 10
>>> f'Five plus ten is {num1 + num2} and not {2 * (num1 + num2)}.'
'Five plus ten is 15 and not 30.'
```

