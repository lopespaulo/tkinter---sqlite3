# -*- coding: utf-8 -*-
from Tkinter import *
from datetime import datetime



class main:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        Label(self.frame, text="Analista").pack()
        self.analista = Entry(self.frame, width=30)
        self.analista.pack()
        Label(self.frame, text="Cliente").pack()
        self.cliente = Entry(self.frame, width=30)
        self.cliente.pack()
        self.criar = Button(self.frame, text="Salvar", width=30, command= self.move_toclipboard)
        self.criar.pack()

    def move_toclipboard(self):
        analista = self.analista.get()
        cliente = self.cliente.get()
        now = datetime.now()
        if now.hour < 12:
            hora = ("um Bom dia")
        else:
            hora = ("uma Boa tarde")
        app.clipboard_clear()
        app.clipboard_append("""Agradecemos seu contato %s. \n Tenha %s. Em caso de duvidas permanecemos a disposição. \n\n Att, \n %s. \n Suporte Engematica.""" %(cliente, hora, analista))

app = Tk()
app.title=("Assinatura de Atendimento.")
app.clipboard_clear()
main(app)

app.mainloop()