from datetime import datetime

from sqlalchemy import PrimaryKeyConstraint
from apps.app import db
from werkzeug.security import generate_password_hash

# db.Modelを継承したUserクラスを作成
class User(db.Model):
    # テーブル名を指定
    __tablename__ = "users"

    # カラムを定義する
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )

    # パスワードをセットするプロパティ
    @property
    def password(self):
        raise AttributeError("読み取り不可")

    # セッター関数でハッシュ化したパスワードをセット
    def password(self, password):
        self.password_hash = generate_password_hash(password)