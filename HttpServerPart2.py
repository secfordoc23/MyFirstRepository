#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT_NUMBER = 11337

class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if  self.path == '/{0}'.format(os.environ.get('level_1_secret_token')):
            self.wfile.write(bytes('<html><head><title>Correct Code</title></head><body><h1>Correct Code</h1><p>Level 2 Token: {0}</p></body></html>'.format(os.environ.get('level_2_secret_token')), "utf-8"))
        else:
            self.wfile.write(bytes(
                '<html><head><title>Nothing to see here</title></head><body><h1>Nothing here</h1><p>Nothing to see here</p></body></html>',
                "utf-8"))

        return

try:
    server = HTTPServer(('', PORT_NUMBER), HttpHandler)
    print('Webserver listening for HTTP request on:', PORT_NUMBER)
    server.serve_forever()

except Exception as err:
    print(err)
