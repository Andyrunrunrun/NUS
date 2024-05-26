import http.client
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys


class ProxyServer:
    # Class to handle the proxy server functionality
    def handle_request(self, client_request):
        # Method to handle the incoming client request
        content_length = int(client_request.headers['Content-Length'])
        # Read the request body
        request_body = client_request.rfile.read(content_length).decode()
        request_data = json.loads(request_body)
        # Extract the server host and port from the request data
        echo_server_host = request_data['server_host']
        echo_server_port = request_data['server_port']
        # Extract the message from the request data
        message = request_data['message']
        # Forward the message to the Echo server
        conn = http.client.HTTPConnection(echo_server_host, echo_server_port)
        conn.request('POST', '/', message)
        echo_server_response = conn.getresponse()
        response_message = echo_server_response.read().decode()

        # Return the response to the client
        client_request.send_response(200)
        client_request.end_headers()
        client_request.wfile.write(response_message.encode())


if __name__ == '__main__':
    # Create an instance of the ProxyServer class and specify the echo server host and port
    proxy_server = ProxyServer()
    print('Starting the proxy server...')


    # Define a custom request handler by subclassing BaseHTTPRequestHandler
    class ProxyRequestHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            # Handle POST requests by calling the handle_request method of the proxy_server
            proxy_server.handle_request(self)


    # Specify the address and port for the proxy server
    proxy_address = ('0.0.0.0', 8888)
    httpd = HTTPServer(proxy_address, ProxyRequestHandler)
    httpd.serve_forever()
