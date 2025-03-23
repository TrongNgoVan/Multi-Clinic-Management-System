
import base64
import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from flask import Flask, request, render_template, jsonify, send_file
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import io
from PIL import Image
from io import BytesIO
from flask_cors import CORS





app = Flask(__name__)
CORS(app)

# 1. Load mô hình Keras (đã huấn luyện)
MODEL_PATH = "brain_tumor_detection_model.h5"
model = load_model("brain_tumor_classification.h5")


# 2. Từ điển lớp (giả sử 4 lớp)
TUMOR_TYPES = {
    0: "U thần kinh đệm",
    1: "U màng não",
    2: "Không có khối u",
    3: "U tuyến yên"
}

@app.route("/ai_diagnosis", methods=["POST"])
def ai_diagnosis():
    """
    Nhận ảnh base64 từ client (key='image'),
    chuyển đổi thành mảng NumPy, chạy mô hình AI,
    trả về kết quả chẩn đoán (chuỗi).
    """
    try:
        data = request.json
        if "image" not in data:
            return jsonify({"error": "No image field in JSON"}), 400

        # 3. Giải mã base64 -> ảnh
        base64_image = data["image"]
        image_bytes = base64.b64decode(base64_image)
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # 4. Tiền xử lý ảnh (resize, chuẩn hóa,...)
        image = image.resize((150, 150))  # Kích thước khớp với mô hình
        img_array = np.array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # Thêm batch dimension

        # 5. Dự đoán bằng mô hình
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)[0]

        # 6. Lấy tên loại u não
        diagnosis = TUMOR_TYPES.get(predicted_class, "Không xác định")

        return jsonify({"diagnosis": diagnosis})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
