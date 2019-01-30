## Database 기본 용어

- __RDBMS__: Relational Database Management System
- __CRUD__: Create, Read, Update, Delete
- __TABLE__: collection of records
- __COLUMN__: one data info
- __RECORD__: row (all data info of one item)



## SQLite 시작

- 터미널에서 `sqlite3` 입력
- Ctrl + D   or `.exit` to quit
- 명령어:
  - `.` 으로 시작하는 명령어 (does not end with a semicolon)
  - All-caps commands end with a semicolon (may insert line breaks in between)
    - all-caps are NOT mandatory, but conventional in terms of readability



## csv파일로부터 데이터베이스 불러오기

`.mode csv`

`.import fileName.csv tableName`



## Commands starting with `.`

- `.tables` : print names of all tables in the database
- `.mode column`: when printing records, align by column
- `.headers on`: when printing records, also print each respective column name
- `.schema tableName`: print all columns & data type of _table_
- `.read fileName.sql` : run whatever commands are saved in _fileName.sql_



## Creating a Table

```sqlite
CREATE TABLE tableName (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);
```

