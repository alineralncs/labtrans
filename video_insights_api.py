from tornado.web import Application
from controllers.ResultsCreateController import ResultsCreateController
from controllers.ResultsExportController import ResultsExportController
from controllers.ResultsController import ResultsController
from controllers.ResultsIncidenceController import ResultsIncidenceController
import tornado.ioloop


app = Application([
    (r"/results/", ResultsController),  
    (r"/results/create", ResultsCreateController),  
    (r"/results/export", ResultsExportController),
    (r"/results/incidence/([\w\s]+)", ResultsIncidenceController)  # Rota para exportar dados
])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


