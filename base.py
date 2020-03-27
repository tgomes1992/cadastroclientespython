import csv
import os
import datetime
import sqlite3

#mapa
#Cadastra
#Gera CSV
#Importa para um banco de Dados

new_csv = []
now = datetime.datetime.now()

class Clientes():
    def __init__(self):
        print("Construtor Cliente")
    def novo_cliente(self):
        self.name = "Teste"
        self.endereco = "Teste"
        self.idade = '28'
        self.nascimento = "teste"
        self.telefone = "teste"

class BancoClientes(Clientes):
    def __init__(self):
        self.conection =  sqlite3.connect("clientes.db")
        self.curs = self.conection.cursor()
    def inserir_cliente(self):
        Clientes.novo_cliente(self)
        self.curs.execute('''INSERT into clientes values (?,?,?,?,?)''',(self.name,self.endereco,self.idade,self.nascimento,self.telefone))
    def deletar_dados(self):
        self.curs.execute('''DELETE FROM clientes WHERE Endereço="Teste" ''')
    def close_connection(self):
        self.conection.close()
    def commit_changes(self):
        self.conection.commit()

def desejodecadastro():
    print("Deseja Cadastrar um novo cliente: ")
    a = "yes"
    b = "no"
    c = input("Digite yes ou no: ")
    if c.lower()==a:
        return True
    elif c.lower() == b:
        return False
    else:
        print("Valor inválido")
        return desejodecadastro()

def write_csv():
    csv_name = ("Clientes Cadastrados-" + now.strftime("%d %b  %H-%M-%S")+".csv")
    csv_header = ["Nome","Endereço", "Idade","Nascimento" ,"Telefone"]
    csv_file = open(os.path.join("C:/Users/thiag/Desktop/Cadastro de Clientes Python/Log",csv_name) +".csv","w",newline="")
    writer = csv.writer(csv_file,delimiter=";")
    writer.writerow(csv_header)
    writer.writerows(new_csv)
    print (new_csv)


while desejodecadastro():
    Banco = BancoClientes()
    Banco.inserir_cliente()
    csv_row =[Banco.name,Banco.endereco,Banco.idade , Banco.nascimento,Banco.telefone]
    #Banco.deletar_dados()
    Banco.commit_changes()
    Banco.close_connection()
    new_csv.append(csv_row)

write_csv()


