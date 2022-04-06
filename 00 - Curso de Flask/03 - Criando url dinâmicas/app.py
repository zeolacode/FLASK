# Aula 03 - Criando url dinâmicas 

from flask import Flask 

app = Flask(__name__)


# url dinâmica
@app.route('/ola/')

@app.route("/ola/<nome>")
def ola(nome=""):
    return "<h1>Ola {}</h1>".format(nome)

# add link (blog) int 
@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID = -1):
    if postID >= 0:
        return "blog int {}".format(postID)
    else:
        return "blog int todo"

# tipo float
@app.route('/blog/')
@app.route('/blog/<float:postID>')
def blog2(postID = -1):
    if postID >= 0:
        return "blog float {}".format(postID)
    else:
        return "blog float todo"


if __name__ == '__main__':
    app.run(debug=True)