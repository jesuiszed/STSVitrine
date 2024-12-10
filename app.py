# app.py
from flask import Flask, render_template
import os
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Configuration
app.config.update(
    SECRET_KEY=os.environ.get('SECRET_KEY', 'default-secret-key'),
    DEBUG=False,
    ENV='production'
)

# Logging setup
if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/sts.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('STS startup')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Production server configuration
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    app.run(
        host=host,
        port=port,
        ssl_context='adhoc'  # Enable HTTPS in production
    )