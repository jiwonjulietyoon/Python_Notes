### *) Relevant files

- `models.py`
- `db.sqlite3`





# Create DB Table (Model) 

### In `models.py`:

```python
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    def __repr__(self):
        return f"제목: {self.title}, 내용: {self.content}"
    def __str__(self):
        return f"제목: {self.title}, 내용: {self.content}"
```

- Name of table is automatically created as `Article` => same as class name
- column `id` is automatically created (if not already included in the above class definition)
- `def __repr__(self)`: return value is printed when attempting to access the data record itself
- `def __str__(self)`: return value is printed when attempting to print the data record



# Add Model to DB

















