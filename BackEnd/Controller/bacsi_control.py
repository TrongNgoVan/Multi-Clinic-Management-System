import mysql.connector
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from BackEnd.DB.db_connection import get_db_connection

bacsi_bp = Blueprint("bacsi", __name__)

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

    hashed_password = generate_password_hash(data["password"])
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
        hashed_password
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
    return jsonify({"message": "Tạo bác sĩ thành công"}), 201


@bacsi_bp.route("/login", methods=["POST"])
def login_bacsi():
    data = request.json
    username = data.get("username")
    matkhau = data.get("password")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT id, password FROM bacsi WHERE username = %s"
    cursor.execute(query, (username,))
    bacsi = cursor.fetchone()

    cursor.close()
    conn.close()

    if bacsi and check_password_hash(bacsi["password"], matkhau):
        return jsonify({"message": "Đăng nhập thành công"}), 200
    else:
        return jsonify({"message": "Tên đăng nhập hoặc mật khẩu không đúng"}), 401




