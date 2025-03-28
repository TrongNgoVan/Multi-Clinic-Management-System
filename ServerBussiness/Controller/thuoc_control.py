import mysql.connector
from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from DB.db_connection import get_db_connection



thuoc_bp = Blueprint("thuoc", __name__)
