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
    @staticmethod
    def add_lichhen(data):
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            query = """
                INSERT INTO lichhen (bacsiID, benhnhanID, thoigianhen, ghichu)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (data.get("bacsiID"), data.get("benhnhanID"), data.get("thoigian"), data.get("ghichu")))
            conn.commit()
            return {"success": True, "message": "Tạo lịch hẹn thành công"}
        except Exception as e:
            return {"success": False, "message": f"Lỗi khi tạo lịch hẹn: {str(e)}"}
        finally:
            if 'cursor' in locals(): cursor.close()
            if 'conn' in locals(): conn.close()
    
    @staticmethod
    def get_lichhen(benhnhanID):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT lichhen.id, lichhen.thoigianhen, lichhen.ghichu, lichhen.trangthai,
                   bacsi.id as bacsi_id, bacsi.ten as bacsi_ten, bacsi.dob as bacsi_dob, bacsi.chuyenmon as bacsi_chuyenmon, bacsi.hocvan as bacsi_hocvan, bacsi.kinhnghiem as bacsi_kinhnghiem, bacsi.img as bacsi_img, 
                   benhnhan.id as benhnhan_id
            FROM lichhen
            JOIN benhnhan ON lichhen.benhnhanID = benhnhan.id
            JOIN bacsi ON lichhen.bacsiID = bacsi.id
            WHERE lichhen.benhnhanID = %s
        """
        cursor.execute(query, (benhnhanID,))
        lichhen_list = []
        for row in cursor.fetchall():
            bacsi = BacSi(id=row["bacsi_id"], ten=row["bacsi_ten"], dob=row["bacsi_dob"], chuyenmon=row["bacsi_chuyenmon"], hocvan=row["bacsi_hocvan"], kinhnghiem=row["bacsi_kinhnghiem"], img=row["bacsi_img"],  phongID=None, username=None, password=None)
            benhnhan = BenhNhan(id=row["benhnhan_id"], ten=None, sdt=None, quequan=None, cccd=None, dob=None, img=None, username=None, password=None)
            lichhen = LichHen(id=row["id"], Bacsi=bacsi, BenhNhan=benhnhan, ghichu = row["ghichu"],thoigianhen=row["thoigianhen"], trangthai=row["trangthai"])
            lichhen_list.append(lichhen)
        cursor.close()
        conn.close()
        return lichhen_list

    @staticmethod
    def get_donthuoc(benhnhanID):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            # Bước 1: Lấy danh sách đơn thuốc chính
            cursor.execute("""
                SELECT 
                    dt.ID,
                    dt.ngaymua,
                    dt.tonggia,
                    dt.mota,
                    dt.bacsiID,
                    bs.ten AS ten_bacsi
                FROM donthuoc dt
                JOIN bacsi bs ON dt.bacsiID = bs.id
                WHERE dt.benhnhanID = %s
                ORDER BY dt.ngaymua DESC
            """, (benhnhanID,))
            
            donthuoc_list = cursor.fetchall()
            if not donthuoc_list:
                return []

            # Bước 2: Lấy chi tiết từng đơn thuốc
            for donthuoc in donthuoc_list:
                # Truy vấn chi tiết thuốc
                cursor.execute("""
                    SELECT 
                        ct.soluong,
                        ct.gia,
                        t.id AS thuoc_id,
                        t.ten AS ten_thuoc,
                        t.mota AS mota_thuoc,
                        t.nsx,
                        t.hsd,
                        t.dongia,
                        t.img
                    FROM chitietdonthuoc ct
                    JOIN thuoc t ON ct.thuocID = t.id
                    WHERE ct.donthuocID = %s
                """, (donthuoc["ID"],))
                
                # Đóng gói chi tiết vào đơn thuốc
                chitiet = cursor.fetchall()
                donthuoc["chitiet"] = [
                    {
                        "thuoc_id": item["thuoc_id"],
                        "ten_thuoc": item["ten_thuoc"],
                        "soluong": item["soluong"],
                        "gia": item["gia"],
                        "mota_thuoc": item["mota_thuoc"],
                        "nsx": item["nsx"].strftime("%d/%m/%Y") if item["nsx"] else None,
                        "hsd": item["hsd"].strftime("%d/%m/%Y") if item["hsd"] else None,
                        "dongia": item["dongia"],
                        "img": item["img"]
                    }
                    for item in chitiet
                ]

            # Định dạng lại ngày tháng cho đơn thuốc
            for donthuoc in donthuoc_list:
                donthuoc["ngaymua"] = donthuoc["ngaymua"].strftime("%d/%m/%Y %H:%M:%S") if donthuoc["ngaymua"] else None

            return donthuoc_list

        except Exception as e:
            print(f"[LỖI] Không thể lấy đơn thuốc: {str(e)}")
            return None

        finally:
            if conn:
                conn.close()