INIT_TEMPLATE = """from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    from app.controllers.user_controller import user_bp
    from app.controllers.index_controller import index_bp
    app.register_blueprint(index_bp)
    app.register_blueprint(user_bp)

    return app
"""
