# Python Formatting: %, .format, f"string"

### ## % formatting

##### - %d : int (integer)

```python
print('%d + %d = %d' % (2, 3, 2+3))  # -> 2 + 3 = 5
print('%d degrees' % 17.8)           # -> 17 degrees

# %-10.8d => -(align left), 10(total spaces), .8(leftover spaces filled with 0)
print('|%-10.8d|' % 555)    # -> |00000555  |
```

