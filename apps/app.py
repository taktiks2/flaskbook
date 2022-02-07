from flask import Flask
# appsを抜いてただのcrudにすると動かない
from apps.crud import views as crud_views

def create_app():
    app = Flask(__name__)

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app