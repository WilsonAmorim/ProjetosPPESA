# -*- coding: utf8 -*-

import socket

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 8000
#criando o objetro socker
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conectar no servidor
socket_cliente.connect((SERVER_ADDRESS, SERVER_PORT))

socket_cliente.sendall(b'ping')
dado = socket_cliente.recv(1024)
dado = dado.decode()

print(f'recebido do servidor: {dado}')



# debug
print(f'conexão estabelecida com sucesso')

# finalizer conexão
socket_cliente.close()
