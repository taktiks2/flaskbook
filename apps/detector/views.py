from apps.crud.models import db, User
from apps.detector.models import UserImage
from flask import Blueprint, render_template

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
