import pypyodbc
from connection import Connection
import mysql.connector
import pyttsx3
import datetime
import os
from time import gmtime, strftime

class Cadastro():

    choice = None
    
    def __init__(self):
        db_access = Connection()
        self.conn = db_access.conecta_msql() # sql server
        self.conn2 = db_access.conecta_mysql() # Mysql
        self.conn2_cloud = db_access.conecta_mysql_cloud() # mysql cloud [name server]     

    def start(self):

        tempo = self.hora()

        if tempo < '12' :
            msg_hello = 'Bom dia!'
        elif tempo >= '12' and tempo < '18':
            msg_hello = 'Boa tarde!'
        elif tempo >= '18' and tempo < '24':
            msg_hello = 'Boa noite!'
        self.speech(msg_hello)

        info = 'escolha o banco de dados, 1 para my sql e 2 para sql server!'

        self.speech(info)

        choice = input("What is the data base: \n1 - for Mysql \n2 - for Sql Server \n\nYour choice: ")

        if choice == '1':
            print("Data base Mysql")
            cursor = self.conn2.cursor(buffered=True)
            obj_conn = self.conn2
        elif choice == '2':
            print("Data base Sql Server")
            cursor = self.conn.cursor()
            obj_conn = self.conn
        else:
            print("Data base default is Mysql cloud")
            cursor = self.conn2_cloud.cursor(buffered=True)
            obj_conn = self.conn2_cloud
            self.speech('Como não escolheu um banco de dados, vamos usar o servidor de produção')
            #self.speech('Como não escolheu um banco de dados, vamos usar o servidor de desenvolvimento local')

        info2 = 'Esta aplicação serve para cadastro de contatos!'
        self.speech(info2)

        self.speech('informe o nome!')
        no = str(input("Digite o nome: "))
        nome_v = 'Ok, o nome será {}', no
        self.speech(nome_v)

        self.speech('informe um e-mail')
        em = str(input("Digite o e-mail: "))
        email_v = 'O email que digitou foi {}', em
        self.speech(email_v)
        
        self.speech('informe o código de àrea!')
        dd = int(input("Digite o ddd: "))
        ddd_v = 'o ddd é {}', dd
        self.speech(ddd_v)
        
        self.speech('informe o telefone')
        ph = int(input("Digite o telefone: "))
        phone_v = 'e seu telefone é {}', ph
        self.speech(phone_v)

        insert = "INSERT INTO contatos (nome, email, ddd, telefone) " \
                "VALUES('%s', '%s', '%i', '%i')" % (no, em, dd, ph)

        if no != '' and em != '' and dd != '' and ph != '':
            cursor.execute(insert)
            obj_conn.commit()
            msg_ok = 'Tudo certo, o cadastro foi realizado com sucesso!'
            self.speech(msg_ok)
        else:
            msg_ok = 'Houve algum problema, imagino que deixou algum campo sem ser preenchido! Por favor preencha!'
            self.speech(msg_ok)

        cursor.execute("SELECT * FROM contatos")
        for row in cursor.fetchall():
            print("\nID: %02d | Nome: %s | e-mail: %s | phone: (%s) %d " % (row[0], row[1], row[2], row[3], row[4]))

        obj_conn.close()
        self.speech('Fim da aplicação!')
    
    def speech(self, text):
        engine = pyttsx3.init()
        engine.say(str(text))
        engine.runAndWait()

    def hora(self):
        temp_time = (int(strftime("%H", gmtime())))
        tempo = str(temp_time - 3)
        if tempo == '-1':
            tempo = '23'
        elif tempo == '-2':
            tempo = '22'
        elif tempo == '-3':
            tempo = '21'

        return tempo

begin = Cadastro()
begin.start()