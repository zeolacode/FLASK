# Aula 02 - Criando Rotas e configurações
from flask import Flask

# instanciando objeto flask 
app = Flask(__name__)

# Criando Rotas
@app.route("/")
def index():
    return "Index"

# outra froma de criar rotas 
# regar - "/teste"
# endpoint - "teste" nome da regra
# function

def teste():
    return "<p>Teste</p>" 

def teste2():
    return "<h1>Teste 02</h1>"


app.add_url_rule("/teste", "teste", teste)
app.add_url_rule("/teste2", "teste2", teste2)

# executar código, somente se o arquivo for executado diretamente e não importado! 
if __name__ == '__main__':
    app.run(debug=True, port="3000")  # host= IP