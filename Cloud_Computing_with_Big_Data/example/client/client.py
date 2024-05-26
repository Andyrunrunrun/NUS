import http.client
import sys


def get_hello_world(host, port):
    # 创建HTTP连接
    connection = http.client.HTTPConnection(host, port)
    try:
        # 发送GET请求
        connection.request('GET', '/')
        # 获取响应
        response = connection.getresponse()
        print('Status:', response.status, response.reason)
        data = response.read()
        print('Response from server:', data.decode())
    except Exception as e:
        # 打印访问服务器时的错误
        print('Error accessing server:', e)
    finally:
        # 关闭连接
        connection.close()


if __name__ == '__main__':
    # 检查命令行参数数量
    if len(sys.argv) != 3:
        print("Usage: python script.py <host> <port>")
        sys.exit(1)
    # 从命令行参数中获取主机和端口
    host = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except ValueError:
        # 检查端口参数是否为有效数字
        print("Please enter a valid port number.")
        sys.exit(1)
    # 调用函数发送GET请求
    get_hello_world(host, port)
