# -*- coding: utf-8 -*-
from Tkinter import *
app = Tk()
app.title("Trabalhando com banco de Dados")
app.geometry('300x600+100+100')



from conexaobanco import *
banco = Banco()
def vai_capeta(user, mail):
    user = usuario.get()
    mail = email.get()
    Banco.entrada_dados(user, mail)

Label(app, text="Teste de criação, leitura e \n escrita em BD com Sqlite3", width = 200).pack()
Label(app, text = "Usuário: ").pack()
usuario = Entry(app)
usuario.pack()
Label(app, text = "Email: ").pack()
email = Entry(app)
email.pack()



b1 = Button(app, text= "Criar Banco", width=10, height = 5, command = banco.create_table)
b1.pack(side="left", padx=(40, 0), pady=20)
b2 = Button(app, text= "Enviar", width=10, height = 5, command = vai_capeta)
b2.pack(side="left", padx=0, pady=20)

app.mainloop()
