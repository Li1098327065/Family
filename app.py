from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chujie")
def chujie():
    return render_template("chujie.html")

@app.route("/shaohua")
def shaohua():
    return render_template("shaohua.html")

@app.route("/meng")
def meng():
    return render_template("meng.html")

@app.route("/ni")
def ni():
    return render_template("ni.html")

@app.route("/bin")
def bin():
    return render_template("bin.html")

@app.route("/yan")
def yan():
    return render_template("yan.html")

@app.route("/yang")
def yang():
    return render_template("yang.html")

@app.route("/han")
def han():
    return render_template("han.html")

if __name__ == "__main__":
    app.run(debug=True)
