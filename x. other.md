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

