# 基于的基础镜像
FROM python:3.12.5

# 将代码添加到/code文件夹
ADD . .

# 设置/code文件夹为工作目录
WORKDIR /sign98

# 安装项目依赖
COPY requirements.txt /tmp/requirements.txt
# RUN ["pip", "install", "-r", "/tmp/requirements.txt"]
RUN ["pip", "install", "-r", "/tmp/requirements.txt" , "-i" , "https://pypi.tuna.tsinghua.edu.cn/simple"]

# 运行Python脚本
CMD ["python","-u", "./src/main.py"]