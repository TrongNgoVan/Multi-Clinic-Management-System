from DB.db_connection import get_db_connection
from Model.bacsi import BacSi
from Model.benhnhan import BenhNhan
from Model.lichhen import LichHen
from Model.phieukham import PhieuKham
from Model.thuoc import Thuoc

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
            SELECT lichhen.id, lichhen.thoigianhen, lichhen.ghichu, lichhen.trangthai,
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
            lichhen = LichHen(id=row["id"], Bacsi=bacsi, BenhNhan=benhnhan, ghichu = row["ghichu"],thoigianhen=row["thoigianhen"], trangthai=row["trangthai"])
            lichhen_list.append(lichhen)
        cursor.close()
        conn.close()
        return lichhen_list

    @staticmethod
    def create_phieu_kham(trieuchung, chandoan, thongsoxetnghiem,
                          anhxetnghiem, ngaykham, benhnhanID,
                          bacsiID, tienkham):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        try:
            # 1) Ghép tiền tố URL trước tên file (hoặc path gốc từ form)
            base_url = "http://192.168.43.20:5000/static/xetnghiem/"
            full_file_url = base_url + anhxetnghiem.lstrip("/")  # đảm bảo không dư slash

            # 2) Thực hiện INSERT, lưu full_file_url
            query = """
                INSERT INTO phieukham 
                    (trieuchung, chandoan, thongsoxetnghiem, anhxetnghiem, 
                     ngaykham, benhnhanID, bacsiID, tienkham)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                trieuchung,
                chandoan,
                thongsoxetnghiem,
                full_file_url,   # lưu URL đầy đủ
                ngaykham,
                benhnhanID,
                bacsiID,
                tienkham
            ))
            conn.commit()

            # 3) Lấy ID mới tạo (tuỳ nếu bạn muốn trả về)
            phieukham_id = cursor.lastrowid

            return {
                "success": True,
                "message": "Tạo phiếu khám thành công",
            }

        except Exception as e:
            conn.rollback()
            return {
                "success": False,
                "message": f"Lỗi khi tạo phiếu khám: {str(e)}"
            }

        finally:
            cursor.close()
            conn.close()


    @staticmethod
    def create_prescription(ngaymua, benhnhan, bacsi, tonggia, mota, chitietdonthuoc):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        try:
            # Tạo đơn thuốc
            query = """
                INSERT INTO donthuoc (ngaymua, benhnhanID, bacsiID, tonggia, mota)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (ngaymua, benhnhan.get("id"), bacsi.get("id"), tonggia, mota))
            conn.commit()
            
            # Lấy ID của đơn thuốc vừa tạo
            donthuoc_id = cursor.lastrowid
            
            # Tạo chi tiết đơn thuốc
            for chitiet in chitietdonthuoc:
                query = """
                    INSERT INTO chitietdonthuoc (donthuocID, thuocID, soluong, gia)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (donthuoc_id, chitiet["thuocID"], chitiet["soluong"], chitiet["dongia"]))
            conn.commit()
            
            return {"success": True, "message": "Tạo đơn thuốc thành công"}

        except Exception as e:
            conn.rollback()
            return {"success": False, "message": f"Lỗi khi tạo đơn thuốc: {str(e)}"}

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
                    "dob": bacsi["dob"],
                    "chuyenmon": bacsi["chuyenmon"],
                    "hocvan": bacsi["hocvan"],
                    "kinhnghiem": bacsi["kinhnghiem"],
                    "img": bacsi["img"],
                    "phongID": bacsi["phongID"],
                    "username": bacsi["username"],
                    "password": bacsi["password"]
                }
            }
        else:
            return {"success": False, "message": "Tên đăng nhập hoặc mật khẩu không đúng"}

    @staticmethod
    def get_thuoc(search_term):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT id, ten, mota, nsx, hsd, dongia, img
            FROM thuoc
            WHERE ten LIKE %s
        """
        cursor.execute(query, ('%' + search_term + '%',))
        thuoc_list = [Thuoc(**row).to_dict() for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return thuoc_list
    
    @staticmethod
    def get_all_phieukham():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT pk.id, pk.trieuchung, pk.chandoan, pk.thongsoxetnghiem, pk.anhxetnghiem, pk.ngaykham, pk.tienkham,
                   bn.id as benhnhan_id, bn.ten as benhnhan_ten, bn.dob as benhnhan_dob, bn.cccd as benhnhan_cccd, bn.sdt as benhnhan_sdt, bn.quequan as benhnhan_quequan, bn.img as benhnhan_img,
                   bs.id as bacsi_id, bs.ten as bacsi_ten, bs.dob as bacsi_dob, bs.chuyenmon as bacsi_chuyenmon, bs.hocvan as bacsi_hocvan, bs.kinhnghiem as bacsi_kinhnghiem, bs.img as bacsi_img
            FROM phieukham pk
            JOIN benhnhan bn ON pk.benhnhanID = bn.id
            JOIN bacsi bs ON pk.bacsiID = bs.id
        """
        cursor.execute(query)
        phieukham_list = []
        for row in cursor.fetchall():
            benhnhan = BenhNhan(id=row["benhnhan_id"], ten=row["benhnhan_ten"], dob=row["benhnhan_dob"], cccd=row["benhnhan_cccd"], sdt=row["benhnhan_sdt"], quequan=row["benhnhan_quequan"], img=row["benhnhan_img"], username=None, password=None)
            bacsi = BacSi(id=row["bacsi_id"], ten=row["bacsi_ten"], dob=row["bacsi_dob"], chuyenmon=row["bacsi_chuyenmon"], hocvan=row["bacsi_hocvan"], kinhnghiem=row["bacsi_kinhnghiem"], img=row["bacsi_img"], phongID=None, username=None, password=None)
            phieukham = PhieuKham(id=row["id"], trieuchung=row["trieuchung"], chandoan=row["chandoan"], thongsoxetnghiem=row["thongsoxetnghiem"], anhxetnghiem=row["anhxetnghiem"], ngaykham=row["ngaykham"], tienkham=row["tienkham"], BenhNhan=benhnhan, BacSi=bacsi)
            phieukham_list.append(phieukham)
        cursor.close()
        conn.close()
        return [pk.to_dict() for pk in phieukham_list]

    @staticmethod
    def duyetlichhen(id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            UPDATE lichhen
            SET trangthai = "Đã duyệt"
            WHERE ID = %s
        """
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return {"success": True, "message": "Duyệt lịch hẹn thành công"}