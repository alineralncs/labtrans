from peewee import (
    SqliteDatabase,
    Model, 
)

db = SqliteDatabase('labtrans.db')

class BaseModel(Model):
    class Meta:
        database = db 