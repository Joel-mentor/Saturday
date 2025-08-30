from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("hosting.html")


@app.route("/Students_Info.html")
def projects():
    return render_template("Students_Info.html")

    


if __name__=="__main__":
    app.run(debug=True)