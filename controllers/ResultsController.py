from models.Results import Results
from tornado.web import RequestHandler


class ResultsController(RequestHandler):
    def get(self):
        qs = Results.get_highway_info()
        self.write(f"Video: {qs}")
