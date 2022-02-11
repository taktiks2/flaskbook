from flask import Blueprint, render_template
from apps.crud.models import db, User

# Blueprintでcrudアプリを生成
crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)


# indexエンドポイントを作成
@crud.route("/")
def index():
    return render_template("crud/index.html")


# sqlエンドポイント
@crud.route("/sql")
def sql():
    # User.query.all()でも可
    db.session.query(User).get(2)
    return "コンソールを確認してください"
