from flask import render_template
from controllers.main import bp

# Định nghĩa route '/' cho blueprint 'index'
@bp.route('/order', methods=["GET", "POST"])
def order_index():
    data = []
    return render_template('views/order_screen/index.html', data=data)
