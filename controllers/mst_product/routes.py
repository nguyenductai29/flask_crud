from unittest import result
from flask import redirect, render_template, request, session, url_for, jsonify
from sqlalchemy import text
from helpers.logger import setup_logger
from controllers.mst_product import bp
from models.common import *
import datetime

dt_now = datetime.datetime.now()
logger = setup_logger()
str_date = f"{dt_now.year}/{dt_now.month}/{dt_now.day}"

@bp.route('/mst_product', methods=["GET", "POST"])
def master_product_index():
    sql = text("SELECT product_name, category_code FROM mst_tbl_product WHERE is_delete='0'")
    search_data =select(sql)
    sql = text("SELECT * FROM mst_tbl_product WHERE is_delete='0'")
    table_data = select(sql)
    return render_template('views/mst_product_screen/index.html', search_data=search_data, table_data=table_data)

@bp.route('/add_mst_product', methods=["GET", "POST"])
def add_new_item():
    try:
        begin_transaction()
        data = request.json
        for item in data:
            product_name = item.get('product_name')
            category_code = item.get('category_code')
            price = item.get('price')

            sql = text("SELECT COUNT(product_code) FROM mst_tbl_product")
            product_code = int(select_fetchone(sql)[0])
            print(product_code)

            sql = text("INSERT INTO mst_tbl_product (product_code, product_name, category_code, price, is_delete, created_at, updated_at) VALUES (:product_code, :product_name, :category_code, :price, :is_delete, :created_at, :updated_at)")
            params = {
                "product_code": product_code + 1,
                "product_name": product_name,
                "category_code": category_code,
                "price": price,
                "is_delete": '0',
                "created_at": str_date,
                "updated_at": str_date
            }
            insert(sql, params)
        commit_transaction()
        close_transaction()
        response = {
            'status': 'success',
            'message': 'Data received successfully',
            'url': '/mst_product'
        }
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

@bp.route('/update_mst_product', methods=["GET", "POST"])
def udpate_mst_product():
    try:
        begin_transaction()
        data = request.json
        for item in data:
            product_code = item.get('product_code')
            product_name = item.get('product_name')
            category_code = item.get('category_code')
            product_price = item.get('product_price')
            print(item)
            logger.info(item)

            sql = text("UPDATE mst_tbl_product SET product_name = :product_name, category_code = :category_code, price = :product_price, updated_at = :updated_at WHERE product_code = :product_code")
            params = {
                "product_code": product_code,
                "product_name": product_name,
                "category_code": category_code,
                "product_price": product_price,
                "updated_at": str_date
            }
            update(sql, params)
        commit_transaction()
        close_transaction()
        response = {
            'status': 'success',
            'message': 'cập nhật thành công!',
            'url': '/mst_product'
        }
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

@bp.route('/delete_mst_product', methods=["GET", "POST"])
def delete_mst_product():
    try:
        begin_transaction()
        data = request.json
        for item in data:
            print(item)
            product_code = item.get('product_code')

            sql = text("UPDATE mst_tbl_product SET is_delete = :is_deleted, updated_at = :updated_at WHERE product_code = :product_code")
            params = {
                    "product_code": product_code,
                    "is_deleted": '1',
                    "updated_at": str_date
            }
            update(sql, params)
        commit_transaction()
        close_transaction()
        response = {
            'status': 'success',
            'message': 'xóa thành công!',
            'url': '/mst_product'
        }
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
