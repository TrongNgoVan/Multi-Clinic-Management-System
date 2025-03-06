import requests

BASE_URL = "http://127.0.0.1:5000"  # Thay đổi nếu Flask chạy trên cổng khác

def test_get_all_bacsi():
    url = f"{BASE_URL}/get_all_bacsi"
    response = requests.get(url)

    if response.status_code == 200:
        print("✅ API get_all_bacsi hoạt động tốt!")
        print(response.json())  # In dữ liệu bác sĩ lấy được
    else:
        print(f"❌ Lỗi API get_all_bacsi: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    test_get_all_bacsi()
