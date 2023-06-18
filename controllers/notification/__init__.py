from flask import Blueprint
# Tạo một thể hiện của lớp Blueprint
bp = Blueprint('notification', __name__)

# Import các route từ tệp routes.py
from controllers.notification import routes
