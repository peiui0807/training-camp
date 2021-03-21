from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app=Flask(
    __name__,
)

app.secret_key = "hello"

@app.route("/")
def index():
    return render_template("homepage.html") #homepage.html


@app.route("/signin",methods=["POST"])
def signin():
    name=request.form["name"]
    password=request.form["password"]
    if name=="test" and password=="test":
        session["user"]=name
        return redirect("/member/")
    else:
        return redirect("/error/")

@app.route("/member/")
def member():
    if "user" in session:
        name=session["user"]
        return render_template("successpage.html") #successpage.html
    else:    
        return redirect("/")

@app.route("/error/")
def error():
    return render_template("failpage.html") #failpage.html

@app.route("/signout")
def logout():
    session.pop("user",None)
    return redirect("/")


app.run(port=3000)