import mysql.connector
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session, flash
from BackEnd.DB.db_connection import get_db_connection

from BackEnd.Service.bacsi_sv import BacSiService

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

# @bacsi_bp.route("/get_phieu_kham_by_id", methods=["GET"])
# def get_phieu_kham_by_id():
#     phieukham = session.get("phieukham")
#     print("Lấy từ session:", session.get("phieukham"))
#     if phieukham:
#         return jsonify(phieukham), 200
#     else:
#         return jsonify({"message": "Không tìm thấy phiếu khám"}), 404
    

@bacsi_bp.route("/create_phieu_kham", methods=["POST"])
def create_phieu_kham():
    data = request.get_json()

    # Lấy dữ liệu từ request
    trieuchung = data.get("trieuchung")
    chandoan = data.get("chandoan")
    thongsoxetnghiem = data.get("thongsoxetnghiem")
    anhxetnghiem = data.get("anhxetnghiem")
    ngaykham = data.get("ngaykham")
    benhnhan = data.get("benhnhan")
    bacsi = data.get("bacsi")
    tienkham = data.get("tienkham")

    # Gọi service để tạo phiếu khám
    result = BacSiService.create_phieu_kham(
        trieuchung, chandoan, thongsoxetnghiem, anhxetnghiem, ngaykham, benhnhan, bacsi, tienkham
    )

    return jsonify(result), 201  # Convert object to dictionary trước khi trả về




@bacsi_bp.route("/get_thuoc", methods=["GET"])
def get_thuoc():
    search_term = request.args.get("search", "")
    thuoc_list = BacSiService.get_thuoc(search_term)
    return jsonify(thuoc_list), 200