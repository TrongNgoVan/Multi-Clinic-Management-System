from DB.db_connection import get_db_connection
from Model.bacsi import BacSi
from Model.benhnhan import BenhNhan
from Model.lichhen import LichHen
from Model.phieukham import PhieuKham
from Model.thuoc import Thuoc
from datetime import datetime


class BenhNhanService:
    @staticmethod
    def register_benhnhan(ten, sdt, quequan, cccd, dob, img, username, password):
        """Hàm đăng ký bệnh nhân mới"""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Kiểm tra xem username đã tồn tại chưa
        check_query = "SELECT id FROM benhnhan WHERE username = %s"
        cursor.execute(check_query, (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            cursor.close()
            conn.close()
            return {"success": False, "message": "Tên đăng nhập đã tồn tại"}

        # Chèn bệnh nhân mới vào database
        insert_query = """
        INSERT INTO benhnhan (ten, sdt, quequan, cccd, dob, img, username, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (ten, sdt, quequan, cccd, dob, img, username, password))
        conn.commit()

        new_id = cursor.lastrowid  # Lấy ID vừa chèn vào
        cursor.close()
        conn.close()

        return {"success": True, "message": "Đăng ký thành công", "benhnhan_id": new_id}

    @staticmethod
    def login_benhnhan(username, password):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM benhnhan WHERE username = %s"
        cursor.execute(query, (username,))
        benhnhan = cursor.fetchone()
        cursor.close()
        conn.close()

        if benhnhan and benhnhan["password"] == password:
            return {
                "success": True,
                "benhnhan": {
                    "id": benhnhan["id"],
                    "ten": benhnhan["ten"],
                    "sdt": benhnhan["sdt"],
                    "quequan": benhnhan["quequan"],
                    "cccd": benhnhan["cccd"],
                    "dob": benhnhan["dob"],
                    "img": benhnhan["img"],
                    "username": benhnhan["username"],
                    "password": benhnhan["password"]
                }
            }
        else:
            return {"success": False, "message": "Tên đăng nhập hoặc mật khẩu không đúng"}
    
    @staticmethod
    def get_all_benhnhan():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM benhnhan"
        cursor.execute(query)
        benhnhans = cursor.fetchall()
        cursor.close()
        conn.close()

        # Chuyển đổi định dạng ngày tháng
        for benhnhan in benhnhans:
            if isinstance(benhnhan["dob"], datetime):  # Kiểm tra kiểu dữ liệu
                benhnhan["dob"] = benhnhan["dob"].strftime("%Y-%m-%d")  # Định dạng YYYY-MM-DD

        return {"success": True, "data": benhnhans}