import os 
from controllers.BaseHandler import BaseHandler
import pandas as pd
class ResultsFileDownload(BaseHandler):
    def initialize(self, directory):
        self.directory = directory

    def get(self, filename):
        file_path = os.path.join(self.directory, filename)
        
        if os.path.exists(file_path):
            self.set_header('Content-Type', 'text/csv')
            self.set_header('Content-Disposition', f'attachment; filename="{filename}"')

            df = pd.read_csv(file_path)
            csv_data = df.to_csv(index=False)
            self.write(csv_data)
        else:
            self.send_error(404)