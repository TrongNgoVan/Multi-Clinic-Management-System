import os
from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")  # Chỉ định thư mục chứa HTML

@app.route("/")
def home():
    return render_template("BenhNhanView.html")

if __name__ == "__main__":
    app.run(debug=True)



