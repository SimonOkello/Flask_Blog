from flask import Flask, render_template,url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] ="d4bab8cde4783fa2a550c6e79ccb185d"

posts = [
    {
        "Author": "Simon Okello",
        "Title": "Blog Post 1",
        "Content": "My first blog post",
        "Date": "December 17, 2018"
    },
    {
        "Author": "Simon Maseno",
        "Title": "Blog Post 2",
        "Content": "My Second blog post",
        "Date": "December 18, 2018"
    }
]

@app.route("/")
def home():
    return render_template("home.html", posts = posts)

@app.route("/about")
def about():
    return render_template("about.html", title = "About")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title = "Register", form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("register.html", title = "Register", form = form)

if __name__ == "__main__":
    app.run(debug = True)
