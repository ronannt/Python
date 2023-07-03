import mysql.connector
from mysql.connector import errorcode

class Funcs:
    def Login(self, user, pasw):
        try:
            self.db_con = mysql.connector.connect(host='localhost', user=user, password=pasw, database='basevendas')
            print("Conectado!")
            self.cursor = self.db_con.cursor()
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Servidor indisponível!")
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuário ou senha incorreto!")
        else:
            print("Concluído!")

user = input("Digite seu usuário:")
pasw = input("Digite sua senha:")
Funcs.Login(Funcs, user, pasw)