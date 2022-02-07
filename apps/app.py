from flask import Flask
from apps.crud import vies as crud_views

def create_app():
    app = Flask(__name__)

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app