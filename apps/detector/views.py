from flask import Blueprint, render_template

# template_folderを指定(staticは指定しない)
dt = Blueprint(
    "detector",
    __name__,
    template_folder="templates"
)


@dt.route("/")
def index():
    return render_template("detector/index.html")
