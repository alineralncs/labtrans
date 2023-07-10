from peewee import (
    ForeignKeyField,
    DoubleField
)
from Results import BaseModel

class Highways(BaseModel):
    km_ini = DoubleField()
    km_final = DoubleField()