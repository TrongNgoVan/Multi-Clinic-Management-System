import mysql.connector
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from BackEnd.DB.db_connection import get_db_connection

bacsi_bp = Blueprint("bacsi", __name__)
# đoạn này là để ae tạo ra một Blueprint có tên là bacsi_bp cho phần controller của bác sĩ, nó đại diện cho toàn bộ các router hay chúc năng con của bác sĩ
# ae phải khai báo cái này thì ở main.py mới có thể tiến hành đăng ký blueprint này vào server

@bacsi_bp.route("/dang-nhap")
def dang_nhap():
    return render_template("BacSiDangNhap.html")  


@bacsi_bp.route("/login", methods=["POST"])
def login_bacsi():
    data = request.form  # Lấy dữ liệu từ form gửi lên
    username = data.get("username")
    matkhau = data.get("password")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

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

@bacsi_bp.route("/logout", methods=["GET", "POST"])
def logout_bacsi():
    session.pop("bacsi", None)
    flash("Đăng xuất thành công!", "info")
    return redirect(url_for("bacsi.dang_nhap"))



@bacsi_bp.route("/trangchu")
def trang_chu_bacsi():
    if "bacsi" in session:
        bacsi = session["bacsi"] 
        return render_template("BacSiView.html", bacsi=bacsi)  # Truyền thông tin vào trang chủ bác sĩ
    
    flash("Vui lòng đăng nhập trước!", "warning")
    return redirect(url_for("bacsi.dang_nhap"))


@bacsi_bp.route("/get_all_bacsi", methods=["GET"])
def get_all_bacsi():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT ID, ten, dob, chuyenmon, hocvan, kinhnghiem, img, phongID , username FROM bacsi"
    cursor.execute(query)
    ds_bacsi = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(ds_bacsi), 200


@bacsi_bp.route("/thembacsi", methods=["POST"])
def create_bacsi():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO bacsi (ten, dob, chuyenmon, hocvan, kinhnghiem, img, phong_id, username, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data["ten"],
        data["dob"],
        data["chuyenmon"],
        data["hocvan"],
        data["kinhnghiem"],
        data["img"],
        data["phong_id"],
        data["username"],
        data["pass"]
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
    return jsonify({"message": "Tạo bác sĩ thành công"}), 201

