import os
import uuid
import mysql.connector
from flask import Blueprint, request, jsonify, session
from werkzeug.utils import secure_filename
from DB.db_connection import get_db_connection
from Service.benhnhan_sv import BenhNhanService

benhnhan_bp = Blueprint("benhnhan", __name__)

# Thư mục lưu ảnh upload
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Tạo thư mục nếu chưa có
savepath = "http://172.11.43.16:5000/static/uploads/"


# Thêm thư mục tạm để lưu file tạm thời
TEMP_FOLDER = "/static/temp_folder"
os.makedirs(TEMP_FOLDER, exist_ok=True)
@benhnhan_bp.route("/register", methods=["POST"])
def register_benhnhan():
    try:
        # Lấy dữ liệu từ form-data
        ten = request.form.get("ten")
        sdt = request.form.get("sdt")
        quequan = request.form.get("quequan")
        cccd = request.form.get("cccd")
        dob = request.form.get("dob")
        username = request.form.get("username")
        password = request.form.get("password")

        img_save = None
        temp_path = None
        img_db = None

        # Xử lý file ảnh
        if "img" in request.files:
            img = request.files["img"]
            if img.filename != "":
                # Tạo tên file duy nhất và lưu tạm
                filename = secure_filename(img.filename)
                unique_filename = f"{uuid.uuid4()}_{filename}"
                temp_path = os.path.join(TEMP_FOLDER, unique_filename)
                img.save(temp_path)  # Lưu tạm vào thư mục TEMP_FOLDER
                img_save = os.path.join(UPLOAD_FOLDER, unique_filename)  # Đường dẫn đích
                img_db = savepath + unique_filename

        # Gọi service để đăng ký bệnh nhân (truyền img_save vào service)
        result = BenhNhanService.register_benhnhan(
            ten, sdt, quequan, cccd, dob, img_db, username, password
        )

        # Chỉ di chuyển file nếu đăng ký thành công
        if result["success"] and temp_path and img_save:
            os.rename(temp_path, img_save)  # Di chuyển từ temp sang thư mục đích
        elif temp_path:
            os.remove(temp_path)  # Xóa file tạm nếu thất bại

        return jsonify(result), 201 if result["success"] else 400

    except Exception as e:
        # Xóa file tạm nếu có lỗi
        if "temp_path" in locals() and temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
        return jsonify({"success": False, "message": str(e)}), 500
        
@benhnhan_bp.route("/update", methods=["PUT"])
def update_benhnhan():
    try:
        # Lấy dữ liệu từ form-data
        id = request.form.get("id")
        ten = request.form.get("ten")
        sdt = request.form.get("sdt")
        quequan = request.form.get("quequan")
        cccd = request.form.get("cccd")
        dob = request.form.get("dob")

        # Lấy thông tin ảnh cũ từ CSDL
        old_img_path = BenhNhanService.get_benhnhan_image_path(id)
        img_save = old_img_path  # Mặc định giữ nguyên ảnh cũ
        temp_path = None
        img_db = old_img_path if old_img_path else None

        # Xử lý file ảnh mới nếu có
        if "img" in request.files:
            img = request.files["img"]
            if img.filename != "":
                # Tạo tên file mới
                filename = secure_filename(img.filename)
                unique_filename = f"{uuid.uuid4()}_{filename}"
                temp_path = os.path.join(TEMP_FOLDER, unique_filename)
                
                # Lưu tạm ảnh mới
                img.save(temp_path)
                img_save = os.path.join(UPLOAD_FOLDER, unique_filename)
                img_db = savepath + unique_filename

        # Gọi service cập nhật thông tin
        data = {
            "id": id,
            "ten": ten,
            "sdt": sdt,
            "quequan": quequan,
            "cccd": cccd,
            "dob": dob,
            "img": img_db,
        }
        result = BenhNhanService.update_benhnhan_info(data)

        # Xử lý sau khi cập nhật thành công
        if result["success"] and temp_path and img_save:
            # Di chuyển ảnh mới từ temp sang thư mục đích
            os.rename(temp_path, img_save)
            
        elif temp_path:
            # Xóa ảnh tạm nếu cập nhật thất bại
            os.remove(temp_path)

        return jsonify(result), 200 if result["success"] else 400

    except Exception as e:
        # Xóa ảnh tạm nếu có lỗi
        if "temp_path" in locals() and temp_path and os.path.exists(temp_path):
            os.remove(temp_path)
        return jsonify({"success": False, "message": str(e)}), 500

@benhnhan_bp.route("/login", methods=["POST"])
def login_bacsi():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    result = BenhNhanService.login_benhnhan(username, password)
    if result["success"]:
        session["benhnhan"] = result["benhnhan"]
        return jsonify(result), 200
    else:
        return jsonify(result), 401

@benhnhan_bp.route("/change-password", methods=["POST"])
def change_password():
    try:
        data = request.get_json()
        benhnhan_id = data.get("id")
        new_password = data.get("newPassword")

        # Cập nhật mật khẩu mới
        result = BenhNhanService.update_password(benhnhan_id, new_password)
        return jsonify(result), 201 if result["success"] else 400

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500



@benhnhan_bp.route("/phongkham", methods=["GET"])
def get_phongkham():
    ds_phongkham = BenhNhanService.get_phongkham()
    return jsonify(ds_phongkham)

@benhnhan_bp.route("/bacsi/<int:phongkhamID>", methods=["GET"])
def get_bacsi(phongkhamID):
    ds_bs = BenhNhanService.get_bacsi(phongkhamID)
    return jsonify(ds_bs)

@benhnhan_bp.route("/lichhen/add", methods= ["POST"])
def add_lichhen():
    try:
        data = request.get_json()
        result = BenhNhanService.add_lichhen(data)
        return jsonify(result), 201 if result["success"] else 400
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@benhnhan_bp.route("/get_all_lichhen/<int:benhnhanID>", methods=["GET"])
def get_all_lichhen(benhnhanID):
    ds_lichhen = BenhNhanService.get_lichhen(benhnhanID)
    return jsonify([lichhen.to_dict() for lichhen in ds_lichhen])


from flask import jsonify
from werkzeug.exceptions import InternalServerError, NotFound

@benhnhan_bp.route("/donthuoc/<int:benhnhanID>", methods=["GET"])
def get_donthuoc(benhnhanID):
    try:
        # Gọi service
        result = BenhNhanService.get_donthuoc(benhnhanID)
        
        # Xử lý kết quả
        if result is None:
            raise InternalServerError("Lỗi hệ thống khi truy vấn dữ liệu")
            
        if not result:  # Danh sách rỗng
            return jsonify({
                "success": True,
                "message": "Bệnh nhân chưa có đơn thuốc nào",
                "data": []
            }), 200
            
        return jsonify({
            "success": True,
            "count": len(result),
            "data": result
        }), 200
        
    except Exception as e:
        # Ghi log lỗi
        app.logger.error(f"Lỗi API /donthuoc/{benhnhanID}: {str(e)}")
        return jsonify({
            "success": False,
            "error": "Lỗi server nội bộ"
        }), 500


@benhnhan_bp.route("/phieukham/<int:benhnhanID>", methods=["GET"])

def get_all_phieukham(benhnhanID):
    try:
        # Validate input
        

        # Get data from service
        result = BenhNhanService.get_phieukham(benhnhanID)
        
        # Handle service response
        if result.get('success'):
            return jsonify({
                "success": True,
                "message": "Lấy danh sách phiếu khám thành công",
                "data": result.get('data', []),
                "total": result.get('total', 0)
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Lỗi hệ thống",
                "error": result.get('error', 'UNKNOWN_ERROR')
            }), 500

    except Exception as e:
        return jsonify({
            "success": False,
            "message": "Lỗi không xác định",
            "error": str(e)
        }), 500