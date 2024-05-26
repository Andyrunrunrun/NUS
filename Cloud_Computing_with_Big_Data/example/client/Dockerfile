# 使用 Python 3.8 slim 版本作为基础镜像
FROM python:3.8-slim
 # 将本地的 client.py 文件复制到容器中的根目录下
COPY client.py /client.py
# 在容器启动时执行的命令，让容器休眠 60 秒
CMD ["sh", "-c", "sleep 3600"]
