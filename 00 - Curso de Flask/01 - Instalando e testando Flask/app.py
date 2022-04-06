# Aula 01 - Instalando e testando Flask

# importando Flask
from flask import Flask

# instanciando objeto Flask
app = Flask(__name__)

# criando rotas 
# responde como index
@app.route("/")
def index():
    return "index"

# criando outra rota
@app.route("/rota2")
def rota2():
    return "Rota2"

# é usado para executar algum código apenas se o arquivo foi executado diretamente, e não importado.
if __name__ == '__main__':
    app.run()