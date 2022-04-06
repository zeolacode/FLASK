from flask import Blueprint, Response, request
import json
from models.models import db, Disciplina


app = Blueprint("disciplina", __name__)


@app.route('/')
def index():
    disciplina = Disciplina.query.all()
    result = [e.to_dict() for e in disciplina]
    return Response(response=json.dumps(result), status=200, content_type="application/json")

@app.route('/view/<int:id>', methods= ['GET'])
def view(id):
    row = db.session.execute("select * from disciplina where id = %s" % id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")

@app.route('/add', methods=["POST"])
def add():
    disciplina = Disciplina(request.form['nome'])
    db.session.add(disciplina)
    db.session.commit()
    return Response(response=json.dumps({'status': 'success','data': disciplina.to_dict()}), status=200, content_type="application/json")



@app.route('/edit/<int:id>', methods=["PUT", "POST"])
def edit(id):
    disciplina = Disciplina.query.get(id)
    disciplina.nome = request.form['nome']
    db.session.commit()
    return Response(response=json.dumps(disciplina.to_dict()), status=200, content_type="application/json")




@app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    estudante = Disciplina.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type="application/json")
