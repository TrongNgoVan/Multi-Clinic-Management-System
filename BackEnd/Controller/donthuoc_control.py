import mysql.connector
from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from BackEnd.DB.db_connection import get_db_connection


donthuoc_bp = Blueprint("donthuoc", __name__)

@donthuoc_bp.route("/themdonthuoc", methods=["POST"])
def create_donthuoc():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO donthuoc (ngaymua, benhnhanID, bacsiID, tonggia, mota)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        data["ngaymua"],
        data["benhnhanID"],
        data["bacsiID"],
        data["tonggia"],
        data["mota"]
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
    return jsonify({"message": "Tạo đơn thuốc thành công"}), 201