import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="phongkhamptit",
            charset="utf8mb4"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Lỗi kết nối MySQL: {err}")
        return None

def test_connection():
    conn = get_db_connection()
    if conn:
        print("✅ Kết nối MySQL thành công!")
        conn.close()
    else:
        print("❌ Kết nối MySQL thất bại!")

# Chạy kiểm tra kết nối
if __name__ == "__main__":
    test_connection()
