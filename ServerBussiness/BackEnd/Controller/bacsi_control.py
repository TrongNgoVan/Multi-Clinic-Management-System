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
    

@bacsi_bp.route("/create_phieu_kham", methods=["POST"])
def create_phieu_kham():
    data = request.get_json()   
    # Lấy dữ liệu từ request
    trieuchung = data.get("trieuchung")
    chandoan = data.get("chandoan")
    thongsoxetnghiem = data.get("thongsoxetnghiem")
    anhxetnghiem = data.get("anhxetnghiem")
    ngaykham = data.get("ngaykham")
    benhnhanID = data.get("benhnhanID")
    bacsiID = data.get("bacsiID")
    tienkham = data.get("tienkham")

    # Gọi service để tạo phiếu khám
    result = BacSiService.create_phieu_kham(
        trieuchung, chandoan, thongsoxetnghiem, anhxetnghiem, ngaykham, benhnhanID, bacsiID, tienkham
    )
    if result["success"]:
        return jsonify(result), 201
    else:
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