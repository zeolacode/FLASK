from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():

    return "Hello World!"

@app.route('/start')
def start():

    return url_for("start", next="login")

@app.route('/google')
def go_to_google():
    
    return redirect('https://www.google.com')

@app.route('/post/<int:id>')
def post(id):

    return f'Showing post: {id}'

@app.route('/today')
def today():

    return redirect(url_for('post', id=50))


@app.route('/git/<string:perfil>')
def git(perfil):   
    git = 'https://github.com/'
    url = git + perfil
    return redirect(url)

@app.route('/ml')
def ml():
    return redirect(url_for('git', perfil='zeolacode'))



if __name__ == "__main__":
    app.run(debug=True)