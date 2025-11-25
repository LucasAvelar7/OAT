from datetime import datetime
from src import db

class TarefaModel(db.Model):
    tablename = 'tarefas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.String(500), nullable=True)
    data_entrega = db.Column(db.DateTime, nullable=True)
    entregue = db.Column(db.Boolean, default=False, nullable=False)
 
    aluno_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    aluno = db.relationship('UsuarioModel', backref=db.backref('tarefas', lazy=True))

    def repr(self):
        return f"<Tarefa id={self.id} titulo={self.titulo!r} aluno_id={self.aluno_id}>"
    
    