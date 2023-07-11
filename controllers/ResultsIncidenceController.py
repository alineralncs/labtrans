from models.Results import Results
from controllers.BaseHandler import BaseHandler
import json


class ResultsIncidenceController(BaseHandler):
    def get(self, item ):
        print("Você selecionou a Opção 4 - Consultar Incidência por KM ")
        km_maior_incidencia, incidencia, rodovia = Results.find_incidence(item)
        print(f"O quilômetro com maior incidência de {item} é na rodovia {rodovia} e no km: {km_maior_incidencia}, com {incidencia} ocorrências.")
        response_data = {
            "km_maior_incidencia": km_maior_incidencia,
            "incidencia": incidencia,
            "rodovia": rodovia
        }

        # Convert the dictionary to JSON
        json_data = json.dumps(response_data, indent=4)

        # Set the response headers
        self.set_header("Content-Type", "application/json")

        # Write the JSON response
        self.write(json_data)