from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # 当收到 GET 请求时调用
    def do_GET(self):
        # 发送 HTTP 200 响应
        self.send_response(200)
        # 设置响应头的 Content-type 为 text/plain
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        # 返回 "Hello World" 作为响应内容
        self.wfile.write(b"Hello World")


if __name__ == '__main__':
    httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
    httpd.serve_forever()    # 启动服务器并持续运行，处理传入的请求

#它创建了一个简单的 HTTP 请求处理程序，以处理 GET 请求并返回 "Hello World" 作为响应。
# 然后，它创建一个 HTTPServer 实例，并将其绑定到本地地址 0.0.0.0 和端口 8080。
# 最后，它调用 serve_forever() 方法，以便处理传入的请求。