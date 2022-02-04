from flask import Flask, render_template, url_for,\
    request, redirect

app = Flask(__name__)


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
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")
