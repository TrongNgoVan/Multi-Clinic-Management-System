import mysql.connector
from flask import Blueprint, request, jsonify , render_template
from werkzeug.security import generate_password_hash, check_password_hash
from BackEnd.DB.db_connection import get_db_connection

benhnhan_bp = Blueprint("benhnhan", __name__)


@benhnhan_bp.route("/dang-nhap")
def dang_nhap():
    return render_template("BenhNhanDangNhap.html")  