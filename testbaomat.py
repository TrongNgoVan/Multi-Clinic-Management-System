import requests
from concurrent.futures import ThreadPoolExecutor
import time

# URL bạn muốn gửi đến
TARGET_URL = 'http://26.80.253.0:8080/api/benhnhan/phongkham'

def send_request(i):
    try:
        response = requests.get(TARGET_URL)
        print(f"[{i}] Status: {response.status_code}")
    except Exception as e:
        print(f"[{i}] Lỗi: {e}")

# Gửi 5 request cùng lúc (song song)
while True:
    with ThreadPoolExecutor(max_workers=15) as executor:
        for i in range(5):
            executor.submit(send_request, i + 1)
    
    time.sleep(55)  # Đợi 1 giây rồi tiếp tục batch mới
