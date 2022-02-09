from pathlib import Path
from flask import Flask
from apps.crud import views as crud_views
from flask_migrate import Migrate
from apps.crud.models import db, User


def create_app():
    app = Flask(__name__)

    # アプリのコンフィグ設定
    app.config.from_mapping(
        SECRET_KEY="slkFgWiosfweoi35dkdfoDD",
        SQLALCHEMY_DATABASE_URI=
            f"sqlite:///{Path(__file__).parent.parent/'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
    )

    # SQLAlchemyとアプリの連携
    db.init_app(app)
    # Migrateとアプリの連携
    Migrate(app, db)

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app