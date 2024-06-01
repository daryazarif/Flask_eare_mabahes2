from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def hello_world():
    #return "<p>Hello, World!</p>"

    return render_template('home.html', name='zarif')

@app.route("/about")
def about():
    return render_template("about.html")