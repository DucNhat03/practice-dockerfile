# Docker Commands Cheat Sheet

## 1. Kiểm tra phiên bản Docker
```sh
docker --version
```

## 2. Chạy container kiểm tra
```sh
docker run hello-world
```

## 3. Tải image từ Docker Hub
```sh
docker pull nginx
```

## 4. Kiểm tra container chạy trên cổng 8080
```sh
# Sau khi chạy nginx, kiểm tra bằng trình duyệt:
http://localhost:8080
```

## 5. Liệt kê danh sách images
```sh
docker images
```

## 6. Chạy container ở chế độ nền
```sh
docker run -d nginx
```

## 7. Liệt kê container đang chạy
```sh
docker ps
```

## 8. Liệt kê toàn bộ container (bao gồm container đã dừng)
```sh
docker ps -a
```

## 9. Xem logs của container
```sh
docker logs <container_id>
```

## 10. Truy cập vào container
```sh
docker exec -it <container_id> /bin/sh
```

## 11. Dừng container
```sh
docker stop <container_id>
```

## 12. Khởi động lại container
```sh
docker restart <container_id>
```

## 13. Xóa container
```sh
docker rm <container_id>
```

## 14. Xóa toàn bộ container đã dừng
```sh
docker container prune
```

## 15. Xóa image
```sh
docker rmi <image_id>
```

## 16. Xóa toàn bộ image không sử dụng
```sh
docker image prune -a
```

## 17. Chạy container với port mapping
```sh
docker run -d -p 8080:80 nginx
```

## 18. Xem thông tin chi tiết của container
```sh
docker inspect <container_id>
```

## 19. Tạo volume và chạy container sử dụng volume
```sh
docker run -d -v mydata:/data nginx
```

## 20. Kiểm tra danh sách volume
```sh
docker volume ls
```

## 21. Xóa volume không sử dụng
```sh
docker volume prune
```

## 22. Chạy container với tên tùy chỉnh
```sh
docker run -d --name my_nginx nginx
```

## 23. Xem tài nguyên sử dụng của container
```sh
docker stats
```

## 24. Liệt kê danh sách network
```sh
docker network ls
```

## 25. Tạo network
```sh
docker network create my_network
```

## 26. Chạy container trong network đã tạo
```sh
docker run -d --network my_network --name my_container nginx
```

## 27. Kết nối container với network
```sh
docker network connect my_network my_nginx
```

## 28. Chạy container với biến môi trường
```sh
docker run -d -e MY_ENV=hello_world nginx
```

## 29. Xem logs của container theo thời gian thực
```sh
docker logs -f my_nginx
```

## 30. Tạo Dockerfile
```Dockerfile
FROM nginx
COPY index.html /usr/share/nginx/html/index.html
```

## 31. Build image từ Dockerfile
```sh
docker build -t my_nginx_image .
```

## 32. Chạy container từ image vừa build
```sh
docker run -d -p 8080:80 my_nginx_image
