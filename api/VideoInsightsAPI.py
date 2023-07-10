from models.Results import Results
from tornado.web import Application
from controllers.ResultsController import ResultsController
from controllers.ResultsCreateController import ResultsCreateController
from controllers.ResultsExportController import ResultsExportController
import tornado.ioloop

Results.create_table()

app = Application([
    (r"/results/", ResultsController),  
    (r"/results/create", ResultsCreateController),  
    (r"/results/export", ResultsExportController)  # Rota para exportar dados
])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


