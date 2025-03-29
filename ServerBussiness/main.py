import secrets
from flask import Flask

from Controller.bacsi_control import bacsi_bp
from Controller.benhnhan_control import benhnhan_bp
from Controller.donthuoc_control import donthuoc_bp
from Controller.lichhen_control import lichhen_bp
from Controller.phieukham_control import phieukham_bp
from Controller.thuoc_control import thuoc_bp
from Controller.chitietdonthuoc_control import chitietdonthuoc_bp
from Controller.phongchucnang_control import phongchucnang_bp
from flask_cors import CORS

app = Flask(__name__, static_folder="static")
CORS(app)
# ae nhớ thêm CORS sẽ giúp trình duyệt không chặn request từ router của FrontEnd đến API của BackEnd nhé ae!
# cái này là thêm mã hóa bảo mật cho bất cứ trang web nào dùng session nhé ae

app.secret_key = secrets.token_hex(32)


# Đoạn này là đăng ký các Blueprint cho toàn bộ các controller mỗi khi ae  khởi chạy server nhé!
#  ae cứ hiể BluePrint như một cái tên đaij diện cho 1 module lớn( liên quan đến 1 đối tượng)
# nó chứa nhiều route( hay API, URL) , mỗi route sẽ đại diện cho 1 hàm hay 1 tính năng cụ thể của 1 đối tượng
#  ví dụ BluePrint bacsi_bp chứa các route liên quan đến bác sĩ như: bacsi/dangnhap, bacsi/get_all_bacsi
# khi ae gọi đến route này thì nó sẽ gọi đến hàm tương ứng trong controller để xử lý
#  còn url_prefix là tiền tố của blueprint, nó sẽ thêm vào trước tất cả các route trong blueprint, muốn truy cập vào 1 route nào đó thì ae phải thêm tiền tố đó vào trước
#  ví dụ: bacsi_bp có url_prefix là "/bacsi" thì route dangnhap sẽ là "/bacsi/dangnhap"
#  Server khởi động khi chạy file này, server sẽ khởi động trên cổng http://127.0.0.1:5000  .  
# ae muón try cập vào 1 route nào đó thì thêm tên của router ( nhớ thêm tiền tố nếu có của blueprint) vào sau cổng 

app.register_blueprint(bacsi_bp, url_prefix="/bacsi")
app.register_blueprint(benhnhan_bp, url_prefix="/benhnhan")
app.register_blueprint(donthuoc_bp, url_prefix="/donthuoc")
app.register_blueprint(lichhen_bp, url_prefix="/lichhen")   
app.register_blueprint(phieukham_bp, url_prefix="/phieukham")   
app.register_blueprint(thuoc_bp, url_prefix="/thuoc")
app.register_blueprint(chitietdonthuoc_bp, url_prefix="/chitietdonthuoc")
app.register_blueprint(phongchucnang_bp, url_prefix="/phongchucnang")

if __name__ == "__main__":
    app.run(host="26.80.253.0", port=5000)

# chạy node.js server cho fe live-server --host=26.80.253.0 --port=5500     live-server --host=192.168.43.20 --port=5500
#  ip wifi trường 172.11.34.197
#  ip trọng 192.168.43.20
# thu mục ảnh 
