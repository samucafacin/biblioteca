from livro import livro
from leitor import usuario
from biblioteca import Biblioteca

def main():  # alimentação da biblioteca
    biblioteca = Biblioteca()

    biblioteca.cadastrar_livro(livro("Python para pycoders", "Samuel Facin", 2020, 3))
    biblioteca.cadastrar_livro(livro("POO em python", " Sandra Facin", 2023, 2))

    biblioteca.cadastrar_usuario(usuario("Gabriel", "cleitogabriel@email.com", 1))
    biblioteca.cadastrar_usuario(usuario("Ellen", "ellen@email.com", 2))

    # emprestar e devolver
    biblioteca.emprestar_livro(1, "Python para pycodrers")
    biblioteca.emprestar_livro(2, "POO em python")
    biblioteca.devolver_livro(1, "Python para pycoders")

    biblioteca.listar_livros()
    biblioteca.listar_usuarios()

if __name__ == "__main__":
    main()
