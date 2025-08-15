import tkinter as tk
from tkinter import messagebox
from filme import filme
from Cliente import usuario
from Locafilmes import Locafilmes


import psycopg2


DB_CONFIG = {
    'host': 'localhost',
    'database': 'locadora',
    'user': 'admin',       
    'password': 'ssdele12'      
}

class Usuario:
    def __init__(self, nome_usuario, email, id_usuario=None):
        self.nome_usuario = nome_usuario
        self.email = email
        self.id_usuario = id_usuario
        self.filmes_emprestado = []

    def __str__(self):
        return f"{self.nome_usuario} - {self.email} - {len(self.filmes_emprestado)}"

    # Salvar no banco
    def salvar(self):
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        if self.id_usuario is None:  # Inserir novo usuário
            cursor.execute(
                "INSERT INTO usuarios (nome_usuario, email) VALUES (%s, %s) RETURNING id_usuario",
                (self.nome_usuario, self.email)
            )
            self.id_usuario = cursor.fetchone()[0]  # pega o ID gerado
        else:  # Atualizar usuário existente
            cursor.execute(
                "UPDATE usuarios SET nome_usuario = %s, email = %s WHERE id_usuario = %s",
                (self.nome_usuario, self.email, self.id_usuario)
            )

        conn.commit()
        cursor.close()
        conn.close()

    # Buscar usuário pelo ID
    @staticmethod
    def buscar_por_id(id_usuario):
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_usuario, nome_usuario, email FROM usuarios WHERE id_usuario = %s",
            (id_usuario,)
        )
        linha = cursor.fetchone()
        cursor.close()
        conn.close()
        if linha:
            return Usuario(linha[1], linha[2], linha[0])
        return None

    # Listar todos os usuários
    @staticmethod
    def listar_todos():
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT id_usuario, nome_usuario, email FROM usuarios")
        usuarios = [Usuario(linha[1], linha[2], linha[0]) for linha in cursor.fetchall()]
        cursor.close()
        conn.close()
        return usuarios
    import psycopg2

DB_CONFIG = {
    'host': 'localhost',
    'database': 'locadora',
    'user': 'seu_usuario',    # troque pelo seu usuário PostgreSQL
    'password': 'sua_senha'   # troque pela sua senha
}

class Filme:
    def __init__(self, titulo, autor, ano, quantidade, id_filme=None):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.quantidade = quantidade
        self.id_filme = id_filme

    def __str__(self):
        return f"{self.titulo} {self.ano} {self.autor} | Quantidade Disponível {self.quantidade}"

    # Salvar no banco
    def salvar(self):
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        if self.id_filme is None:  # Inserir novo filme
            cursor.execute(
                "INSERT INTO filmes (titulo, autor, ano, quantidade) VALUES (%s, %s, %s, %s) RETURNING id_filme",
                (self.titulo, self.autor, self.ano, self.quantidade)
            )
            self.id_filme = cursor.fetchone()[0]
        else:  # Atualizar filme existente
            cursor.execute(
                "UPDATE filmes SET titulo = %s, autor = %s, ano = %s, quantidade = %s WHERE id_filme = %s",
                (self.titulo, self.autor, self.ano, self.quantidade, self.id_filme)
            )

        conn.commit()
        cursor.close()
        conn.close()

    # Buscar filme pelo ID
    @staticmethod
    def buscar_por_id(id_filme):
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_filme, titulo, autor, ano, quantidade FROM filmes WHERE id_filme = %s",
            (id_filme,)
        )
        linha = cursor.fetchone()
        cursor.close()
        conn.close()
        if linha:
            return Filme(linha[1], linha[2], linha[3], linha[4], linha[0])
        return None

    # Listar todos os filmes
    @staticmethod
    def listar_todos():
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT id_filme, titulo, autor, ano, quantidade FROM filmes")
        filmes = [Filme(linha[1], linha[2], linha[3], linha[4], linha[0]) for linha in cursor.fetchall()]
        cursor.close()
        conn.close()
        return filmes




Locafilmes = Locafilmes()

# ------------------- Funções -------------------

def cadastrar_filmes():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    ano = entrada_ano.get()
    qtd = entrada_qtd.get()

    if titulo and autor and ano.isdigit() and qtd.isdigit():
        Locafilmes.cadastrar_filme(filme(titulo, autor, int(ano), int(qtd)))
        messagebox.showinfo("Sucesso", f"Filme '{titulo}' cadastrado!")
        resumo()
    else:
        messagebox.showwarning("Atenção", "Preencha os campos corretamente.")

def cadastrar_usuario():
    nome = entrada_nome.get()
    email = entrada_email.get()
    id_usuario = entrada_id.get()

    if not "@" in email:
        messagebox.showwarning(
            "Atenção", "O email deve conter um domínio válido.")
        return

    if nome and email and id_usuario.isdigit():
        Locafilmes.cadastrar_usuario(usuario(nome, email, int(id_usuario)))
        messagebox.showinfo("Sucesso", f"Usuário '{nome}' cadastrado!")
    else:
        messagebox.showwarning("Atenção", "Preencha os campos corretamente.")

def listar_filmes():
    filmes = Locafilmes.listar_filmes()
    messagebox.showinfo("Lista de filmes", "\n".join(
        filmes) if filmes else "Nenhum filme cadastrado.")


def listar_usuarios():
    usuarios = Locafilmes.listar_usuarios()
    messagebox.showinfo("Lista de Usuários", "\n".join(
        usuarios) if usuarios else "Nenhum usuário cadastrado.")


def resumo():
    total_disponivel = sum(filme.quantidade for filme in Locafilmes.filme)
    total_emprestado = sum(len(u.filmes_emprestado)
                           for u in Locafilmes.usuarios)
    label_resumo.config(
        text=f"🎦 Filmes Disponíveis: {total_disponivel} || Filmes Emprestados: {total_emprestado}"
    )


def emprestar_filme():
    id_usuario = entrada_id.get()
    titulo = entrada_titulo.get()

    if not id_usuario.isdigit() or not titulo:
        messagebox.showwarning(
            "Atenção", "Informe o ID do usuário e o título do filme.")
        return

    Locafilmes.emprestar_filme(int(id_usuario), titulo)
    resumo()


def devolver_filme():
    id_usuario = entrada_id.get()
    titulo = entrada_titulo.get()

    if not id_usuario.isdigit() or not titulo:
        messagebox.showwarning(
            "Atenção", "Informe o ID do usuário e o título do filme.")
        return

    Locafilmes.devolver_filme(int(id_usuario), titulo)
    resumo()

# ------------------- Interface Tkinter -------------------

root = tk.Tk()
root.title("🎦 LokLok Locadora APP 🎦")


root.minsize(500, 400)

root.update_idletasks()
width = 800
height = 600
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")


root.geometry("400x400")
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

tk.Button(root, text="Cadastrar Filme",
          command=cadastrar_filmes).grid(row=4, column=1)


tk.Label(root, text='Nome').grid(row=5, column=0)
entrada_nome = tk.Entry(root)
entrada_nome.grid(row=5, column=1)

tk.Label(root, text='E-mail').grid(row=6, column=0)
entrada_email = tk.Entry(root)
entrada_email.grid(row=6, column=1)

tk.Label(root, text='ID').grid(row=7, column=0)
entrada_id = tk.Entry(root)
entrada_id.grid(row=7, column=1)

tk.Button(root, text="Cadastrar Cliente",
          command=cadastrar_usuario).grid(row=8, column=1)


btn_listar_filmes = tk.Button(
    root, 
    text="Listar Filmes",
    command=listar_filmes,
    bg="#4CAF50",     
    fg="white",       
    font=("Arial", 9, "bold"),
    width=13, 
    height=1,
    relief="raised",
    bd=3
)
btn_listar_filmes.grid(row=9, column=0, padx=5, pady=5)

btn_listar_usuarios = tk.Button(
    root, 
    text="Listar Usuários",
    command=listar_usuarios,
    bg="#2196F3",     
    fg="white",
    font=("Arial", 9, "bold"),
    width=13, 
    height=1,
    relief="raised",
    bd=3
)
btn_listar_usuarios.grid(row=9, column=1, padx=5, pady=5)



btn_emprestar_filme = tk.Button(
    root,
    text="🎦 Emprestar Filme",
    command=emprestar_filme,
    bg="#AD7828",      
    fg="white",        
    font=("Arial", 8, "bold"),
    width=14,
    height=1,
    relief="raised",
    bd=3
)
btn_emprestar_filme.grid(row=10, column=0, padx=5, pady=5)

btn_devolver_filme = tk.Button(
    root,
    text="🎦 Devolver Filme",
    command=devolver_filme,
    bg="#9C27B0",      
    fg="white",
    font=("Arial", 9, "bold"),
    width=14,
    height=1,
    relief="raised",
    bd=3
)
btn_devolver_filme.grid(row=10, column=1, padx=5, pady=5)


# Label de Resumo
label_resumo = tk.Label(root, bd=1, anchor="w")
label_resumo.grid(row=11, column=0, columnspan=2, sticky="we")
resumo()

root.mainloop()
