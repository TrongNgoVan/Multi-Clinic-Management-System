from BackEnd.DB.db_connection import get_db_connection
from BackEnd.Model.bacsi import BacSi

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
    def get_bacsi_by_username(username):
        """Tìm bác sĩ theo username."""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM bacsi WHERE username = %s", (username,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return BacSi(**row) if row else None

    @staticmethod
    def create_bacsi(data):
        """Tạo một bác sĩ mới."""
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO bacsi (ten, dob, chuyenmon, hocvan, kinhnghiem, img, phongID, username, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data["ten"], data["dob"], data["chuyenmon"], data["hocvan"],
            data["kinhnghiem"], data["img"], data["phongID"], data["username"],
            data["password"]
        )

        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return True
        
    @staticmethod
    def login_bacsi(username, password):
     
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM bacsi WHERE username = %s"
        cursor.execute(query, (username,))
        bacsi = cursor.fetchone()  # Lấy toàn bộ thông tin bác sĩ

        cursor.close()
        conn.close()

        if bacsi and bacsi["pass"] == matkhau:
            # Lưu toàn bộ thông tin bác sĩ vào session
            session["bacsi"] = bacsi  

            flash("Đăng nhập thành công!", "success")
            return redirect(url_for("bacsi.trang_chu_bacsi"))  # Chuyển đến trang chủ bác sĩ
        else:
            flash("Tên đăng nhập hoặc mật khẩu không đúng", "danger")
            return redirect(url_for("bacsi.dang_nhap"))  # Quay lại trang đăng nhập nếu sai
