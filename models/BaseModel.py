from peewee import (
    SqliteDatabase,
    Model, 
)

db = SqliteDatabase('results.db')

class BaseModel(Model):
    class Meta:
        database = db 