from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/home.html")
def home():
    return render_template('home.html')

@app.route("/measurments.html")
def measurements():
    return render_template('measurments.html')

@app.route("/about.html")
def about():
    return "<h1>About Page<h1>"

@app.route("/measurments.html/<float:num>")
def numbs(num):
    return "The number is {0}".format(num)
@app.route("/measure")
def measure():
    v = request.args.to_dict()
    return v


if __name__ == '__main__':
    app.run(debug=True)
