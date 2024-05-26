from http.server import HTTPServer, BaseHTTPRequestHandler


class EchoRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get the content length from the request headers
        content_length = int(self.headers['Content-Length'])
        # Read the specified amount of data from the request
        body = self.rfile.read(content_length)
        # Send a 200 OK response
        self.send_response(200)
        self.end_headers()
        # Echo the received data back in the response
        self.wfile.write(body)


if __name__ == '__main__':
    server_address = ('0.0.0.0', 8080)
    # Create an HTTP server with the custom request handler
    httpd = HTTPServer(server_address, EchoRequestHandler)
    print('Starting the echo server...')
    httpd.serve_forever()
