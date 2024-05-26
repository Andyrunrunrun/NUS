#使用 Python 3.8-slim 作为基础镜像
FROM python:3.8-slim
#将服务器端的 Python 文件复制到镜像中
COPY server.py /server.py
#将客户端的 Python 文件复制到镜像中
COPY client.py /client.py
#将容器内的 8080 端口暴露出来，供外部访问
EXPOSE 8080
#在容器启动时运行 Python server.py 文件作为服务
CMD ["python", "/server.py"]
