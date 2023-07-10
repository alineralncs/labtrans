from peewee import (
    ForeignKeyField,
    DoubleField, 
    IntegerField
)
from models.Results import BaseModel
from models.Results import Results

class Highway(BaseModel):
    rodovia = IntegerField(unique=True)
    km_ini = DoubleField()
    km_final = DoubleField()

    def create_highway():
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
            highway = Highway.create(rodovia=highway_name, km_ini=data['min_km'], km_final=data['max_km'])
            
    def show_highways():
        rodovias = Highway.select()
        for rodovia in rodovias:
            print(f"Rodovia: {rodovia.rodovia}")
            print(f"Km inicial: {rodovia.km_ini}")
            print(f"Km final: {rodovia.km_final}")
            print("--------------------")
    def delete_highways():
        Highway.delete().execute()