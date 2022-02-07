from pathlib import Path
from flask import Flask
from apps.crud import views as crud_views
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # アプリのコンフィグ設定
    app.config.from_mapping(
        SECRET_KEY="slkdfoi2354lkj@sldhfioddDERf",
        SQLALCHEMY_DATABASE_URI=
            f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}"
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # SQLAlchemyと連携
    db.init_app(app)

    # Migrateと連携
    Migrate(app, db)

    # register_blueprintを使いviewsのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app