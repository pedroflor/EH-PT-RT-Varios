"""
1) Ubicarse en el directorio que se desea publicar contenido.
2) Ejecutar desde linea de comandos ó
3) Convertir a .exe y ejecutar en un Windows SIN python.
"""

###
### Simple
###
python2 -m SimpleHTTPServer 8000


###
### One liner
###
python2 -c 'import SimpleHTTPServer,SocketServer;PORT = 8000; Handler = SimpleHTTPServer.SimpleHTTPRequestHandler; httpd = SocketServer.TCPServer(("", PORT), Handler); print "serving at port", PORT; httpd.serve_forever()'


###
### Multiple lines
###
import SimpleHTTPServer
import SocketServer

PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()



