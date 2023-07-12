from peewee import (
    ForeignKeyField,
    DoubleField, 
    IntegerField
)
from models.BaseModel import BaseModel
from models.Results import Results

class Rodovias(BaseModel):
    rodovia = IntegerField(unique=True)
    km_ini = DoubleField()
    km_final = DoubleField()
    
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
        for rodovia in rodovias:
            print(f"Rodovia: {rodovia.rodovia}")
            print(f"Km inicial: {rodovia.km_ini}")
            print(f"Km final: {rodovia.km_final}")
            print("--------------------")
        return rodovias
    @classmethod
    def delete_highways(cls):
        Rodovias.delete().execute()