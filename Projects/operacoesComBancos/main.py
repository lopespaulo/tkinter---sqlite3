# -*- coding: utf-8 -*-
from Tkinter import *
from conexaobanco import *

class Main:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        Label(self.frame, text="Usuário").pack()
        self.user = Entry(self.frame, width=40)
        self.user.pack()
        Label(self.frame, text="Email").pack()
        self.email = Entry(self.frame, width=40)
        self.email.pack()
        self.frame2 = Frame(master)
        self.frame2.pack()
        self.add = Button(self.frame2, text="Salvar", width=40, command=self.vai_banco)
        self.add.pack()
        self.find = Button(self.frame2, text="Consultar", width=40, command=self.consulta_banco)
        self.find.pack(side="bottom")



        barralateral = Scrollbar(master)
        barralateral.pack(fill=Y, side=RIGHT)
        self.caixalista = Listbox(master, width=75, height=40)
        self.caixalista.pack(padx=5, pady=5)
        self.caixalista.config(yscrollcommand= barralateral.set)
        barralateral.config(command=self.caixalista.yview)

        self.Banco = Banco()
        self.Banco.create_table()





    def vai_banco(self):
        usuario = self.user.get()
        email = self.email.get()
        self.Banco.entrada_dados(usuario, email)



    def consulta_banco(self):
        usuario = self.user.get()
        chamada = self.Banco.chamada_dados(usuario)
        for i in chamada:
            self.caixalista.insert(END,i) #Preciso receber dados do banco




    def apaga_capeta(self):
        pass

        #banco
        #self.conectar = sqlite3.connect("dadoseemails.db")
        #self.cursor = self.conectar.cursor()
        #self.cursor.execute("CREATE TABLE IF NOT EXISTS dados (ids INTEGER PRIMARY KEY NOT NULL, usuario text, email text, date text )")
        #self.conectar.commit()
        #self.date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))

app = Tk()
app.title("teste com sqlite3")
app.geometry("300x400")
Main(app)
app.mainloop()



#def vai_capeta():

    #global email
    #global commentario
    #print (user)
    #Banco.entrada_dados(usuario, email, commentario)

#lab = Label(app, text="Teste de criação, leitura e \n escrita em BD com Sqlite3", width = 200)
#lab.pack(side='top')

#Label(app, text = "Usuário: ").pack()
#usuario = Entry(app, bd= 0)
#usuario.pack()
#user = usuario.get()

#Label(app, text = "Email: ").pack()
#email = Entry(app, bd = 0)
#email.pack()
#email = email.get()

#Label(app, text = "Comentário: ").pack()
#comentario = Entry(app)
#comentario.pack()
#commentario = comentario.get()

#Banco = Banco()


#b1 = Button(app, text= "Criar Tabela", width=10, height = 5, command = Banco.create_table)
#b1.pack(side="left", padx=(40, 0), pady=20)
#b2 = Button(app, text= "Enviar", width=10, height = 5, command = vai_capeta)
#b2.pack(side="left", padx=0, pady=20)

##side="left"
##side="left"


#app.mainloop()
#
