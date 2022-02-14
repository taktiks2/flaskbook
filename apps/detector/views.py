from apps.crud.models import db, User
from apps.detector.models import UserImage
from flask import Blueprint, render_template, current_app,\
send_from_directory

# template_folderを指定(staticは指定しない)
dt = Blueprint(
    "detector",
    __name__,
    template_folder="templates"
)


@dt.route("/")
def index():
    # UserとUserImageをJoinして画像一覧を取得
    user_images = (
        db.session.query(User, UserImage)
        .join(UserImage)
        .filter(User.id == UserImage.user_id)
        .all()
    )
    return render_template("detector/index.html", user_images=user_images)


@dt.route("/images/<path:filename>")
def image_file(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename)
