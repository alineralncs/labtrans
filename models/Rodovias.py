from peewee import (
    ForeignKeyField,
    DoubleField, 
    IntegerField
)
from models.BaseModel import BaseModel
from models.Results import Results
from prettytable import PrettyTable

class Rodovias(BaseModel):
    rodovia = IntegerField(unique=True)
    km_ini = DoubleField()
    km_final = DoubleField()
    class Meta:
        table_name = 'rodovias'

    @classmethod
    def create_highway(cls):
        results = Results.select()

        highway_data = {}
    
        for result in results:
            highway = result.highway
            km = result.km
            
            if highway not in highway_data:
                highway_data[highway] = {'min_km': km, 'max_km': km}
            else:
                highway_data[highway]['min_km'] = min(highway_data[highway]['min_km'], km)
                highway_data[highway]['max_km'] = max(highway_data[highway]['max_km'], km)
        
        for highway_name, data in highway_data.items():
            highway = Rodovias.create(rodovia=highway_name, km_ini=data['min_km'], km_final=data['max_km'])

    @classmethod
    def show_highways(cls):
        rodovias = Rodovias.select()
        table = PrettyTable()
        table.field_names = ["Rodovia", "Km Inicial", "Km Final"]

        for rodovia in rodovias:
            table.add_row([rodovia.rodovia, rodovia.km_ini, rodovia.km_final])

        print(table)
        return rodovias
    @classmethod
    def delete_highways(cls):
        Rodovias.delete().execute()