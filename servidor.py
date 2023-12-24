from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


clientes = []
ip_origem = '192.168.1.67'
porta_conexao = 2731
servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind((ip_origem, porta_conexao))
servidor.listen()

def principal():
    tarefa1 = Thread(target=aceita_conexoes, args=())
    tarefa1.start()
    tarefa2 = Thread(target=envia_comando, args=())
    tarefa2.start()

def aceita_conexoes():
    while True:
        cliente, endereco = servidor.accept()
        clientes.append(cliente)

def envia_comando():
    while True:
        comando = input('Digite um comando: ')
        if comando == 'sair':
            servidor.close()
            break
        for c in range(0, len(clientes) + 1):
            clientes[c].send(bytes(comando, 'utf-8'))

principal()
