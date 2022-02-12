from flask import Flask
from apps.crud import views as crud_views
from apps.auth import views as auth_views
from flask_migrate import Migrate
from apps.crud.models import db, User
from flask_wtf.csrf import CSRFProtect
from apps.config import config

csrf = CSRFProtect()


def create_app(config_key):
    app = Flask(__name__)
    # config_keyにマッチする環境のコンフィグクラスを読み込む
    app.config.from_object(config[config_key])
    # SQLAlchemyとアプリの連携
    db.init_app(app)
    # Migrateとアプリの連携
    Migrate(app, db)
    # CSRFProtectとアプリの連携
    csrf.init_app(app)

    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app
