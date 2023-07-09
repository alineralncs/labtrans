from tornado.web import Application
from controller import ResultsController, ResultsExportController
import tornado.ioloop
from tornado.web import URLSpec

app = Application([
    (r"/results/", ResultsController),  
    (r"/results/export", ResultsExportController)  # Rota para exportar dados


])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()