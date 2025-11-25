from ..models.tarefa_model import TarefaModel
from ..schemas.tarefa_schema import TarefaSchema
from src import db
from datetime import datetime


def cadastrar_tarefa(tarefa):
    tarefa_db = TarefaModel(
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        data_entrega=tarefa.data_entrega,
        entregue=tarefa.entregue,
        aluno_id=tarefa.aluno_id
    )

    db.session.add(tarefa_db)
    db.session.commit()
    return tarefa_db


def listar_tarefas():
    return TarefaModel.query.all()


def listar_tarefa_id(id):
    try:
        tarefa = TarefaModel.query.get(id)
        return tarefa
    except Exception as e:
        print(f"Erro ao buscar tarefa por ID: {e}")
        return None


def listar_tarefas_por_aluno(aluno_id):
    return TarefaModel.query.filter_by(aluno_id=aluno_id).all()


def editar_tarefa(id, nova_tarefa):
    tarefa = TarefaModel.query.get(id)

    if tarefa:
        tarefa.titulo = nova_tarefa.titulo
        tarefa.descricao = nova_tarefa.descricao
        tarefa.data_entrega = nova_tarefa.data_entrega
        tarefa.entregue = nova_tarefa.entregue
        tarefa.aluno_id = nova_tarefa.aluno_id

        db.session.commit()
        return tarefa

    return None


def excluir_tarefa(id):
    tarefa = TarefaModel.query.get(id)

    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
        return True

    return False