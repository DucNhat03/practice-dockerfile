# Phần 2: Thao tác với Dockerfile

## Bài 1: Tạo Dockerfile chạy một ứng dụng Node.js đơn giản

### Yêu cầu:  
- Viết Dockerfile để chạy một ứng dụng Node.js hiển thị "Hello, Docker!" trên cổng 3000.  
- Sử dụng `node:18` làm base image.

---

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
# Sử dụng node:18 làm base image
FROM node:18

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy file package.json và package-lock.json
COPY package*.json ./

# Cài đặt dependencies
RUN npm install

# Copy toàn bộ mã nguồn vào container
COPY . .

# Expose cổng 3000
EXPOSE 3000

# Lệnh chạy ứng dụng
CMD ["node", "app.js"]
```

---

### **2. Build Docker Image**
```sh
docker build -t my-node-app .
```

---

### **3. Test Docker Container**
Chạy container từ image đã build:
```sh
docker run -d -p 3000:3000 my-node-app
```

Kiểm tra ứng dụng bằng trình duyệt hoặc cURL:
```sh
curl http://localhost:3000
```

Nếu thành công, bạn sẽ thấy thông báo:
```
Hello, Docker!