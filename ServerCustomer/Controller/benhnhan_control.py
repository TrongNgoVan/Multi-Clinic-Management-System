import mysql.connector
from flask import Blueprint, request, jsonify , render_template
from werkzeug.security import generate_password_hash, check_password_hash
from DB.db_connection import get_db_connection

benhnhan_bp = Blueprint("benhnhan", __name__)

