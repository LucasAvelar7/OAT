class Tarefa:
    def init(self, titulo, descricao=None, data_entrega=None, entregue=False, aluno_id=None):
        self.titulo = titulo
        self.descricao = descricao
        self.data_entrega = data_entrega
        self.entregue = entregue
        self.aluno_id = aluno_id

    # --- titulo ---
    @property
    def titulo(self):
        return self.titulo

    @titulo.setter
    def titulo(self, titulo):
        self.titulo = titulo

    # --- descricao ---
    @property
    def descricao(self):
        return self.descricao

    @descricao.setter
    def descricao(self, descricao):
        self.descricao = descricao

    # --- data_entrega ---
    @property
    def data_entrega(self):
        return self.data_entrega

    @data_entrega.setter
    def data_entrega(self, data_entrega):
        self.data_entrega = data_entrega

    # --- entregue ---
    @property
    def entregue(self):
        return self.entregue

    @entregue.setter
    def entregue(self, entregue):
        self.entregue = entregue

    # --- aluno_id ---
    @property
    def aluno_id(self):
        return self.aluno_id

    @aluno_id.setter
    def aluno_id(self, aluno_id):
        self.__aluno_id = aluno_id
