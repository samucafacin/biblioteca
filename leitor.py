class usuario:
    def __init__(self, nome_usuario, email, id_usuario):
        self.nome_usuario = nome_usuario
        self.email = email
        self.id_usuario = id_usuario
        self.livros_emprestado = []

    def __str__(self):
        return f"{self.nome_usuario} - {self.email} - {len(self.livros_emprestado)}"