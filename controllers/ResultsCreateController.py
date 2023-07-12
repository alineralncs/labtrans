from models.Results import Results
from controllers.BaseHandler import BaseHandler

class ResultsCreateController(BaseHandler):
    def post(self):
        Results.delete_results()
        Results.insert_data()
        self.write('Tabela Results populada com dados do csv!')