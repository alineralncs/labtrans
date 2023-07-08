from peewee import (
    Model, 
    SqliteDatabase, 
    TextField,
    IntegerField,
    DoubleField	
)

db = SqliteDatabase('results.db')

class BaseModel(Model):
    class Meta:
        database = db 

class Results(BaseModel):
    name = TextField()
    km = DoubleField()
    distance = DoubleField()
    highway = IntegerField()
    item = TextField()

Results.create_table()