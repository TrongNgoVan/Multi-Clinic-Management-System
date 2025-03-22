from BackEnd.DB.db_connection import get_db_connection
from BackEnd.Model.bacsi import BacSi
from BackEnd.Model.benhnhan import BenhNhan
from BackEnd.Model.lichhen import LichHen
from BackEnd.Model.phieukham import PhieuKham
from BackEnd.Model.thuoc import Thuoc

class BacSiService:

    @staticmethod
    def get_all_bacsi():
        """Lấy danh sách tất cả bác sĩ từ DB."""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM bacsi")
        bacsi_list = [BacSi(**row) for row in cursor.fetchall()]  # Tạo danh sách đối tượng BacSi
        cursor.close()
        conn.close()
        return bacsi_list





    @staticmethod
    def get_all_lichhen(bacsiID):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT lichhen.id, lichhen.thoigianhen, 
                   bacsi.id as bacsi_id, bacsi.ten as bacsi_ten, 
                   benhnhan.id as benhnhan_id, benhnhan.ten as benhnhan_ten, benhnhan.dob as benhnhan_dob, 
                   benhnhan.cccd as benhnhan_cccd, benhnhan.sdt as benhnhan_sdt, benhnhan.quequan as benhnhan_quequan, benhnhan.img as benhnhan_img
            FROM lichhen
            JOIN bacsi ON lichhen.bacsiID = bacsi.id
            JOIN benhnhan ON lichhen.benhnhanID = benhnhan.id
            WHERE lichhen.bacsiID = %s
        """
        cursor.execute(query, (bacsiID,))
        lichhen_list = []
        for row in cursor.fetchall():
            bacsi = BacSi(id=row["bacsi_id"], ten=row["bacsi_ten"], dob=None, chuyenmon=None, hocvan=None, kinhnghiem=None, img=None, phongID=None, username=None, password=None)
            benhnhan = BenhNhan(id=row["benhnhan_id"], ten=row["benhnhan_ten"], dob=row["benhnhan_dob"], cccd=row["benhnhan_cccd"], sdt=row["benhnhan_sdt"], quequan=row["benhnhan_quequan"], img=row["benhnhan_img"], username=None, password=None)
            lichhen = LichHen(id=row["id"], thoigianhen=row["thoigianhen"], Bacsi=bacsi, BenhNhan=benhnhan)
            lichhen_list.append(lichhen)
        cursor.close()
        conn.close()
        return lichhen_list

    @staticmethod
    def create_phieu_kham(trieuchung, chandoan, thongsoxetnghiem, anhxetnghiem, ngaykham, benhnhan, bacsi, tienkham):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        try:
            # Tạo phiếu khám
            query = """
                INSERT INTO phieukham (trieuchung, chandoan, thongsoxetnghiem, anhxetnghiem, ngaykham, benhnhanID, bacsiID, tienkham)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (trieuchung, chandoan, thongsoxetnghiem, anhxetnghiem, ngaykham, benhnhan.get("id"), bacsi.get("id"), tienkham))
            conn.commit()
            
            # Lấy ID của phiếu khám vừa tạo
            phieukham_id = cursor.lastrowid
            

            phieukham_dict = {
                "id": phieukham_id,
                "trieuchung": trieuchung,
                "chandoan": chandoan,
                "thongsoxetnghiem": thongsoxetnghiem,
                "anhxetnghiem": anhxetnghiem,
                "ngaykham": ngaykham,
                "tienkham": tienkham,
                "BenhNhan": benhnhan,  # Giữ nguyên dict đã nhận
                "BacSi": bacsi  # Giữ nguyên dict đã nhận
            }
            
            return phieukham_dict

        except Exception as e:
            conn.rollback()
            return {"error": f"Lỗi khi tạo phiếu khám: {str(e)}"}

        finally:
            cursor.close()
            conn.close()

    
    @staticmethod
    def login_bacsi(username, password):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM bacsi WHERE username = %s"
        cursor.execute(query, (username,))
        bacsi = cursor.fetchone()
        cursor.close()
        conn.close()

        if bacsi and bacsi["password"] == password:
            return {
                "success": True,
                "bacsi": {
                    "id": bacsi["id"],
                    "ten": bacsi["ten"],
                    "chuyenmon": bacsi["chuyenmon"],
                    "kinhnghiem": bacsi["kinhnghiem"],
                    "username": bacsi["username"]
                }
            }
        else:
            return {"success": False, "message": "Tên đăng nhập hoặc mật khẩu không đúng"}

    @staticmethod
    def get_thuoc(search_term):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT id, ten, mota, nsx, hsd, dongia
            FROM thuoc
            WHERE ten LIKE %s
        """
        cursor.execute(query, ('%' + search_term + '%',))
        thuoc_list = [Thuoc(**row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return thuoc_list
