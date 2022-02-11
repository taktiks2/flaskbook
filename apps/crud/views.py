from apps.crud.forms import UserForm
from flask import Blueprint, render_template, redirect, url_for
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


@crud.route("/users/new", methods=["GET", "POST"])
def create_user():
    form = UserForm()
    # フォームの値をバリデート
    if form.validate_on_submit():
        # ユーザーを作成
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        # ユーザーを追加してコミット
        db.session.add(user)
        db.session.commi()
        # ユーザーの一覧画面へリダイレクト
        return redirect(url_for("curd.users"))
    return render_template("crud/create.html", form=form)

