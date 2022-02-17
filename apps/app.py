from flask import Flask, render_template
from apps.crud import views as crud_views
from apps.auth import views as auth_views
from apps.detector import views as dt_views
from apps.crud.models import db, User, login_manager
from apps.detector.models import UserImage, UserImageTag
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from apps.config import config

csrf = CSRFProtect()

# login_message属性に未ログイン時にリダイレクトするエンドポイントを指定
login_manager.login_view = "auth.signup"
# login_view属性にログイン後に表示するメッセージを指定
# ここでは何も表示しないよう指定
login_manager.login_message = ""


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
    # login_managerとアプリの連携
    login_manager.init_app(app)

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    app.register_blueprint(auth_views.auth, url_prefix="/auth")
    app.register_blueprint(dt_views.dt)

    return app


# 登録したエンドポイント名の関数を作成し、404や500が発生した際に指定しHTMLを返す
def page_not_found(e):
    """404 Not Found"""
    return render_template("404.html"), 404


def internal_server_error(e):
    """500 Internal Server Error"""
    return render_template("500.html"), 500
