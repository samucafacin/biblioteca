
class livro:
    def __init__(self, titulo, autor, ano, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.quantidade = quantidade

    def __str__(self):
      return f"{self.titulo} {self.ano} {self.autor} | Quantidade Disponível {self.quantidade}"