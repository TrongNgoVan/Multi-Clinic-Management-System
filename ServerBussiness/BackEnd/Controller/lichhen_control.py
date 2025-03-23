import mysql.connector
from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from BackEnd.DB.db_connection import get_db_connection


lichhen_bp = Blueprint("lichhen", __name__)

@lichhen_bp.route("/get_all_lichhen/<int:bacsiID>", methods=["GET"])
def get_all_lichhen(bacsiID):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT lichhen.id, bacsi.ten as bacsi_ten, benhnhan.ten as benhnhan_ten, lichhen.thoigianhen
        FROM lichhen
        JOIN bacsi ON lichhen.bacsiID = bacsi.id
        JOIN benhnhan ON lichhen.benhnhanID = benhnhan.id
        WHERE lichhen.bacsiID = %s
    """
    cursor.execute(query, (bacsiID,))
    ds_lichhen = cursor.fetchall()

    cursor.close()
    conn.close()
    return jsonify(ds_lichhen), 200