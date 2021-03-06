from apps.crud.forms import UserForm
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
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
@login_required
def index():
    return render_template("crud/index.html")


# sqlエンドポイント
@crud.route("/sql")
@login_required
def sql():
    # User.query.all()でも可
    db.session.query(User).get(2)
    return "コンソールを確認してください"


@crud.route("/users/new", methods=["GET", "POST"])
@login_required
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
        db.session.commit()
        # ユーザーの一覧画面へリダイレクト
        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)


# login_requiredはrouteの下に書くこと！じゃないと機能しない
@crud.route("/users")
@login_required
def users():
    '''ユーザーの一覧取得'''
    users = User.query.all()
    return render_template("crud/index.html", users=users)


@crud.route("/users/<user_id>", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    form = UserForm()
    # Userモデルを利用してユーザーを取得
    user = User.query.filter_by(id=user_id).first()
    # formからサブミットされた場合はユーザーを更新してユーザー一覧画面へリダイレクト
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.users"))
    return render_template("crud/edit.html",
                           user=user,
                           form=form)


@crud.route("/users/<user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("crud.users"))
