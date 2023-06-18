from flask import render_template, session
from helpers.logger import setup_logger
from controllers.notification import bp

logger = setup_logger()

@bp.route('/order_detail', methods=["GET", "POST"])
def order_detail_index():
    message = session.pop('order_message', None)
    return render_template('views/notification_screen/index.html', message=message)
