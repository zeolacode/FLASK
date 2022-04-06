# Aula 07 - Objetos de Requisição 

from flask import Flask, request
import json


app = Flask(__name__)


# http://127.0.0.1:5000/?nome=Teste&idade=10

@app.route("/", methods=["GET", "POST"])
def index():
    #print(request.method, request.args)
    d1 = request.args.to_dict()
    d2 = dict(request.args)
    return json.dumps([d1['nome'], d2['idade']])


if __name__=='__main__':
    app.run(debug=True)