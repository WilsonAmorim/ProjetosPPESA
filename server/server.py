# -*- coding: utf8 -*-

import socket

SERVER_ADDRESS = '0.0.0.0'
SERVER_PORT = 8000
#criando o objetro socker
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# solicitar ao windows para ouvir na porta 8000
socket_servidor.bind((SERVER_ADDRESS, SERVER_PORT))
socket_servidor.listen()


# aguardar um conexão cliente
# debug
print(f'Servidor ouvindo em {SERVER_ADDRESS} : {SERVER_PORT} pronto para receber conexôes...')
socket_cliente, cliente_addr = socket_servidor.accept()
#receber dados cliente
dado_recebido = socket_cliente.recv(1024)
dado_recebido = dado_recebido.decode()

# resposta ao browser
resposta = f'HTTP/1.1 200 OK\r\n\r\nHello, World'

# responder para o cliente
socket_cliente.sendall(resposta.encode('utf-8'))


# encerrar a conexão
#socket_cliente .close()