from models.Rodovias import Rodovias
from controllers.BaseHandler import BaseHandler
import json 

class RodoviasController(BaseHandler):
    def get(self):
        # Rodovias.delete_highways()
        # Rodovias.create_highway()
        show_highways = Rodovias.show_highways()
        dict_highway = []
        
        for highway in show_highways:
            dict_h = {}
            dict_h['nome'] = highway.rodovia
            dict_h['km_ini'] = highway.km_ini
            dict_h['km_final'] = highway.km_final
            dict_highway.append(dict_h)

        json_data = json.dumps(dict_highway, indent=4)

        self.set_header("Content-Type", "application/json")

        self.write(json_data)
        
