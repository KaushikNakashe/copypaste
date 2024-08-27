from gryphos_app.config import Config
from gryphos_app import App
from flask import request
from flask import send_from_directory
from werkzeug.utils import send_from_directory
from werkzeug.serving import WSGIRequestHandler
import warnings
warnings.filterwarnings("ignore")

app = App().create_app()
class CustomRequestHandler(WSGIRequestHandler):
    def connection_dropped(self, error, environ=None):
        return ConnectionAbortedError

@app.route('/static/<path:path>')
def serve_file(path):
    return send_from_directory('', path, environ=request.environ)

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT ,debug=True,request_handler=CustomRequestHandler)



