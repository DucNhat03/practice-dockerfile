# Sử dụng Python 3.9 làm base image
FROM python:3.9

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy file vào container
COPY app.py .
COPY requirements.txt .

# Cài đặt dependencies
RUN pip install -r requirements.txt

# Thiết lập biến môi trường mặc định
ENV APP_ENV=development

# Chạy ứng dụng
CMD ["python", "app.py"]
