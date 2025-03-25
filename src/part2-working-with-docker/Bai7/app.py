import os

app_env = os.getenv("APP_ENV", "production")  # Lấy biến môi trường APP_ENV, mặc định là "production"
print(f"Application is running in {app_env} mode.")
