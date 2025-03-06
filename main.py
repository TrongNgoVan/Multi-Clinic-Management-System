import os
from flask import Flask, render_template
from BackEnd.Controller.bacsi_control import bacsi_bp
app = Flask(__name__, template_folder="templates")  # Chỉ định thư mục chứa HTML
app.register_blueprint(bacsi_bp)
@app.route("/")
def home():
    return render_template("BacSiView.html")

if __name__ == "__main__":
    app.run(debug=True)
