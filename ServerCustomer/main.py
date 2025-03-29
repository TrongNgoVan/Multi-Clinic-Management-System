import secrets
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Khởi tạo Flask app trước
app = Flask(__name__, static_folder="static")

# # Cấu hình JWT
# app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'  # Thay bằng secret key thực tế
# app.config['JWT_TOKEN_LOCATION'] = ['headers']  # Đảm bảo token được lấy từ header
# app.config['JWT_HEADER_NAME'] = 'Authorization'  # Tên header chứa JWT token
# app.config['JWT_HEADER_TYPE'] = 'Bearer'  # Loại token, thường là Bearer

# # Khởi tạo JWTManager
# jwt = JWTManager(app)

# CORS để cho phép request từ frontend
CORS(app)

# Secret key để bảo mật session
app.secret_key = secrets.token_hex(32)

# Import các blueprint
from Controller.bacsi_control import bacsi_bp
from Controller.benhnhan_control import benhnhan_bp
from Controller.donthuoc_control import donthuoc_bp
from Controller.lichhen_control import lichhen_bp
from Controller.phieukham_control import phieukham_bp
from Controller.thuoc_control import thuoc_bp
from Controller.chitietdonthuoc_control import chitietdonthuoc_bp
from Controller.phongchucnang_control import phongchucnang_bp

# Đăng ký các blueprint
app.register_blueprint(bacsi_bp, url_prefix="/bacsi")
app.register_blueprint(benhnhan_bp, url_prefix="/benhnhan")
app.register_blueprint(donthuoc_bp, url_prefix="/donthuoc")
app.register_blueprint(lichhen_bp, url_prefix="/lichhen")   
app.register_blueprint(phieukham_bp, url_prefix="/phieukham")   
app.register_blueprint(thuoc_bp, url_prefix="/thuoc")
app.register_blueprint(chitietdonthuoc_bp, url_prefix="/chitietdonthuoc")
app.register_blueprint(phongchucnang_bp, url_prefix="/phongchucnang")

# Chạy server
if __name__ == "__main__":
    app.run(host="192.168.43.20", port=5000)
    # ipv4 wifi trọng 192.168.43.20
    # ipv4 wifi trường 172.11.43.16

