from filme import filme
from Cliente import usuario

class Locafilmes:
    def __init__(self):
        self.filme = []
        self.usuarios = []

    def cadastrar_filme(self, filme):
        self.filme.append(filme)
        print(f"🎦 Filme '{filme.titulo}' cadastrado com sucesso!")

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"🙎 Usuário '{usuario.nome_usuario}' adicionado com sucesso!")

    def emprestar_filme(self, id_usuario, titulo_filme):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        filme = next((l for l in self.filme if l.titulo.lower() == titulo_filme.lower()), None)

        if not usuario:
            print("Usuário não encontrado!!")
            return
        if not filme:
            print("Filme não encontrado!!")
            return
        if filme.quantidade <= 0:
            print("Filme indisponível.")
            return

        usuario.filmes_emprestado.append(filme.titulo)
        filme.quantidade -= 1
        print(f"✅ Filme '{filme.titulo}' emprestado para {usuario.nome_usuario}.")

    def devolver_filme(self, id_usuario, titulo_filme):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if not usuario:
            print("Usuário não encontrado.")
            return

        if titulo_filme not in usuario.filmes_emprestado:
            print("Este filme não está com este usuário.")
            return

        usuario.filmes_emprestado.remove(titulo_filme)
        for filme in self.filme:
            if filme.titulo.lower() == titulo_filme.lower():
                filme.quantidade += 1
                break

        print(f"🎦 Filme '{titulo_filme}' devolvido por {usuario.nome_usuario}.")

    def listar_filmes(self):
       if not self.filme:
          return []
       return [f"{filme.titulo} - {filme.autor} ({filme.ano}) - {filme.quantidade} disponíveis"
               for filme in self.filme]


    def listar_usuarios(self):
        if not self.usuarios:
            return []
        return [f"{usuario.nome_usuario} - {usuario.email} de ID: {usuario.id_usuario}"
                for usuario in self.usuarios]
