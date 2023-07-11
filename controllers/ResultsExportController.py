from models.Results import Results
from tornado.web import RequestHandler

class ResultsExportController(RequestHandler):
    def get(self):
        Results.export_csv()
        self.write('Dados exportados com sucesso!')
