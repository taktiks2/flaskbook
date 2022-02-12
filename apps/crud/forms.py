from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length


class UserForm(FlaskForm):
    # ユーザーフォームusername属性のラベルとバリデータを設定
    username = StringField(
        "ユーザー名",
        validators=[
            DataRequired(message="ユーザー名は必須です。"),
            length(max=30, message="30文字以内で入力してください。"),
        ],
    )
    # ユーザーフォームemail属性のラベルとバリデータを設定
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired(message="メールアドレスは必須です。"),
            Email(message="メールアドレスの形式で入力してください。"),

        ],
    )
    # ユーザーフォームpassword属性のラベルとバリデータを設定
    passowrd = PasswordField(
        "パスワード",
        validators=[DataRequired(message="パスワードは必須です。")]
    )

    # ユーザーフォームsubmitの文言を設定
    submit = SubmitField("新規作成")
