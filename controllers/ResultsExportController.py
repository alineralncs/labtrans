from models.Results import Results
from tornado.web import RequestHandler

class ResultsExportController(RequestHandler):
    def get(self):
        # Chame o método export_data no controlador Results
        Results.export_csv()
        self.write('Exportado com sucesso')
