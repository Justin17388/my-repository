from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome"


@app.route("/head")
def head():
    return render_template("index.html", number1 = 10, number2 = 20)  

@app.route("/sum")
def sum():

    val1 = 22
    val2 = 36
    mysum = val1 + val2
    return render_template("body.html", value1 = val1, value2 = val2, sum = mysum)     

if __name__== "__main__":
    app.run(host="0.0.0.0")