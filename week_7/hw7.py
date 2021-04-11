from flask import Flask,request,redirect,render_template,session
import mysql.connector
import json

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fish8888",
    database="mydatabase"
)
mycursor = mydb.cursor()



app=Flask(
    __name__,
)
app.secret_key = "Hello"
@app.route("/")
def index():
    return render_template("w7_homepage.html") 

@app.route("/signup",methods=["POST"])
def signup():
    signupName=request.form["signupName"]
    signupId=request.form["signupId"]
    signupPw=request.form["signupPw"]
    searchId = "SELECT userId FROM member where userId = %s"
    signupid=(signupId,)
    mycursor.execute(searchId,signupid)
    idData = mycursor.fetchall()
    if signupid in idData:
        return redirect("/error/?message=帳號已經被註冊")
    else:
        createData="INSERT INTO member (name,userId,password) VALUES (%s,%s,%s);"
        createVal=(signupName,signupId,signupPw)
        mycursor.execute(createData,createVal)
        mydb.commit()
        return redirect("/")


@app.route("/signin",methods=["POST"])
def signin():
    signinId=request.form["signinId"]
    signinPw=request.form["signinPw"]
    userCheck="SELECT name,userId,password FROM member where userId = %s"
    signinid=(signinId,)
    mycursor.execute(userCheck,signinid)
    idData = mycursor.fetchall()
    if len(idData) == 0:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    elif signinId != idData[0][1] or signinPw != idData[0][2]:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    else:
        if signinId in idData[0][1] and signinPw in idData[0][2]:
            session["userName"]=idData[0][0]
            return redirect("/member/")
    
@app.route("/member/")
def member():
    user=session.get("userName")
    if user == None:
        return redirect("/")
    else:    
        return render_template("w7_successpage.html",name=user)

@app.route("/api/users",methods=["GET"])
def data():
    userName=request.args.get("username",None)
    data="select id,name,userId from member where userId = %s"
    id=(userName,)
    mycursor.execute(data,id)
    idData=mycursor.fetchone()
    print(idData)
    if idData != None:
        return json.dumps({
            "data":{
                "id": idData[0],
                "name": idData[1],
                "username": idData[2]
            }
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "data":idData
            }, ensure_ascii=False)

@app.route("/error/")
def error():
    message=request.args.get("message",None)
    return render_template("w7_failpage.html",errormsg=message)

@app.route("/signout")
def signout():
    session.clear()
    return redirect("/")


app.run(port=3000)
