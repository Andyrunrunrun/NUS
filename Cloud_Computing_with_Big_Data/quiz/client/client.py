import http.client
import json
import sys


def send_request(proxy_host, proxy_port, server_host, server_port, message):
    # Create an HTTP connection to the specified server host and port
    conn = http.client.HTTPConnection(proxy_host, proxy_port)
    # Set the headers for the HTTP request
    headers = {'Content-Type': 'application/json'}
    try:
        # Send a POST request to the server with the message data
        conn.request('POST', '/',
                     json.dumps({'server_host': server_host, 'server_port': server_port, 'message': message}), headers)
        # Get the response from the server
        response = conn.getresponse()
        print('Status:', response.status, response.reason)
        data = response.read().decode()
        # Return the response as a decoded string
        return data
    except Exception as e:
        print('Error accessing proxy:', e)
    finally:
        conn.close()


if __name__ == '__main__':
    # Send a test message to the echo server and print the response
    if len(sys.argv) != 6:
        print("Usage: python script.py <proxy_host> <proxy_port> <server_host> <server_port> <message>")
        sys.exit(1)
    proxy_host = sys.argv[1]
    server_host = sys.argv[3]
    message = sys.argv[5]
    try:
        proxy_port = int(sys.argv[2])
        server_port = int(sys.argv[4])
    except ValueError:
        print("Please enter a valid port number.")
        sys.exit(1)

    response = send_request(proxy_host, proxy_port, server_host, server_port, message)
    print(f'Response from echo server: {response}')
