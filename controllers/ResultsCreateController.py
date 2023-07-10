from models.Results import Results
from tornado.web import RequestHandler
from tornado.httpclient import HTTPResponse 

class ResultsCreateController(RequestHandler):
    def post(self):
        Results.insert_data()
        self.write('Inseriu dados')