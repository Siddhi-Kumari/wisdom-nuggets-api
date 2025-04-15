from flask import Flask
from .database import db
from .routes import nuggets_bp
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        from .model import WisdomNugget
        db.create_all()

    app.register_blueprint(nuggets_bp)
    return app
