import mysql.connector
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session, flash
from DB.db_connection import get_db_connection
from werkzeug.utils import secure_filename
from Service.bacsi_sv import BacSiService
import os
bacsi_bp = Blueprint("bacsi", __name__)

@bacsi_bp.route("/get_all_bacsi", methods=["GET"])
def get_all_bacsi():
    ds_bacsi = BacSiService.get_all_bacsi()
    return jsonify([bacsi.to_dict() for bacsi in ds_bacsi]) 

@bacsi_bp.route("/get_all_lichhen/<int:bacsiID>", methods=["GET"])
def get_all_lichhen(bacsiID):
    ds_lichhen = BacSiService.get_all_lichhen(bacsiID)
    return jsonify([lichhen.to_dict() for lichhen in ds_lichhen])

@bacsi_bp.route("/login", methods=["POST"])
def login_bacsi():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    result = BacSiService.login_bacsi(username, password)
    if result["success"]:
        session["bacsi"] = result["bacsi"]
        return jsonify(result), 200
    else:
        return jsonify(result), 401
    

UPLOAD_FOLDER_ABS = r"B:\Documents\Kỳ 2 - Năm 4\Chuyên Đề HTTT\Multi-Clinic-Management-System\ServerCustomer\static\xetnghiem"

@bacsi_bp.route("/create_phieu_kham", methods=["POST"])
def create_phieu_kham():
    file = request.files.get("anhxetnghiem")
    if not file or file.filename == "":
        return jsonify({"success": False, "message": "Chưa upload ảnh xét nghiệm"}), 400

    # Xử lý form data
    form = request.form
    trieuchung       = form.get("trieuchung", "")
    chandoan         = form.get("chandoan", "")
    thongsoxetnghiem = form.get("thongsoxetnghiem", "")
    ngaykham         = form.get("ngaykham", "")
    benhnhanID       = form.get("benhnhanID")
    bacsiID          = form.get("bacsiID")
    tienkham         = form.get("tienkham", "")

    # Xử lý tên file an toàn
    filename = secure_filename(file.filename)

    # Chỉ gửi dữ liệu form (chưa lưu ảnh vội)
    result = BacSiService.create_phieu_kham(
        trieuchung=trieuchung,
        chandoan=chandoan,
        thongsoxetnghiem=thongsoxetnghiem,
        anhxetnghiem=filename,  # vẫn gửi tên file vào DB
        ngaykham=ngaykham,
        benhnhanID=benhnhanID,
        bacsiID=bacsiID,
        tienkham=tienkham
    )

    if result.get("success"):
        try:
            # Sau khi database thành công, mới lưu file ảnh
            os.makedirs(UPLOAD_FOLDER_ABS, exist_ok=True)
            save_path = os.path.join(UPLOAD_FOLDER_ABS, filename)
            file.save(save_path)

            public_url = f"/static/xetnghiem/{filename}"  # đường dẫn public
            result.update({"anhxetnghiem_url": public_url})

            return jsonify(result), 201

        except Exception as e:
            # Nếu lỗi khi lưu file -> rollback database nếu cần (tuỳ bạn)
            return jsonify({"success": False, "message": f"Lỗi khi lưu ảnh: {str(e)}"}), 500

    else:
        # Nếu database lỗi -> không lưu gì hết
        return jsonify(result), 400


@bacsi_bp.route("/create_prescription", methods=["POST"])
def create_don_thuoc():
    data = request.get_json()
    ngaymua = data.get("ngaymua")
    benhnhan = data.get("benhnhan")
    bacsi = data.get("bacsi")
    tonggia = data.get("tonggia")
    mota = data.get("mota")
    chitietdonthuoc = data.get("chitietdonthuoc")

    # Gọi service để tạo đơn thuốc
    result = BacSiService.create_prescription(
        ngaymua, benhnhan, bacsi, tonggia, mota, chitietdonthuoc
    )
    return jsonify(result), 201

@bacsi_bp.route("/get_thuoc", methods=["GET"])
def get_thuoc():
    search_term = request.args.get("search", "")
    thuoc_list = BacSiService.get_thuoc(search_term)
    return jsonify(thuoc_list), 200

@bacsi_bp.route("/get_all_phieukham", methods=["GET"])
def get_all_phieukham():
    ds_phieukham = BacSiService.get_all_phieukham()
    return jsonify(ds_phieukham), 200

@bacsi_bp.route("/duyetlichhen/<int:id>", methods=["PUT"])
def duyetlichhen(id):
   
    result = BacSiService.duyetlichhen(id)
    return jsonify(result), 200