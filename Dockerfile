FROM python:3.9
# 工作目录路径
WORKDIR /usr/src/model_deploy_demo

# 配置环境
COPY requirements.txt ./
# 安装配置环境
RUN pip install -r requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# 复制文件夹
COPY model_api ./

EXPOSE 5000
# 直接运行文件
CMD ["python3","./flask_manager.py"]
