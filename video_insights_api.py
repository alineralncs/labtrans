from tornado.web import Application
from controllers.ResultsCreateController import ResultsCreateController
from controllers.ResultsExportController import ResultsExportController
from controllers.ResultsController import ResultsController
from controllers.ResultsFileDownload import ResultsFileDownload
from controllers.ResultsIncidenceController import ResultsIncidenceController
from controllers.VideosController import VideosController
from controllers.RodoviasController import RodoviasController

import tornado.ioloop


app = Application([
    (r"/results/", ResultsController),  
    (r"/results/create", ResultsCreateController),  
    (r"/results/files", ResultsExportController),
    (r"/files/download/(.*)", ResultsFileDownload, {'directory': 'dados_saida'}),
    (r"/results/incidence/([\w\s]+)", ResultsIncidenceController),
    (r"/videos/", VideosController),
    (r"/rodovias/", RodoviasController),

])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


