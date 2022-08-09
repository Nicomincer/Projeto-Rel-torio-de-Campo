from asyncio.windows_events import NULL
from sre_compile import isstring
import string
import tkinter
from tkinter import END, Scrollbar, ttk
from tkinter.messagebox import NO 
import sqlite3

def montar_tabela():
    global banco_de_dados, cursor
    banco_de_dados = sqlite3.connect("horasdecampo.bd")
    cursor = banco_de_dados.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS relatorio(
        Nome CHAR(40) NOT NULL,
        Horas FLOAT (20),
        Publicações INTEGER (20),
        Estudos INTEGER(20)
    );"""
)
def limpar():
    global colocar_nome, colocar_estudos, colocar_hora, colocar_publicações, anotações_do_campo
    colocar_nome.delete(0, END)
    colocar_estudos.delete(0, END)
    colocar_hora.delete(0, END)
    colocar_publicações.delete(0, END)

def conectar():
    global banco_de_dados, cursor
    banco_de_dados = sqlite3.connect("horasdecampo.bd")
    cursor = banco_de_dados.cursor()

def fechar():
    banco_de_dados.close()
def add():
    global colocar_nome, colocar_estudos, colocar_hora, colocar_publicações, anotações_do_campo, nome, estudos, horas, publicações
    conectar()
    nome = colocar_nome.get()
    estudos = colocar_estudos.get()
    horas = colocar_hora.get()
    publicações = colocar_publicações.get()
    if len(nome) != 0:
        cursor.execute(f""" INSERT INTO relatorio(Nome, Horas, Publicações, Estudos) VALUES (?, ?, ?, ?)
        """, (nome, estudos, horas, publicações))
        banco_de_dados.commit()
        fechar()
        select()
        limpar()
    else:
        fechar()
        select()
        limpar()

def select():
    global anotações_do_campo
    anotações_do_campo.delete(*anotações_do_campo.get_children())
    conectar()
    list = cursor.execute(""" SELECT Nome, Horas, Publicações, Estudos FROM relatorio; """)
    for i in list:
        anotações_do_campo.insert("", END, values=i)
    fechar()

montar_tabela()
programa = tkinter.Tk("Relátorio")
programa.title("Tela")
programa.configure(background="lightblue")
programa.geometry("600x500")
programa.resizable(True, True)
programa.maxsize(width=980, height=780)
programa.minsize(width=480, height=380)

frame_colocarinfo = tkinter.Frame(programa, bd=4, bg="#DCDCDC", highlightbackground="blue", highlightthickness=2)
frame_colocarinfo.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.46)

frame_arvore = tkinter.Frame(programa, bd=4, bg="#D3D3D3", highlightbackground="blue", highlightthickness=2)
frame_arvore.place(relx=0.02 , rely=0.5, relwidth=0.96, relheight=0.46)

botão_limpar = tkinter.Button(frame_colocarinfo, text="Limpar", command=limpar)
botão_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

botão_buscar = tkinter.Button(frame_colocarinfo, text="Buscar")
botão_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

botão_novo = tkinter.Button(frame_colocarinfo, text="Novo", command=add)
botão_novo.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)

botão_alterar = tkinter.Button(frame_colocarinfo, text="Alterar")
botão_alterar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

botão_apagar = tkinter.Button(frame_colocarinfo, text="Apagar")
botão_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

texto_nome = tkinter.Label(frame_colocarinfo, text="Nome", font="arial")
texto_nome.place(relx=0.05, rely=0.35)

colocar_nome = tkinter.Entry(frame_colocarinfo,background='white', bd=2, fg='black')
colocar_nome.place(relx=0.05, rely=0.45, relwidth=0.35)

texto_hora = tkinter.Label(frame_colocarinfo, text="Horas", font="arial")
texto_hora.place(relx=0.05, rely=0.65)

colocar_hora = tkinter.Entry(frame_colocarinfo, bd=2)
colocar_hora.place(relx=0.05, rely=0.75)

texto_publicações = tkinter.Label(frame_colocarinfo, text="Publicações", font="arial")
texto_publicações.place(relx=0.55, rely=0.35)

colocar_publicações = tkinter.Entry(frame_colocarinfo, bd=2)
colocar_publicações.place(relx=0.55, rely=0.45)

texto_estudos = tkinter.Label(frame_colocarinfo, text="Estudos", font="arial")
texto_estudos.place(relx=0.55, rely=0.65)

colocar_estudos = tkinter.Entry(frame_colocarinfo, bd=2)
colocar_estudos.place(relx=0.55, rely=0.75)

anotações_do_campo = ttk.Treeview(frame_arvore, height=3, columns=("col1", "col2", "col3", "col4"))

anotações_do_campo.heading("#0", text="")
anotações_do_campo.heading("#1", text="Nome")
anotações_do_campo.heading("#2", text="Horas")
anotações_do_campo.heading("#3", text="Publicações")
anotações_do_campo.heading("#4", text="Estudos")

anotações_do_campo.column("#0", width=1)
anotações_do_campo.column("#1", width=200)
anotações_do_campo.column("#2", width=50)
anotações_do_campo.column("#3", width=125)
anotações_do_campo.column("#4", width=50)
anotações_do_campo.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

barra_de_rolagem = Scrollbar(frame_arvore, orient='vertical')
anotações_do_campo.configure(yscroll=barra_de_rolagem)
barra_de_rolagem.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

programa.mainloop()