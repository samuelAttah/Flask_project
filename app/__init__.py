from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate(db)
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login_route'


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

    # Register blueprints here
    from .main import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
