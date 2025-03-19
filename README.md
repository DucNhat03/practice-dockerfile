# Phần 1: Docker Commands Cheat Sheet

## 1. Kiểm tra phiên bản Docker
```sh
docker --version
```
![image](https://github.com/user-attachments/assets/3c3392d6-608b-4a20-a460-77c878002627)

## 2. Chạy container kiểm tra
```sh
docker run hello-world
```
![image](https://github.com/user-attachments/assets/ba2c258f-57d1-407a-b1d1-4edfb29f3c3a)

## 3. Tải image từ Docker Hub
```sh
docker pull nginx
```
![image](https://github.com/user-attachments/assets/11925afe-fbb6-404a-ad79-60ca58e9c89a)

## 4. Kiểm tra container chạy trên cổng 8080
```sh
# Sau khi chạy nginx, kiểm tra bằng trình duyệt:
http://localhost:8080
```
![image](https://github.com/user-attachments/assets/26899d6e-e15c-4382-90f4-29dc67464e1a)
## 5. Liệt kê danh sách images
```sh
docker images
```
![image](https://github.com/user-attachments/assets/09c96098-2a5b-4df3-a1fa-192c9d266360)

## 6. Chạy container ở chế độ nền
```sh
docker run -d nginx
```
![image](https://github.com/user-attachments/assets/7b622245-4f49-4996-a7a5-7202581c64ca)

## 7. Liệt kê container đang chạy
```sh
docker ps
```
![image](https://github.com/user-attachments/assets/dc9e9f41-0130-4a26-af86-31d8f03b0272)

## 8. Liệt kê toàn bộ container (bao gồm container đã dừng)
```sh
docker ps -a
```
![image](https://github.com/user-attachments/assets/577afa8b-d463-4a73-a28d-b1ffe9160354)

## 9. Xem logs của container
```sh
docker logs <container_id>
```
![image](https://github.com/user-attachments/assets/fd5f9a96-58b7-4a09-9327-2cf7ec193acd)

## 10. Truy cập vào container
```sh
docker exec -it <container_id> /bin/sh
```
![image](https://github.com/user-attachments/assets/737e7daf-42c5-43d8-95d6-9bf511203beb)

## 11. Dừng container
```sh
docker stop <container_id>
```
![image](https://github.com/user-attachments/assets/18ca216e-5cea-466f-aa9d-9567996bce3f)

## 12. Khởi động lại container
```sh
docker restart <container_id>
```
![image](https://github.com/user-attachments/assets/a286a175-d158-4fa3-bf24-74df7ee3c032)
#### Stop
![image](https://github.com/user-attachments/assets/997e8cc8-de59-4652-a045-9620110f6a6f)
#### Restart
![image](https://github.com/user-attachments/assets/ab9db0ce-2b66-45f8-b047-ba6cb6c2fd5b)

## 13. Xóa container
```sh
docker rm <container_id>
```
#### Để xóa, ban đầu container còn chạy -> stop container -> remove 
![image](https://github.com/user-attachments/assets/e12f4351-3384-4cc4-9f92-db603b69639d)

## 14. Xóa toàn bộ container đã dừng
```sh
docker container prune
```
#### 0B bởi vì lệnh này chỉ xóa những container đã đừng, mà crazy_swartz vẫn còn chạy, còn my-nginx đã xóa ở câu trước
![image](https://github.com/user-attachments/assets/5e09d6d1-3f7c-4bfd-ac48-ec92694adb33)

## 15. Xóa image
```sh
docker rmi <image_id>
```
#### Đầu tiên xem danh sách container -> stop container -> xóa container -> xóa image -> kiểm tra lại image, container sau khi xóa
![image](https://github.com/user-attachments/assets/0b4188e4-5b53-45de-90fd-e3169f09bd2d)


## 16. Xóa toàn bộ image không sử dụng
```sh
docker image prune -a
```
![image](https://github.com/user-attachments/assets/f6f6db32-d696-4d52-abbf-20de7b90bb9f)

## 17. Chạy container với port mapping
```sh
docker run -d -p 8080:80 nginx
```
![image](https://github.com/user-attachments/assets/b4ecfde0-4f64-4e7f-a827-172b537d558d)
#### Check port: 8080
![image](https://github.com/user-attachments/assets/90b0bb51-337c-49b5-9923-88eacea09701)


## 18. Xem thông tin chi tiết của container
```sh
docker inspect <container_id>
```
![image](https://github.com/user-attachments/assets/d5096643-651d-4f07-a899-3df5c2a613bd)
![image](https://github.com/user-attachments/assets/2a9532e1-7d71-4fd2-803c-25ba0667d36e)
![image](https://github.com/user-attachments/assets/29e9db16-b8f4-4470-8cd9-4461769aef7b)


## 19. Tạo volume và chạy container sử dụng volume
```sh
docker run -d -v mydata:/data nginx
```
#### chạy lệnh -> check lại bằng lệnh “docker volume ls”
![image](https://github.com/user-attachments/assets/52e8b5cd-4bc2-46ae-b80b-c44ec2317286)

## 20. Kiểm tra danh sách volume
```sh
docker volume ls
```
![image](https://github.com/user-attachments/assets/a5763b05-904f-4e07-9de8-e4f38f507a9c)

## 21. Xóa volume không sử dụng
```sh
docker volume prune
```
#### không xóa volume mydata vì nó đang được sử dụng 
![image](https://github.com/user-attachments/assets/e200bc11-b8d8-4f85-8d79-28a184ff22bf)

## 22. Chạy container với tên tùy chỉnh
```sh
docker run -d --name my_nginx nginx
```
![image](https://github.com/user-attachments/assets/7d7242d4-7405-41e3-a490-3358c8afec91)

## 23. Xem tài nguyên sử dụng của container
```sh
docker stats
```
![image](https://github.com/user-attachments/assets/602642ea-8ee8-461e-95e5-8fd0ee988e06)

## 24. Liệt kê danh sách network
```sh
docker network ls
```
![image](https://github.com/user-attachments/assets/63a1f306-58c3-4fba-bd82-5c76b74472e3)

## 25. Tạo network
```sh
docker network create my_network
```
#### chạy lệnh -> kiểm tra lại bằng docker network ls -> đã có network vừa tạo (my_network)
![image](https://github.com/user-attachments/assets/880692ca-f3b5-4537-bdf8-6145d6df4986)
## 26. Chạy container trong network đã tạo
```sh
docker run -d --network my_network --name my_container nginx
```
![image](https://github.com/user-attachments/assets/c4795c04-d761-4cb3-bc17-c9705c521ff3)

## 27. Kết nối container với network
```sh
docker network connect my_network my_nginx
```

#### run lệnh -> kiểm tra kết nối bằng “docker network inspect my_network”
![image](https://github.com/user-attachments/assets/d4b9703a-3eca-4656-89f9-6b0a489fe5ab)

## 28. Chạy container với biến môi trường
```sh
docker run -d -e MY_ENV=hello_world nginx
```

![image](https://github.com/user-attachments/assets/cd32316d-2c0b-4cef-bd5e-8f04fa1e5e0f)

## 29. Xem logs của container theo thời gian thực
```sh
docker logs -f my_nginx
```
![image](https://github.com/user-attachments/assets/546002f8-ecca-4d99-a779-58bf57e902c4)

## 30. Tạo Dockerfile
```Dockerfile
FROM nginx
COPY index.html /usr/share/nginx/html/index.html
```
![image](https://github.com/user-attachments/assets/23a09a40-47d8-408d-9d8c-cda87540027e)

## 31. Build image từ Dockerfile
```sh
docker build -t my_nginx_image .
```
![image](https://github.com/user-attachments/assets/07bceb98-26b9-4dc6-9224-08a49576dd3d)



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
![image](https://github.com/user-attachments/assets/220fb65b-dc80-45dc-bf93-7ddff13acc2e)

### **2. Build Docker Image**
```sh
docker build -t my-node-app .
```

---
![image](https://github.com/user-attachments/assets/97107b58-a630-4fa9-bfda-ceaaeb36a7e8)

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
```
![image](https://github.com/user-attachments/assets/405eeef4-eb19-4419-98ed-f5079f462f38)



