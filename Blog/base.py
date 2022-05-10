

from flask import *
import mydbfile as mb
app=Flask(__name__)

@app.route("/")
def mainpage():
    return render_template("home.html")

@app.route("/Register")
def reg1():
    return render_template("Register.html")    

@app.route("/Register2")
def reg2():
    return render_template("Register2.html")

@app.route("/Login")
def log1():
    return render_template("Login.html")

@app.route("/Login2")
def log2():
    return render_template("Login2.html")        




@app.route("/saveauth", methods=["POST"])    
def save_data_author():
    Username= request.form["Username"]
    Password= request.form["Password"]
    City= request.form["City"]
    myt=(Username,Password,City)
    mb.insert_author(myt)
    return redirect("/Register")

@app.route("/saveuser", methods=["POST"])    
def save_data_user():
    Username= request.form["Username"]
    Password= request.form["Password"]
    City= request.form["City"]
    myt=(Username,Password,City)
    mb.insert_user(myt)
    return redirect("/Register2")    

@app.route("/checkauth",methods=["POST"])
def check_auth_login():
    
    Username= request.form["Username"]
    Password= request.form["Password"]
    t=(Username,Password)
    data=mb.checkauthor(t)
    if data:
        return render_template("welcome_auth.html",name=Username)
    else:
        return redirect("/Login")

@app.route("/checkuser",methods=["POST"])
def check_user_login():
    
    Username= request.form["Username"]
    Password= request.form["Password"]
    t=(Username,Password)
    data=mb.checkuser(t)
    if data:
        data=mb.fetch_all_post()
        return render_template("welcome_user.html",res=data)
    else:
        return redirect("/Login")
    

@app.route("/addpost/<string:name>")
def addpost_fun(name):
    
    return render_template("addpost.html",n=name)

@app.route("/savepost",methods=["POST"])
def save_auth_post():
    Username= request.form["aname"]
    title= request.form["btitle"]
    blog= request.form["blog"]
    t=(Username,title,blog)
    mb.savepostfun(t)
    return render_template("welcome_auth.html",name=Username)

@app.route("/viewpost/<string:name>")
def view_auth(name):
    t=(name,)
    data=mb.view_spec_post(t)
    return render_template("display_auth_post.html",a=data)





if(__name__=="__main__"):
    app.run(debug=True)    