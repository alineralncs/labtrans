from models.Results import Results
from tornado.web import RequestHandler


class ResultsController(RequestHandler):
    def get(self):
        qs = Results.select()
        self.write(f"Resultados: {qs}")
