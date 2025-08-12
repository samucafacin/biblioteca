from livro import livro
from leitor import usuario

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        print(f"📘 Livro '{livro.titulo}' cadastrado com sucesso!")

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"🙎 Usuário '{usuario.nome_usuario}' adicionado com sucesso!")

    def emprestar_livro(self, id_usuario, titulo_livro):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        livro = next((l for l in self.livros if l.titulo.lower() == titulo_livro.lower()), None)

        if not usuario:
            print("Usuário não encontrado!!")
            return
        if not livro:
            print("Livro não encontrado!!")
            return
        if livro.quantidade <= 0:
            print("Livro indisponível.")
            return

        usuario.livros_emprestado.append(livro.titulo)
        livro.quantidade -= 1
        print(f"✅ Livro '{livro.titulo}' emprestado para {usuario.nome_usuario}.")

    def devolver_livro(self, id_usuario, titulo_livro):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if not usuario:
            print("Usuário não encontrado.")
            return

        if titulo_livro not in usuario.livros_emprestado:
            print("Este livro não está com este usuário.")
            return

        usuario.livros_emprestado.remove(titulo_livro)
        for livro in self.livros:
            if livro.titulo.lower() == titulo_livro.lower():
                livro.quantidade += 1
                break

        print(f"🔄 Livro '{titulo_livro}' devolvido por {usuario.nome_usuario}.")

    def listar_livros(self):
        print("\n 📖Lista de livros📖")
        for livro in self.livros:
            print(livro)

    def listar_usuarios(self):
        print("\n 🧑‍🦲Lista de Usuários:")
        for usuario in self.usuarios:
            print(usuario)
