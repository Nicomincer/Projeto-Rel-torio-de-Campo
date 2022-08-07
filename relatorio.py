import tkinter

programa = tkinter.Tk("Relátorio")
programa.title("Tela")
programa.configure(background="lightblue")
programa.geometry("600x500")
programa.resizable(True, True)
programa.maxsize(width=980, height=780)
programa.minsize(width=480, height=380)

frame_colocarinfo = tkinter.Frame(programa, bd=4, bg="white", highlightbackground="blue", highlightthickness=2)
frame_colocarinfo.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.46)

frame_arvore = tkinter.Frame(programa, bd=4, bg="white", highlightbackground="blue", highlightthickness=2)
frame_arvore.place(relx=0.02 , rely=0.5, relwidth=0.96, relheight=0.46)

botão_limpar = tkinter.Button(frame_colocarinfo, text="Limpar")
botão_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

botão_buscar = tkinter.Button(frame_colocarinfo, text="Buscar")
botão_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

botão_novo = tkinter.Button(frame_colocarinfo, text="Novo")
botão_novo.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.15)

botão_alterar = tkinter.Button(frame_colocarinfo, text="Alterar")
botão_alterar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

botão_apagar = tkinter.Button(frame_colocarinfo, text="Apagar")
botão_apagar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

programa.mainloop()