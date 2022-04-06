# AUla 04 - Construcao de url

# importando Flask
from flask import Flask, redirect, url_for

# instanciando objeto Flask
app = Flask(__name__)

@app.route("/admin")
def admin():
    return "<h1> Admin </h1>"

@app.route("/guest/<guest>")
def guest(guest):
    return '<p>olá guest <b> %s </b></p>' %  guest 

@app.route("/user/<name>")
def user(name):
    if name == "admin":
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest = name))

@app.route("/youtube")
def youtube():
    return redirect("https://www.youtube.com")



if __name__ == '__main__':
    app.run(debug=True)