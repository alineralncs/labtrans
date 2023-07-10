from peewee import (
    ForeignKeyField,
    DoubleField
)
from Results import BaseModel

class Videos(BaseModel):
    km_ini = DoubleField()
    km_final = DoubleField()

