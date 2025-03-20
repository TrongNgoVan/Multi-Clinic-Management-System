import mysql.connector
from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from BackEnd.DB.db_connection import get_db_connection

from BackEnd.Service.bacsi_sv import BacSiService


bacsi_bp = Blueprint("bacsi", __name__)
# đoạn này là để ae tạo ra một Blueprint có tên là bacsi_bp cho phần controller của bác sĩ, nó đại diện cho toàn bộ các router hay chúc năng con của bác sĩ
# ae phải khai báo cái này thì ở main.py mới có thể tiến hành đăng ký blueprint này vào server


bacsi_bp = Blueprint("bacsi", __name__)

@bacsi_bp.route("/get_all_bacsi", methods=["GET"])
def get_all_bacsi():
    ds_bacsi = BacSiService.get_all_bacsi()
    return jsonify([bacsi.to_dict() for bacsi in ds_bacsi])




