from server import app
from gryphos_app.config import Config

if __name__=="__main__":
    app.run(host=Config.HOST, port=Config.PORT ,debug=True,request_handler=app.CustomRequestHandler)