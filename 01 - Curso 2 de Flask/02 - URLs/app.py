from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/ola')
def hola():
    return "ola."

# !!! <varType:varName> !!! (string, int, float, path, uuid)
# string
@app.route('/user/<string:user>')
def user(user):
    return "Ola " + user

# int
@app.route('/post/<int:post_id>')
def post(post_id):
    return f'Post {post_id}'

# float
@app.route('/floats/<float:num>')
def floatNum(num):
    return f'Num: {num}'


# path (permite passar barras pela url [ / ])
@app.route('/path/<path:sub_path>')
def path(sub_path):
    return f'Path: {escape(sub_path)}'

# Ex: 123e4567-e89b-12d3-a456-426655440000
@app.route('/uuid/<uuid:subUuid>')
def uuid(subUuid):
    return f'UUID: {subUuid}'

# testes...

@app.route('/users/<int:id>/<string:name>')
def users(id, name):
    return f'ID: {id} e Nome: {name}'

@app.route('/soma/<int:num1>/<int:num2>')
def soma(num1, num2):
    return f'A soma é: {num1 + num2}'

@app.route('/default')
@app.route('/default/<string:tipo>')
def default(tipo='Car'):
    return f'Tipo: {tipo}'

@app.route('/imc/<float:peso>/<float:altura>')
def imc(peso, altura):
    return f'O seu imc é: {peso/(altura*altura)}'

@app.route('/cadastro/<string:nome>/<int:idade>/<string:sexo>/<string:profissao>')
def cadastro(nome, idade, sexo, profissao):
    return f'Nome: {nome}, Idade: {idade}, Sexo: {sexo}, Profissão: {profissao}'

if __name__ == "__main__":
    app.run(debug=True)