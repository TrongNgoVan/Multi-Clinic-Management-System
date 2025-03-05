from flask import Blueprint, request, jsonify
from DB.db_connection import SessionLocal
from Model.bacsi import BacSi

bacsi_bp = Blueprint("bacsi", __name__)

@bacsi_bp.route("/bacsi", methods=["GET"])
def get_all_bacsi():
    session = SessionLocal()
    ds_bacsi = session.query(BacSi).all()
    result = []
    for b in ds_bacsi:
        result.append({
            "id": b.id,
            "ten": b.ten,
            "sdt": b.sdt,
            "chucvu": b.chucvu
        })
    session.close()
    return jsonify(result)

@bacsi_bp.route("/bacsi", methods=["POST"])
def create_bacsi():
    data = request.json
    session = SessionLocal()
    new_bacsi = BacSi(
        ten=data["ten"],
        sdt=data["sdt"],
        chucvu=data["chucvu"]
    )
    session.add(new_bacsi)
    session.commit()
    session.close()
    return jsonify({"message": "Tạo bác sĩ thành công"}), 201
