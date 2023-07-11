from models.Results import Results
from tornado.web import RequestHandler
from tornado.httpclient import HTTPResponse 

class ResultsCreateController(RequestHandler):
    def post(self):
        Results.delete_results()
        Results.insert_data()
        self.write('Tabela Results populada com dados do csv!')