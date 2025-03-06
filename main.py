from flask import Flask
from BackEnd.Controller.bacsi_control import bacsi_bp


app = Flask(__name__)

app.register_blueprint(bacsi_bp)

if __name__ == "__main__":
    app.run(debug=True)
