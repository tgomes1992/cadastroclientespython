import csv
import os
#mapa
#Cadastra
#Gera CSV
#Importa para um banco de Dados

new_csv = []

class Clientes():
    def __init__(self):
         self.name = str(input("Digite o nome do cliente: "))
         self.endereco = str(input("Digite o endereço do referido cliente: "))
         self.idade = int(input("Digite a idade do cliente: "))
         self.nascimento = input("Digite a data de nascimento: ")
         self.telefone = input("Digite a data de nascimento: ")
         print("Cliente "+ self.name + "cadastrado com sucesso: ")

#criar objeto csv e checar interdependências

# criar um log dos cadastros que serão importados para o banco de dados.

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
    csv_header = ["Nome","Endereço", "Idade","Nascimento" ,"Telefone"]
    csv_file = open("Clientes Cadastrados.csv","w",newline="")
    writer = csv.writer(csv_file,delimiter=";")
    writer.writerow(csv_header)
    writer.writerows(new_csv)
    print (new_csv)

while desejodecadastro():
        cliente = Clientes()
        csv_row =[cliente.name,cliente.endereco,cliente.idade , cliente.nascimento,cliente.telefone]
        new_csv.append(csv_row)

write_csv()



