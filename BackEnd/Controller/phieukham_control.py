import mysql.connector
from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from BackEnd.DB.db_connection import get_db_connection

phieukham_bp = Blueprint("phieukham", __name__)

@phieukham_bp.route("/themphieukham", methods=["POST"])
def create_phieukham():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO phieukham (trieuchung, chandoan, thongsoxetnghiem, anhxetnghiem, ngaykham, benhnhanID, bacsiID, tienkham)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data["trieuchung"],
        data["chandoan"],
        data["thongsoxetnghiem"],
        data["anhxetnghiem"],
        data["ngaykham"],
        data["benhnhanID"],
        data["bacsiID"],
        data["tienkham"]
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
    return jsonify({"message": "Tạo phiếu khám thành công"}), 201

@phieukham_bp.route("/get_phieukham/<int:bacsiID>", methods=["GET"])
def get_phieukham_by_bacsi(bacsiID):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM phieukham WHERE bacsiID = %s"
    cursor.execute(query, (bacsiID,))
    ds_phieukham = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(ds_phieukham), 200
