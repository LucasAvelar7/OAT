from src import ma
from src.models import tarefa_model
from marshmallow import fields

class TarefaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = tarefa_model.TarefaModel
        fields = (
            'id',
            'titulo',
            'descricao',
            'data_entrega',
            'entregue',
            'aluno_id'
        )

    titulo = fields.String(required=True)
    descricao = fields.String(required=False, allow_none=True)
    data_entrega = fields.DateTime(required=False, allow_none=True)
    entregue = fields.Boolean(required=False)
    aluno_id = fields.Integer(required=True)