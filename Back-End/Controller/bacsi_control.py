from flask import Blueprint, request, jsonify
from Back_End.DB.db_connection import SessionLocal
from Model.bacsi import BacSi
from werkzeug.security import check_password_hash

bacsi_bp = Blueprint("bacsi", __name__)

#Hai
@bacsi_bp.route("/bacsi", methods=["GET"])
def get_all_bacsi():
    session = SessionLocal()
    ds_bacsi = session.query(BacSi).all()
    result = []
    for b in ds_bacsi:
        bacsi_info = {
            "id": b.id,
            "ten": b.ten,
            "dob": b.dob,
            "chuyenmon": b.chuyenmon
        }
        result.append(bacsi_info)
        print(bacsi_info)  # Hiển thị thông tin bác sĩ ra terminal
    session.close()
    return jsonify(result)