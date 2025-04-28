import os
import cv2
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

# Load mô hình đã huấn luyện
model = load_model("brain_tumor_classification.h5")

# Từ điển lớp
TUMOR_TYPES = {
    0: "U thần kinh đệm",
    1: "U màng não",
    2: "Không có khối u",
    3: "U tuyến yên"
}

@app.route("/ai_diagnosis", methods=["POST"])
def ai_diagnosis():
    """
    Nhận ảnh từ client qua FormData (key='image'),
    chuyển đổi thành mảng NumPy, chạy mô hình AI,
    trả về kết quả chẩn đoán (chuỗi).
    """
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file in request"}), 400
        file = request.files['image']

        # Đọc ảnh
        image = Image.open(file.stream).convert("RGB")

        # Tiền xử lý
        image = image.resize((150, 150))
        img_array = np.array(image, dtype=np.float32) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Dự đoán
        pred = model.predict(img_array)
        cls = np.argmax(pred, axis=1)[0]
        diagnosis = TUMOR_TYPES.get(cls, "Không xác định")

        return jsonify({"diagnosis": diagnosis})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="26.80.253.0", port=5001, debug=True)
