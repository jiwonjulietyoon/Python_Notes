# SQLite and SQL Statements via Python

- `import sqlite3` : required module
- `c = sqlite3.connect('DBName.sqlite3')` : open/create an SQLite database
  - equivalent to `sqlite3 DBName.sqlite3` on a regular SQLite terminal
- `db = c.cursor()`
- `db.execute('[SQL statement]')` : run specified SQL statement (omit semicolon)
  - e.g) `db.execute('SELECT * FROM tableName')`
- `data = db.fetchall()` : store "selected" data (from a previous `db.execute('SELECT ...')` command)
- `c.commit()` : apply changes made on a database via `INSERT INTO`, `UPDATE`, or `DELETE` SQL statements
- `c.close()` : close and exit from an SQLite database

.

.

# [CRUD ex] Flask + Python + SQLite

### List of C9 Files

```
app.py
board.sqlite3          # SQLite database
templates/
	index.html   # Write new article + View list of all submitted articles
	update.html  # Edit existing article
```

### `app.py`

```python
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def query(queryname, tablename, moreinfo=None):    # queryname: 'create', 'readall', 'readone', 'update', 'delete'
    c = sqlite3.connect('board.sqlite3') # DB 'board' already has a table named articles, which has 3 columns: id, title, content
    db = c.cursor()
    data = None
    if queryname == "create":            # moreinfo == (title, content)
        sql = "INSERT INTO {} (title, content) VALUES('{}', '{}')".format(tablename, moreinfo[0], moreinfo[1])
        db.execute(sql)
        c.commit()
    elif queryname == "readall":         # moreinfo : leave blank
        sql = "SELECT * FROM {}".format(tablename)
        db.execute(sql)
        data = db.fetchall()
    elif queryname == "readone":         # moreinfo == (article_id)
        sql = "SELECT * FROM {} WHERE id = {}".format(tablename, moreinfo[0])
        db.execute(sql)
        data = db.fetchall()
    elif queryname == "update":          # moreinfo == (newTitle, newContent, article_id)
        sql = "UPDATE {} SET title='{}', content='{}' WHERE id = {}".format(tablename, moreinfo[0], moreinfo[1], moreinfo[2])
        db.execute(sql)
        c.commit()
    elif queryname == "delete":          # moreinfo == (article_id)
        sql = "DELETE FROM {} WHERE id = {}".format(tablename, moreinfo[0])
        db.execute(sql)
        c.commit()
    c.close()
    return data


@app.route("/")
def index():
    # 1. 사용자로부터 입력을 받아 /create로 넘겨줌
    # 2. 모든 게시물을 보여줌
    data = query('readall', 'articles')
    return render_template('index.html', data=data)

@app.route("/create", methods=["POST"])
def create():
    title = request.form['title']
    content = request.form['content']
    query('create', 'articles', [title, content])
    return redirect('/')

@app.route("/delete/<int:article_id>")
def delete(article_id):
    # 특정 게시물을 삭제한다
    query('delete', 'articles', [article_id])
    return redirect('/')
    
@app.route("/update/<int:article_id>")
def update(article_id):
    data = query('readone', 'articles', [article_id])
    return render_template('update.html', data=data)
    
@app.route("/update2", methods=["POST"])
def update2():
    title = request.form['title']
    content = request.form['content']
    article_id = request.form['article_id']
    query('update', 'articles', [title, content, article_id])
    return redirect('/')
```

### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>게시판</title>
    <style>
        table, th, td {
            border: 1px solid;
            border-collapse: collapse;
        }
    </style>
</head>
<body>
    <h1>게시글 작성하기</h1>
    <form action="/create" method="POST">
        제목: <input type="text" name="title" placeholder="제목을 입력하세요"/><br>
        내용:<br><textarea rows="10" cols="30" name="content" placeholder="내용을 입력하세요"></textarea><br>
        <input type="submit" value="작성하기"/>
    </form>
    
    <h2>게시판</h2>
    <table>
        <col width="30">
        <col width="200">
        <col width="400">
        <col width="100">
        <tr>
            <th>id</th>
            <th>Title</th>
            <th>Content</th>
            <th>-</th>
        </tr>
        {% for row in data %}
        <tr>
            <td>{{row[0]}}</td>
            <td>{{row[1]}}</td>
            <td>{{row[2]}}</td>
            <td><a href="/update/{{row[0]}}">[수정]</a> <a href="/delete/{{row[0]}}">[삭제]</a></td>
        </tr>
        {% endfor %}
    </table>

</body>
</html>
```

### `update.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>게시글 수정하기</h1>
    <form action="/update2" method="POST">
        제목: <input type="text" name="title" value="{{data[0][1]}}"/><br>
        내용:<br><textarea rows="10" cols="30" name="content">{{data[0][2]}}</textarea><br>
        <input type="hidden" name="article_id" value="{{data[0][0]}}">
        <input type="submit" value="수정하기"/>
    </form>
    
</body>
</html>
```

