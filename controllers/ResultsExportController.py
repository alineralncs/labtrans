from models.Results import Results
from controllers.BaseHandler import BaseHandler
import os

class ResultsExportController(BaseHandler):
    def get(self):
        Results.export_csv()
        directory = 'dados_saida'
        files = os.listdir(directory)
        self.write({'files': files})
            # self.write('Dados exportados com sucesso!')
