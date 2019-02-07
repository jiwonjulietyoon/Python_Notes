# ORM and Flask-Alchemy

- 데이터의 객체화
- Cloud9 + FlaskAlchemy + Python
  - No SQLite
- Advantages of switching to ORM+FlaskAlchemy from SQLite:
  - 어떤 DB를 쓰더라도 코드를 수정할 필요가 없음
  - DB 전환이 매우 수월



### Initialization (in `app.py`)

```python
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DBName.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)
```

- in `app.py`



### Create a New Table (in `app.py`)

```python
class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    ...
    ...
db.create_all()
```

- counterpart to SQL's `CREATE TABLE`



### Display Selected Data

```
SELECT * FROM articles;
=> Article.query.all()

SELECT * FROM articles WHERE id = 1;
=> Article.query.filter_by(id=1).all()

SELECT * FROM articles WHERE title = 'Test' LIMIT 1;
=> 
```













