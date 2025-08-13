import tkinter as tk
from tkinter import messagebox
from livro import livro
from leitor import usuario
from biblioteca import Biblioteca

biblioteca = Biblioteca()


def cadastrar_livro():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    ano = entrada_ano.get()
    qtd = entrada_qtd.get()

    if titulo and autor and ano.isdigit() and qtd.isdigit():
        if not titulo: 
         messagebox.showerror("Erro", "O campo Título não pode estar vazio.")
        return
    if not autor:
        messagebox.showerror("Erro", "O campo Autor não pode estar vazio.")
        return
    if not ano.isdigit():
        messagebox.showerror("Erro", "O campo Ano deve conter apenas números.")
        return
    if not qtd.isdigit():
        messagebox.showerror("Erro", "O campo Quantidade deve conter apenas números.")
        return

    biblioteca.cadastrar_livro(livro(titulo, autor, int(ano), int(qtd)))
    messagebox.showinfo("Sucesso", f"livro '{titulo}' cadastrado!")
    
    messagebox.showwarning("Atenção, Preencha os campos corretamente.")


def cadastrar_usuario():
    nome = entrada_nome.get()
    email = entrada_email.get()
    id_usuario = entrada_id.get()
    ## alterei aqui ****
    if not nome:
        messagebox.showerror("Erro", "O campo Nome não pode estar vazio.")
        return
    if not email:
        messagebox.showerror("Erro", "O campo Email não pode estar vazio.")
        return
    if not id_usuario.isdigit():
        messagebox.showerror("Erro", "O campo ID deve conter apenas números.")
        return

    dominios_validos = ["@hotmail.com", "@gmail.com", "@yahoo.com", "@email.com"]
    if not any(email.lower().endswith(dominio) for dominio in dominios_validos):
        messagebox.showerror("Erro", "O email deve conter um domínio válido.")
        return

    biblioteca.cadastrar_usuario(usuario(nome, email, int(id_usuario)))
    messagebox.showinfo("Sucesso", f"Usuário '{nome}' cadastrado!")

def listar_livros():
    livros = biblioteca.listar_livros()
    if livros:
        messagebox.showinfo("Lista de Livros", "\n".join(livros))
    else:
        messagebox.showinfo("Lista de Livros", "Nenhum livro cadastrado.")
def listar_usuarios():
    usuario = listar_usuarios.listar_usuarios()
    if usuario:
        messagebox.showinfo("Lista de Usuarios", "\n".join(usuario))
    else:
        messagebox.showinfo("Lista de Usuarios", "Nenhum usuario cadastrado.")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


root = tk.Tk()
root.title("Biblioteca APP")

tk.Label(root, text='Título').grid(row=0, column=0)
entrada_titulo = tk.Entry(root)
entrada_titulo.grid(row=0, column=1)

tk.Label(root, text='Autor').grid(row=1, column=0)
entrada_autor = tk.Entry(root)
entrada_autor.grid(row=1, column=1)

tk.Label(root, text='Ano').grid(row=2, column=0)
entrada_ano = tk.Entry(root)
entrada_ano.grid(row=2, column=1)

tk.Label(root, text='Quantidade').grid(row=3, column=0)
entrada_qtd = tk.Entry(root)
entrada_qtd.grid(row=3, column=1)

tk.Button(root, text="Cadastrar Livro",
          command=cadastrar_livro).grid(row=4, column=1)

tk.Label(root, text='Nome').grid(row=5, column=0)
entrada_nome = tk.Entry(root)
entrada_nome.grid(row=5, column=1)

tk.Label(root, text='E-mail').grid(row=6, column=0)
entrada_email = tk.Entry(root)
entrada_email.grid(row=6, column=1)

tk.Label(root, text='ID').grid(row=7, column=0)
entrada_id = tk.Entry(root)
entrada_id.grid(row=7, column=1)

tk.Button(root, text="Cadastrar Usuario",
          command=cadastrar_usuario).grid(row=8, column=1)

tk.Button(root, text="Listar Livros",
          command=listar_livros).grid(row=9, column=1)
tk.Button(root, text="Listar Usuarios",
          command=listar_usuarios).grid(row=10, column=1)

root.mainloop()
