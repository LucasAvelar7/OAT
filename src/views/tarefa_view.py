from flask_restful import Resource
from marshmallow import ValidationError
from flask import request, jsonify, make_response
from src.schemas import tarefa_schema
from src.models.tarefa_model import TarefaModel
from src.services import tarefa_service
from src import api


class TarefaList(Resource):
    def get(self):
        tarefas = tarefa_service.listar_tarefas()

        if not tarefas:
            return make_response(jsonify({"message": "Não existem tarefas cadastradas"}), 404)

        schema = tarefa_schema.TarefaSchema(many=True)
        return make_response(jsonify(schema.dump(tarefas)), 200)

    def post(self):
        schema = tarefa_schema.TarefaSchema()

      
        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

        try:
            nova_tarefa = TarefaModel(
                titulo=dados["titulo"],
                descricao=dados.get("descricao"),
                data_entrega=dados.get("data_entrega"),
                entregue=dados.get("entregue", False),
                aluno_id=dados["aluno_id"]
            )

            resultado = tarefa_service.cadastrar_tarefa(nova_tarefa)
            return make_response(jsonify(schema.dump(resultado)), 201)

        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 400)


api.add_resource(TarefaList, "/tarefas")

class TarefaResource(Resource):
    def get(self, id_tarefa):
        tarefa = tarefa_service.listar_tarefa_id(id_tarefa)

        if tarefa:
            schema = tarefa_schema.TarefaSchema()
            return make_response(jsonify(schema.dump(tarefa)), 200)

        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

    def put(self, id_tarefa):
        schema = tarefa_schema.TarefaSchema()

        try:
            dados = schema.load(request.json)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)

        tarefa_editada = tarefa_service.editar_tarefa(id_tarefa, dados)

        if tarefa_editada:
            return make_response(jsonify(schema.dump(tarefa_editada)), 200)

        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)

    def delete(self, id_tarefa):
        if tarefa_service.excluir_tarefa(id_tarefa):
            return make_response(jsonify({"message": "Tarefa excluída com sucesso"}), 200)

        return make_response(jsonify({"message": "Tarefa não encontrada"}), 404)


api.add_resource(TarefaResource, "/tarefas/<int:id_tarefa>")