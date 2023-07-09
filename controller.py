from model import Results
from tornado.web import RequestHandler


class ResultsController(RequestHandler):
    def get(self):
        # Retrieve a user by ID
        qs = Results.get_highway_info()
        #resultado = Results.get_by_id(result_id)
        self.write(f"Video: {qs}")

    def post(self):
        Results.insert_data()
        response = HTTPResponse(status_code=200, body='Inseriu dados')
        self.write(response)


class ResultsExportController(RequestHandler):
    def get(self):
        # Chame o método export_data no controlador Results
        Results.export_csv()
        self.write('Exportado com sucesso')
