from flask import Flask
from config import Config
from routes import api_bp
from flask_cors import CORS
from limiter import limiter
from utils import configure_logging

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes
    app.config.from_object(Config)  # load config from Config class

    configure_logging(Config.LOG_LEVEL)  # setup structured logging

    # Initialize rate limiter with app
    limiter.init_app(app)

    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

# Only run server if this file is executed directly (for local dev)
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, threaded=True)
