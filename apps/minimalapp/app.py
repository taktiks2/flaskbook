import os
import logging
from flask_mail import Mail, Message
from flask_debugtoolbar import DebugToolbarExtension
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
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.logger.setLevel(logging.DEBUG)

# Mailクラスのconfig
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

toolbar = DebugToolbarExtension(app)
mail = Mail(app)


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
    if request.method == "POST":
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
        
        send_email(
            email,
            "問い合わせありがとうございました。",
            "contact_mail",
            the_username=username,
            the_description=description
        )

        flash("お問い合わせ内容はメールにて送信しました。問い合わせありがとうございました。")
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")


def send_email(to, subject, template, **kwargs):
    '''メール送信関数'''
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)