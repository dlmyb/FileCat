from gevent.wsgi import WSGIServer
from app import app

http_server = WSGIServer(('', 9611), app)
http_server.serve_forever()
