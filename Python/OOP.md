# Object Oriented Programming (OOP)

### 객체 지향 프로그래밍이란?

- 동일한 기능을 재사용
- 모듈화, modularization
- 부품을 기능 별로 나누어서 따로 정의해놓을 때
- 사물들의 공통점을 찾아서 하나의 그룹으로 분류를 할 때 (인간의 상식적인 인지과정)
  - Class = 위와 같은 분류 체계
- "class" is like a common template, containing the most basic attributes/methods that all instances of the template share in common
- **주어.동사()** 또는 **메인모듈.서브모듈()** 의 형태
  - app.run()
  - turtle.Turtle()
  - ggobugi.forward()
  - random.sample()

.

## Class Definition

Outline:

```python
globalvar = "CAN'T be accessed via Class1 instance methods"

class Class1:
    classvar = "CAN be accessed via Class1 and Class1 instance methods"
    def __init__(self, parameter1, parameter2):
        self.var1 = parameter1
        self.var2 = parameter2
    def __del__(self):
        return return_value_when_instance_is_deleted
    def __repr__(self):
        return return_value_when_instance_is_printed
    def method1(self):
        return method1_result + f"{self.var1}, {Class1.classvar}"

Instance1 = Class1(Param1, Param2)

Instance1.method1()     # == Class1.method1(Instance1)

del Instance1
```

- 주의사항:
  - 클래스 내에 정의되는 모든 메소드는 첫 번째 인자로 `self`를 전달한다. (꼭 "self" 가 아니어도 되고 다른 표현을 쓸 수는 있으나, 관습적으로 "self"를 쓴다.)
  - `__init__` 처럼 양쪽에 `__`가 있는 메서드를 special method 혹은 magic method라고 부른다.
  - Variable Scope:
    - global variable: 
- `def __init__`:
  - 인스턴스 생성할 때마다 자동으로 실행되는 함수
    - `self` 이외의 다른 `parameter`가 인자로 전달될 경우, 인스턴스를 생성할 때도 해당 인자들을 반드시 전달해야 한다.
- `def __del__`: 
  - 인스턴스가 삭제될 때 실행되는 함수
  - 인스턴스를 삭제하는 방법은 두 가지가 있는데,
      1.  `del Instance1` 이 가장 직접적인 방법이고
      2.  `Instance1 = Class1()` 처럼 동일한 이름의 인스턴스를 한번 더 생성하면, 기존에 생성됐었던 인스턴스는 자연히 삭제된다.
- `def __repr__`: 
  - 인스턴스 자체를 출력할 때 이 부분의 반환값이 출력된다.
  - `__repr__`이 정의되지 않았을 경우, 인스턴스 자체를 출력 시도하면 해당 인스턴스의 storage address가 출력된다.
    - e.g) `<__main__.Class1 object at 0x0598B870>`
- `def method1`:
  - 인스턴스에 적용되는 메소드를 호출하고자 할 때는:
    1. `Instance1.method1()`
    2. `Class1.method1(Instance1)` : 괄호 안의 `Instance1` 을 생략할 경우, 

.

## Class Example: Person

##### Person Definition

```python
globe = "Global Variable"

class Person:
    population = 0
    def __init__(self, Name, age, gender='F'):
        self.name = Name  # typically: self.name = name
        self.age = age
        self.gender = gender
        self.cash = 0
        print(f"Instance {self.name} has been created.")
        Person.population += 1  
    def __del__(self):
        print(f"Instance {self.name} has been deleted.")
    def __repr__(self):
        return f"[repr]Instance {self.name} of Person Class"
    def __str__(self):
        return f"[str]Instance {self.name} of Person Class"
    def introduce(self):
        print(f"Hi, I am {self.name}. I'm {self.age} yrs old and my gender is {self.gender}.")
    def add_cash(self, money):
        self.cash += money
    def print_cash(self):
        print(f"{self.name}'s cash: {self.cash}")
    def print_population(self):
        print(f"Current Population: {Person.population}")
    @staticmethod
    def info():
        print("Human")
    @classmethod
    def print_pop(cls):
        print(f"Current Population (class method): {cls.population}")
```

##### Create Instances `jiwon`, `juliet`, and `john`

```python
>>> jiwon = Person('Jiwon', 26)
Instance Jiwon has been created.

>>> juliet = Person('Juliet', 25)
Instance Juliet has been created.

>>> john = Person('John', 30, 'M')
Instance John has been created.
```

##### Check Available Instance Methods and Membership

```python
>>> print(dir(jiwon))
['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add_cash', 'age', 'cash', 'gender', 'info', 'introduce', 'name', 'population', 'print_cash', 'print_pop', 'print_population']

>>> print(isinstance(jiwon, Person))     # isinstance('instance', 'class')
True
```

##### Print Instances (`__repr__` and `__str__`)

```python
>>> print(jiwon)
[str]Instance Jiwon of Person Class
```

- `__repr__` or `__str__` is returned when an instance is printed (whichever one happens to be defined)
- When both `__repr__` and `__str__` are defined, `__str__` overrides
- When neither `__repr__` nor `__str__` is defined, the storage/memory address of the instance is returned
  - e.g) `<__main__.Person object at 0x0598B870>`

##### Instance Methods

```python
>>> john.introduce()
Hi, I am John. I'm 30 yrs old and my gender is M.

>>> Person.introduce(john)
Hi, I am John. I'm 30 yrs old and my gender is M.
```

- `Person.introduce()` raises a TypeError: 
  - `introduce() missing 1 required positional argument: 'self'`,
  - where `self` must be an instance of `Person`, e.g) `john`

##### Class Variables (`population`, in this case)

```python
>>> print(Person.population)
3

>>> print(jiwon.population)
3

>>> jiwon.print_population()
Current Population: 3
```

- **Class variables**: data shared by all instances
  - defined outside `__init__`
  - can be accessed by both instances and the class itself
    - e.g) `Person.population`, `jiwon.population`
    - instances have access to all parent class variables
  - when called within the `__init__` method, use `Person.population`
- c.f) **Instance Variables**: data specific to each individual instance
  - can be accessed via `instancename.instancevar`

##### Static Method and Class Method

```python
>>> juliet.print_pop()
Current Population (class method): 3

>>> Person.print_pop()
Current Population (class method): 3

>>> juliet.info()
Human

>>> Person.info()
Human
```

- **Class Method** : can only access class variables
  - Use `@classmethod` as the decorator
  - Typically uses `cls` (short for 'class') as the parameter
- **Static Method**: cannot access any variables (neither class or instance)
  - Use `@staticmethod` as the decorator
  - No parameter needed upon definition
- both Class and Static Methods can be called by all instances as well as the class itself.

##### Instance methods that accept additional variables

```python
>>> juliet.add_cash(3000)

>>> juliet.print_cash()
Juliet's cash: 3000
```

##### Variable Scope: Class, Instance, and Global

```python
>>> print(jiwon.population)
3

>>> print(juliet.cash)
3000

>>> print(juliet.globe)    
#AttributeError: 'Person' object has no attribute 'globe'
```

- instances can access both class and instance variables, but cannot directly access any global variables defined outside the class

##### Delete Instances

```python
>>> del jiwon
Instance Jiwon has been deleted.

>>> juliet = Person('Juliet', 25)
Instance Juliet has been created.
Instance Juliet has been deleted.
```

- When indirectly deleting an instance by creating a new instance with the same name, the new instance is created right before the older one is deleted (thus resulting in the order of the messages printed in the above example)



.

.

.

## unfinished - oop2.ipynb

- 연산자 오버라이딩 (중복 정의)
- 상속
- super()
- method overriding
- multiple inheritance

