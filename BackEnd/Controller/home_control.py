import mysql.connector
from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from BackEnd.DB.db_connection import get_db_connection


home_bp = Blueprint("home", __name__)


@home_bp.route("/home")
def home():
    return render_template("TrangChuView.html")  


