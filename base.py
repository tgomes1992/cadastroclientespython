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
         print("Cliente: "+ self.name)


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
    csv_header = ["Nome","Endereço", "Idade"]
    csv_file = open("Clientes Cadastrados.csv","w",newline="")
    writer = csv.writer(csv_file,delimiter=";")
    writer.writerow(csv_header)
    writer.writerows(new_csv)
    print (new_csv)


while desejodecadastro():
        cliente = Clientes()
        csv_row =[cliente.name,cliente.endereco,cliente.idade]
        new_csv.append(csv_row)

write_csv()



