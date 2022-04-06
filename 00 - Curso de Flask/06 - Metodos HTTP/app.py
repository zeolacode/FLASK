# Aula 06 - Metodos HTTP

# GET - solicita a representação de um recurso específico! Apenas retorna retorna dados
# HEAD - solicita uma resposta idêntica ao metodo GET, porém sem conter o corpo da resposta
# POST - submeter uma entidade a um recurso específico, causando uma mudança no estado do recurço.
# PUT - substitui todas as autuais representações do recurso de destino, pela carga de dados da requisição
# DELETE - remove um recurso específico
# CONNECT - estabelece um túnel para o servidor identificado pelo recurso de destino
# OPTIONS - é usado para descrever as opções de comunicação com o recurso de destino
# TRACE - executa um teste de chamada loop-back junto com o caminho para o recurso de destino
# PATCH - é utilizado para aplicar modificações parciais em um recurso


from flask import Flask, request
import json

app = Flask(__name__, static_folder='public')

@app.route("/add", methods=["GET","POST"])
def add():
    # request ajuda no controle das requisições 
    if request.method == "POST":
        # .form retorna o formulário nome e senha do html
        return json.dumps(request.form)
    else:
        return "OK GET"


if __name__ == '__main__':
    app.run(debug=True)