from flask import Blueprint

# Tạo một thể hiện của lớp Blueprint
bp = Blueprint('main', __name__)

# Import các route từ tệp routes.py
from controllers.main import routes
