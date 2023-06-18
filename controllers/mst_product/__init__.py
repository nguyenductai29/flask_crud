from flask import Blueprint
# Tạo một thể hiện của lớp Blueprint
bp = Blueprint('mst_product', __name__)

# Import các route từ tệp routes.py
from controllers.mst_product import routes
