# -*- coding: iso8859-1 -*-
import sqlite3
import time
import datetime
class Banco:

    def __init__(self):
        self.connection = sqlite3.connect('dadosemails.db')
        self.c = self.connection.cursor()


    def create_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS dados (ids INTEGER PRIMARY KEY NOT NULL, usuario varchar , email text NOT NULL, date text )')
        self.connection.commit()

    def entrada_dados(self, usuario, email):
        self.data = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
        self.c.execute("INSERT INTO dados (usuario, email, date) VALUES(?,?,?)",(usuario, email, self.data))
        self.connection.commit()

    def consulta_dados(self, usuario):
        chamada = self.c.execute("SELECT * FROM dados WHERE usuario=?",(usuario))

        #date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
        #self.c.execute("INSERT INTO dados (usuario, email, mensagem, date) VALUES (?, ?, ?, ?)", (usuario, email, comentario, date))
        #self.connection.commit()

