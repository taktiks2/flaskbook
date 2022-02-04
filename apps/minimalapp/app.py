from email_validator import validate_email, EmailNotValidError
from flask import (
    Flask,
    render_template,
    url_for,
    request,
    redirect,
    flash
)

app = Flask(__name__)

app.config["SECRET_KEY"] = "YouWillNeedThisKey"


@app.route("/")
def index():
    return "hello flask"


@app.route("/hello/<name>",
           methods=["GET", "POST"],
           endpoint="hello-endpoint")
def hello(name):
    return f"hello {name}!"


@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html",
                           the_name=name)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete",
           methods=["GET", "POST"])
def contact_complete():
    print(request.method)
    if request.method == "POST":
        print('test1')
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        is_valid = True
        if not username:
            flash("ユーザー名は必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not description:
            flash("問い合わせ内容は必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        flash("問い合わせありがとうございました")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")
