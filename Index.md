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
