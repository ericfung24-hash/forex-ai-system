# ✅ 固定 Python 版本（关键）
FROM python:3.11-slim

# 工作目录
WORKDIR /app

# 复制所有文件
COPY . .

# 安装依赖
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 启动服务
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
