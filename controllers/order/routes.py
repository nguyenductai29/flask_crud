from flask import render_template, request, jsonify, session
from sqlalchemy import text
from controllers.order import bp
from models.common import *
from helpers.logger import setup_logger
import datetime

dt_now = datetime.datetime.now()
logger = setup_logger()
str_date = f"{dt_now.year}/{dt_now.month}/{dt_now.day}"

# Định nghĩa route '/' cho blueprint 'index'
@bp.route('/order', methods=["GET", "POST"])
def order_index():
    sql = text("""
        SELECT * FROM mst_tbl_product WHERE is_delete = '0';
    """)
    data = select(sql)
    return render_template('views/order_screen/index.html', datas=data)

@bp.route('/process_data_order', methods=["GET", "POST"])
def process_data_order():
    try:
        data = request.json
        begin_transaction()
        for item in data:
            product_name = item.get('product_name')
            category_code = item.get('category_code')

            sql = text("INSERT INTO tbl_order (product_name, category_code, order_date) VALUES (:product_name, :category_code, :order_date)")
            params = {
                "product_name": product_name,
                "category_code": category_code,
                "order_date": str_date
            }
            insert(sql, params)
            commit_transaction()

        sql = text("SELECT MAX(order_no) FROM tbl_order")
        maxOrdNo = select_fetchone(sql)[0]
        print(maxOrdNo)

        for item in data:
            product_code = item.get('product_code')
            count = int(item.get('count'))
            price = int(item.get('price'))
            sql = text("INSERT INTO tbl_order_detail (order_no, product_code, order_count, price, is_delete, created_at, updated_at) VALUES (:order_no, :product_code, :order_count, :order_price, :is_delete, :created_at, :updated_at)")
            params = {
                "order_no": maxOrdNo,
                "product_code": product_code,
                "order_count": count,
                "order_price": price,
                "is_delete": '0',
                "created_at": str_date,
                "updated_at": str_date
            }
            insert(sql, params)
            commit_transaction()

        response = {
            'status': 'success',
            'message': 'Data received successfully',
            'url': '/order_detail'
        }
        session['order_message'] = response['message']
        return jsonify(response), 200
    except Exception as ex:
        logger.error(ex)
        rollback_transaction()
        response = {
            'status': 'error',
            'message': 'Data error',
            'url': '/order_detail'
        }
        session['order_message'] = response['message']
        return jsonify(response), 400
