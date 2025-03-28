import mysql.connector
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from DB.db_connection import get_db_connection
from Service.benhnhan_sv import BenhNhanService
benhnhan_bp = Blueprint("benhnhan", __name__)


@benhnhan_bp.route("/login", methods=["POST"])
def login_bacsi():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    result = BenhNhanService.login_benhnhan(username, password)
    if result["success"]:
        session["benhnhan"] = result["benhnhan"]
        return jsonify(result), 200
    else:
        return jsonify(result), 401

@benhnhan_bp.route("/register", methods=["POST"])
def register_benhnhan():
    data = request.get_json()
    
    # Lấy dữ liệu từ request
    ten = data.get("ten")
    sdt = data.get("sdt")
    quequan = data.get("quequan")
    cccd = data.get("cccd")
    dob = data.get("dob")
    img = data.get("img")
    username = data.get("username")
    password = data.get("password")  # Không mã hóa mật khẩu như bạn yêu cầu

    # Gọi service để đăng ký bệnh nhân
    result = BenhNhanService.register_benhnhan(ten, sdt, quequan, cccd, dob, img, username, password)

    # Trả về phản hồi API
    if result["success"]:
        return jsonify(result), 201  # 201 Created
    else:
        return jsonify(result), 400  # 400 Bad Request nếu tên đăng nhập đã tồn tại

@benhnhan_bp.route("/list", methods=["GET"])
def get_all_benhnhan():
    result = BenhNhanService.get_all_benhnhan()
    
    if result["success"]:
        return jsonify(result), 200
    else:
        return jsonify(result), 404  # Không có dữ liệu
