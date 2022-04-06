# Aula 09 - Templates (jinga 2)
from re import T
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates')



# http://127.0.0.1:5000/?nome=Pedro&idade=24
@app.route('/')
def index():
    x = 50
    y = 20
    query = request.args.to_dict()
    return render_template('modelo.html', x=x, y=y, query=query)



if __name__ == '__main__':
    app.run(debug=True)