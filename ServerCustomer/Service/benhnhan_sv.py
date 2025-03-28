from DB.db_connection import get_db_connection
from Model.bacsi import BacSi
from Model.benhnhan import BenhNhan
from Model.lichhen import LichHen
from Model.phieukham import PhieuKham
from Model.thuoc import Thuoc


class BenhNhanService:
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