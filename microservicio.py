from http import server
import json
from ssl import SSL_ERROR_INVALID_ERROR_CODE
from tracemalloc import start
from urllib import response
from wsgiref import headers
from wsgiref.simple_server import make_server
app = (__name__)

def application (environ,start_response):
    haeaders = [('Content-type','application/json')]
    status = '200 OK'
    output = 'Hola desarrolladores TdeA estoy en el server!'
    
    start_response(status,headers)
    
    response = {'mensaje': output}
    
    return [bytes(json.dumps(response),'utf8')]

server = make_server('localhost',7000,application)
server.handle_request()


app.run(debug=True)