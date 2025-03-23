import mysql.connector
from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from BackEnd.DB.db_connection import get_db_connection


chitietdonthuoc_bp = Blueprint("chitietdonthuoc", __name__)
