from flask import render_template, session
from sqlalchemy import text
from helpers.logger import setup_logger
from controllers.notification import bp
from models.common import *

logger = setup_logger()

@bp.route('/mst_product', methods=["GET", "POST"])
def master_producr_index():
    sql = text("SELECT product_name, category_code FROM mst_tbl_product WHERE is_delete='0'")
    search_data =select(sql)
    sql = text("SELECT * FROM mst_tbl_product WHERE is_delete='0'")
    table_data = select(sql)
    return render_template('views/mst_product_screen/index.html', search_data=search_data, table_data=table_data)
