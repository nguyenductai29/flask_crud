from flask import *
from models.database import db
from flask_migrate import Migrate
from controllers import main, order, notification, mst_product
from helpers.logger import setup_logger
import secrets

# Định nghĩa logger
logger = setup_logger()

app = Flask(__name__)
app.config.from_pyfile('./settings.py')    # Tải cấu hình từ tệp settings.py
app.secret_key = secrets.token_hex(16)

db.init_app(app)

# TODO
migrate = Migrate(app, db, directory='migrations', command='db')

logger.info('Start')

# Đăng ký blueprint của các controllers
app.register_blueprint(main.bp)
app.register_blueprint(order.bp)
app.register_blueprint(notification.bp)
app.register_blueprint(mst_product.bp)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='8080')
