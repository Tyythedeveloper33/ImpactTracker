from flask import Flask
from app.config import Configuration
from app.Routes import bp
from flask_migrate import Migrate
from app.Models import db
# app.register_blueprint(main_bp)


def init_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    db.init_app(app)
    Migrate(app, db)
    return app

app = init_app()
app.register_blueprint(bp)
