# ===== Stage 1: Build dependencies =====
FROM node:18 AS builder
WORKDIR /app

# Copy package.json và package-lock.json trước
COPY package.json package-lock.json ./

# Cài đặt dependencies
RUN npm install --production

# Copy toàn bộ source code
COPY . .

# ===== Stage 2: Chạy ứng dụng với Node.js Alpine =====
FROM node:18-alpine
WORKDIR /app

# Copy node_modules từ stage 1
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/server.js ./server.js

# Expose cổng ứng dụng
EXPOSE 3000

# Chạy ứng dụng
CMD ["npm", "start"]
