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
        self.name = str(input("Digite o nome do cliente: "))
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
        self.curs.execute('''DELETE FROM clientes WHERE Telefone="24035621" ''')
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
    # csv_header = ["Nome","Endereço", "Idade","Nascimento" ,"Telefone"]
    csv_file = open("Clientes Cadastrados.csv","w",newline="")
    writer = csv.writer(csv_file,delimiter=";")
    # writer.writerow(csv_header)
    writer.writerows(new_csv)
    print (new_csv)


while desejodecadastro():
    Banco = BancoClientes()
    Banco.inserir_cliente()
    #Banco.deletar_dados()
    Banco.commit_changes()
    Banco.close_connection()
    #csv_row =[cliente.name,cliente.endereco,cliente.idade , cliente.nascimento,cliente.telefone]




#new_csv.append(csv_row)

#write_csv()



