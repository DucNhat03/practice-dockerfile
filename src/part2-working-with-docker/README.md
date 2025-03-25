# Phần 2: Thao tác với Dockerfile

## Bài 1: Tạo Dockerfile chạy một ứng dụng Node.js đơn giản

### Yêu cầu:  
- Viết Dockerfile để chạy một ứng dụng Node.js hiển thị "Hello, Docker!" trên cổng 3000.  
- Sử dụng `node:18` làm base image.

### **1. Setup**
Tạo một thư mục mới và thêm các file sau:

#### **app.js**
```javascript
const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
    res.send('Hello, Docker!');
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

#### **package.json**
```json
{
  "name": "docker-node-app",
  "version": "1.0.0",
  "main": "app.js",
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

#### **Dockerfile**
```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
```

### **2. Build Docker Image**
```sh
docker build -t my-node-app .
```

### **3. Run Docker Container**
```sh
docker run -p 3000:3000 my-node-app
```

---

## Bài 2: Tạo Dockerfile chạy một ứng dụng Python Flask  

### **1. Setup**
#### **app.py**
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker Flask!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

#### **requirements.txt**
```
flask
```

#### **Dockerfile**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### **2. Build & Run**
```sh
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

Truy cập: [http://localhost:5000](http://localhost:5000)

---

## Bài 3: Tạo Dockerfile chạy ứng dụng React

### **1. Setup**
#### **Dockerfile**
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build
RUN npm install -g serve
EXPOSE 3000
CMD ["serve", "-s", "build", "-l", "3000"]
```

### **2. Build & Run**
```sh
docker build -t react-app .
docker run -p 3000:3000 react-app
```

---

## Bài 4: Chạy trang web tĩnh với Nginx

### **1. Setup**
#### **index.html**
```html
<h1>Hello, Docker with Nginx!</h1>
```

#### **Dockerfile**
```dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
```

### **2. Build & Run**
```sh
docker build -t nginx-site .
docker run -p 8080:80 nginx-site
```

Truy cập: [http://localhost:8080](http://localhost:8080)

---

## Bài 5: Chạy ứng dụng Go

### **1. Setup**
#### **main.go**
```go
package main
import (
    "fmt"
    "net/http"
)
func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, Docker with Go!")
}
func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}
```

#### **Dockerfile**
```dockerfile
FROM golang:1.20
WORKDIR /app
COPY . .
RUN go build -o main .
EXPOSE 8080
CMD ["./main"]
```

### **2. Build & Run**
```sh
docker build -t go-app .
docker run -p 8080:8080 go-app
```

---

## Bài 6: Multi-stage Build với Node.js

### **1. Setup**
#### **Dockerfile**
```dockerfile
FROM node:18 AS builder
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app .
EXPOSE 3000
CMD ["node", "server.js"]
```

### **2. Build & Run**
```sh
docker build -t node-multi-stage .
docker run -p 3000:3000 node-multi-stage
```

---

## Bài 7: Sử dụng biến môi trường trong Dockerfile

### **1. Setup**
#### **Dockerfile**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY app.py .
ENV APP_ENV=development
CMD ["python", "app.py"]
```

### **2. Build & Run**
```sh
docker build -t python-env-app .
docker run --rm python-env-app
```

---

## Bài 8: Dockerfile cho PostgreSQL

### **1. Setup**
#### **init.sql**
```sql
CREATE DATABASE my_database;
CREATE USER my_user WITH ENCRYPTED PASSWORD 'my_password';
GRANT ALL PRIVILEGES ON DATABASE my_database TO my_user;
```

#### **Dockerfile**
```dockerfile
FROM postgres:15
COPY init.sql /docker-entrypoint-initdb.d/
EXPOSE 5432
```

### **2. Build & Run**
```sh
docker build -t custom-postgres .
docker run -p 5432:5432 custom-postgres
```

Truy cập PostgreSQL: `psql -U my_user -d my_database`

---


