# Python notes to be categorized later..



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











