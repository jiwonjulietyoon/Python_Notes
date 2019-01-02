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



