from flask_wtf.file import FileAllowed, FileField, FileRequird
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import SubmitField


class UploadImageForm(FlaskForm):
    # ファイルフィールドに必要なバリデーション設定
    image = FileField(
        validators=[
            FileRequird("画像ファイルを指定してください。"),
            FileAllowed(["png", "jpg", "jpeg"] ,"サポートされていない画像形式です"),
        ]
    )
    submit = SubmitField("アップロード")
