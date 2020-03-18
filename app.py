import datetime
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    title = "Hello , World!"
    return render_template("index.html", title=title)


@app.route('/date')
def date():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("index.html", new_year=new_year)


@app.route('/users')
def users():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("index.html", names=names)


@app.route('/more')
def more():
    return render_template("more.html")


@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == "GET":
        return "Please Submit the form instead."
    else:
        name = request.form.get('name')
        return render_template('hello.html', name=name)

# @app.route('/<string:name>')
# def name(name):
#     name = name.capitalize()
#     return "<h1>Hello , {}  !</h1>".format(name)


if __name__ == '__main__':
    app.run()
