# 0. Intro

### Importing Modules

- `import` MODULE
- `from` MODULE `import` SUB-MODULE/ATTRIBUTE1, SUB-MODULE/ATTRIBUTE2
  - `from` MODULE `import` SUB-MODULE `as` NICKNAME
  - -> specifically imports the mentioned attributes only. (can't use unmentioned attributes)
- `from` MODULE `import *`
  - not recommended due to inefficiency (사용하지 않은 어트리뷰트도 다 메모리 상에 올려놓기에)

-  **dir(_module_)** : check all attributes offered by the _module_
- List of Python Modules: https://docs.python.org/3/library/index.html

### Overview of How Modules Work

Ex) `Add.py` (`Add` 모듈) and `importer.py` (`Add` 모듈을 임포트한 다른 모든 파일) 

- -> located in the same directory

**`Add.py` => Add 모듈**

```python
def Add_two(num):
    return num + 2
def Add_three(num):
    return num + 3
def Add_four(num):
    return num + 4

print("__name__:", __name__)
print("이 부분은 Add.py 또는 importer.py가 실행될 때 항상 출력된다.")

if __name__ == "__main__":
    print("add.py 이 직접 실행되었을 때만 출력되는 부분이다.")
    print("즉, __name__이 __main__일 때만 출력된다.")
    print("import.py만 실행하면 이 부분은 출력되지 않는다.")
```

- `Add.py`에는 `Add`라는 모듈의 내용이 담겨 있고, 함수는 `Add_two` ~ `Add_four` 3개가 정의되어 있다.
- `Add.py` 를 실행할 때는 `__name__` 이  `__main__` 이 되고, `importer.py` 를 실행할 때는 `Add` 가 된다.
- `if __name__ == "__main__":`  조건문 안의 실행문은 `Add.py` 을 직접 실행할 때만 작동한다.  나머지 실행문은 `Add.py` 파일을 실행할 때는 물론, `importer.py` 을 실행할 때도 작동한다.

**`importer.py` => Add 모듈을 임포트한 다른 모든 파일**

```python
import Add                 # Add 모듈을 통째로 불러오기.
print(dir(Add))            # 모든 attribute 목록을 출력하기
print(Add.Add_three(10))   # 애초에 'from Add import *' 라 했다면 'Add.'은 생략 가능

=============================

from Add import Add_two as TWO   # Add 모듈에서 Add_two 함수만 불러오기
print(TWO(10))                   # TWO 제외한 Add 모듈의 다른 함수는 사용 불가
```

.

.

.

## math

Note) `math` 모듈 없이 사용할 수 있는 기본 함수: `sum`, `max`, `min`, `abs`, `pow`, `round`, `divmod`

##### 상수

- `math.pi`, `math.e`

##### Operators

- `math.ceil(x)` : round up (smallest integer greater than x)
- `math.floor(x)`: round down (greatest integer less than x)
- `math.trunc(x)`: return the integer part of x (소수점 이하 자리수 버림)
  - `round(-3.3)` == `-3`
  - `math.floor(-3.3)` == `-4`
  - `math.trunc(-3.3)` == `-3`
- `math.factorial(x)` : return x!
- `math.fmod(x, y)`





.

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

## webbrowser

Opens url via a webbrowser

```python
import webbrowser
webbrowser.open('some_url.com')
# c.f webbrowser.open_new(), webbrowser.open_new_tab()
```

.

## random

Random Sampling

```python
import random

random.sample(target_list, 5)   # randomly select multiple items
random.choice(target_list)      # randomly select one item
```

.

## os

Rename multiple files

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

Environment Variables

```python
import os
Var = os.getenv('ENV_VAR')
```

.

## pprint

pretty print (more legible JSON data)

```python
from pprint import pprint as pp
url = f"https://api.telegram.org/{token}/getUpdates"
response = requests.get(url)
doc = response.json()
pp(doc)    # -> will print 'doc' in a relatively more legible JSON format
```

.

## faker

```python
from faker import Faker
fake = Faker()

print(fake.name())
print(fake.job())
print(fake.address())
```

.













