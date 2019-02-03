## Database 기본 용어

- __Database__: 체계화된 데이터의 모임 (파일은 체계화되지 않음)
- __RDBMS__: Relational Database Management System
  - e.g) MySQL, SQLite
  - SQLite: 경량 / 서버가 아닌 응용프로그램에 넣음 / c9등에 기본 탑재
- __CRUD__: Create, Read, Update, Delete
- __TABLE__: collection of records
- __COLUMN__: one data info
- __RECORD__: row (all data info of one item)



## SQLite 시작

- 터미널에서 `sqlite3` 입력
- `sqlite3 DBName.sqlite3` to access database (or create a new database if it already doesn't exist)
- Ctrl + D   or `.exit` to quit
- 명령어:
  - SQLite commands: `.` 으로 시작하는 명령어 (does not end with a semicolon)
  - SQL statements: All-caps commands end with a semicolon (may insert line breaks in between)
    - all-caps are NOT mandatory, but conventional in terms of readability





## SQLite Commands starting with `.`

- `.tables` : print names of all tables in the database
- `.mode column`: when printing records, align by column
- `.headers on`: when printing records, also print each respective column name
- `.schema tableName`: print all columns & data type of _tableName_
- `.read fileName.sql` : run whatever commands are saved in _fileName.sql_
- `.mode csv` => `.import fileName.csv tableName` : csv파일로부터 데이터 레코드 불러오기



## CREATE TABLE: create a new table

```sqlite
CREATE TABLE tableName (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);
```

- _tableName_: usually a plural form
- Data Type : `INTEGER`, `TEXT`, `REAL`
- `PRIMARY KEY` : 
  - may be labeled to one column only (usually id)
- `AUTOINCREMENT`: can only be used on integer values
  - `PRIMARY KEY` & `AUTOINCREMENT`
    - usually used on id's
    - an id number is automatically assigned to every new record inserted without a specified id.
    - the id remains unique to all records, including the deleted ones (id 1, 2, 3 중 3을 삭제한 후 새로운 레코드를 추가하면, 자동으로 4번이 부여된다.)
- other options: `DEFAULT = defaultValue`, `UNIQUE`
  - `UNIQUE`: values must be unique for each record. Multiple columns may be labeled 'UNIQUE'



## SELECT : display selected data

```sqlite
SELECT colName           # -> mandatory
FROM tableName           # -> mandatory
[WHERE colName ... ]
[ORDER BY colName]
[LIMIT int]
;
```

#### SELECT: select which columns or calculated values to display

- `SELECT *` : all columns
- `SELECT colName1, colName2` : display values of only _colName1_ and _colName2_
- `SELECT DISTINCT colName`: display all values of _colName_ after eliminating duplicates
- `SELECT COUNT(*)` : display the total number of all records
- `SELECT MAX(colName)` : display the maximum value of _colName_
- `SELECT AVG(colName)` : display the average value of _colName_

#### WHERE : set a specific condition for which records to select

- `WHERE colName = value` : `=`, `==`, `is`, `>`, `<`, `>=`, `<=` may also be used
- `WHERE colName LIKE 'The %'` : display records whose colName starts with "The "
  - `%word` : ends with "word"
  - `%word%` : includes "word"
- `WHERE colName BETWEEN 'A' and 'J'`: display records whose colName starts with a letter between "A" and "J" (INCLUSIVE of "A", NOT INCLUSIVE of "J")
- `WHERE colName BETWEEN 1 and 10`: display records whose colName is between 1 and 10 (INCLUSIVE of both 1 and 10)
- `WHERE colName1 = value1 AND colName2 = value2`: set multiple conditions with `AND` or `OR`

#### ORDER BY : sort selected records by specified columns

- `ORDER BY colName1, colName2`: _colName1_ is the primary sorting standard while _colName2_ is the secondary standard
- `ORDER BY colName1 ASC, colName2 DESC` : DESC => sort in descending order (default is ascending order)

#### LIMIT : maximum number of selected records to display

- `LIMIT 10` : display the first 10 records from the selected & sorted list
- `LIMIT 10 OFFSET 2` : display the first 10 records AFTER ignoring the first two -> Thus, display 10 records from #3 to #12



## ALTER TABLE : add, delete, or modify columns in an existing table

#### ADD COLUMN

```sqlite
ALTER TABLE tableName
ADD COLUMN colName DATATYPE;
```

#### DROP COLUMN : delete column

```sqlite
ALTER TABLE tableName
DROP COLUMN colName;
```



## INSERT INTO : add new record

```sqlite
INSERT INTO tableName (colName1, colName2)
VALUES (value1, value2);
```

- `(colName1, colName2)` may be omitted if it includes all available columns



## UPDATE : edit record

```sqlite
UPDATE tableName
SET colName1 = newValue1, colName2 = newValue2
WHERE colName = value;
```



## DELETE FROM : delete record

```sqlite
DELETE FROM tableName
WHERE colName = value;
```

- e.g) `WHERE colName IS NULL` 





## DROP TABLE : delete table

`DROP TABLE tableName`










