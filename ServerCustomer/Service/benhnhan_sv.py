from DB.db_connection import get_db_connection
from Model.bacsi import BacSi
from Model.benhnhan import BenhNhan
from Model.lichhen import LichHen
from Model.phieukham import PhieuKham
from Model.thuoc import Thuoc
from datetime import datetime
from flask_jwt_extended import create_access_token


class BenhNhanService:
    @staticmethod
    def register_benhnhan(ten, sdt, quequan, cccd, dob, img, username, password):
        """Hàm đăng ký bệnh nhân mới với xử lý ảnh"""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Kiểm tra username có tồn tại không
        check_query = "SELECT id FROM benhnhan WHERE username = %s"
        cursor.execute(check_query, (username,))
        if cursor.fetchone():
            cursor.close()
            conn.close()
            return {"success": False, "message": "Tên đăng nhập đã tồn tại"}

        # Thêm bệnh nhân vào DB
        insert_query = """
        INSERT INTO benhnhan (ten, sdt, quequan, cccd, dob, img, username, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (ten, sdt, quequan, cccd, dob, img, username, password))
        conn.commit()
        new_id = cursor.lastrowid
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
            # ✅ Tạo token cho bệnh nhân
            # access_token = create_access_token(identity=benhnhan["id"])  

            return {
                "success": True,
                # "access_token": access_token,   # 🔥 Trả về token
                "benhnhan": {
                    "id": benhnhan["id"],
                    "ten": benhnhan["ten"],
                    "sdt": benhnhan["sdt"],
                    "quequan": benhnhan["quequan"],
                    "cccd": benhnhan["cccd"],
                    "dob": benhnhan["dob"],
                    "img": benhnhan["img"],
                    "password": benhnhan["password"],
                    "username": benhnhan["username"]
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

    @staticmethod
    def update_benhnhan_info(data):

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Cập nhật các trường cần thiết (nếu dữ liệu được gửi lên)
        update_query = """
        UPDATE benhnhan
        SET ten = %s, sdt = %s, quequan = %s, cccd = %s, dob = %s, img = %s
        WHERE id = %s
        """
        cursor.execute(update_query, (
            data.get("ten"),
            data.get("sdt"),
            data.get("quequan"),
            data.get("cccd"),
            data.get("dob"),
            data.get("img"),
            data.get("id")
        ))
        conn.commit()
        cursor.close()
        conn.close()
        
        # Để đơn giản, ta trả về dữ liệu đã gửi (có thể bổ sung truy vấn lại từ DB nếu cần)
        return {"success": True, "message": "Cập nhật thành công", "benhnhan": data}

    # Trong BenhNhanService
    @staticmethod
    def get_benhnhan_image_path(benhnhan_id):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT img FROM benhnhan WHERE id = %s", (benhnhan_id,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Lỗi khi lấy đường dẫn ảnh: {str(e)}")
            return None
        finally:
            if connection:
                connection.close()
    
    @staticmethod
    def update_password(id, password):

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Cập nhật các trường cần thiết (nếu dữ liệu được gửi lên)
        update_query = """
        UPDATE benhnhan
        SET password = %s
        WHERE id = %s
        """
        cursor.execute(update_query, (
            
            password,
            id
        ))
        conn.commit()
        cursor.close()
        conn.close()
        
        # Để đơn giản, ta trả về dữ liệu đã gửi (có thể bổ sung truy vấn lại từ DB nếu cần)
        return {"success": True, "message": "Cập nhật thành công"}
    
    @staticmethod
    def get_phongkham():
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM phongchucnang")
            return {
                "success": True,
                "data": cursor.fetchall()
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Lỗi database: {str(e)}",
                "data": []
            }
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()
    
    @staticmethod
    def get_bacsi(idphong):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM bacsi WHERE phongID = %s", (idphong,))
            return {
                "success": True,
                "data": cursor.fetchall()
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Lỗi database: {str(e)}",
                "data": []
            }
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()