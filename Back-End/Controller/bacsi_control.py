from flask import Blueprint, request, jsonify
from DB.db_connection import SessionLocal
from Model.bacsi import BacSi
from werkzeug.security import check_password_hash

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

@bacsi_bp.route("/bacsi/login", methods=["POST"])
def login_bacsi():
    data = request.json
    tendangnhap = data.get("tendangnhap")
    matkhau = data.get("matkhau")

    session = SessionLocal()
    bacsi = session.query(BacSi).filter_by(tendangnhap=tendangnhap).first()

    if bacsi and check_password_hash(bacsi.matkhau, matkhau):
        session.close()
        return jsonify({"message": "Đăng nhập thành công"}), 200
    else:
        session.close()
        return jsonify({"message": "Tên đăng nhập hoặc mật khẩu không đúng"}), 401
