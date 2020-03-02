#-*- coding: utf-8 -*-

import socket
import sys

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    host = input("INFORME O IP COM O QUAL DESEJA SE COMUNICAR: ")
    tcp_client.connect((host, 5555))
    while(True):
        msg = input("Informe uma mensagem p/ enviar ao servidor: ")
        tcp_client.send(msg.encode('utf-8'))
        data = tcp_client.recv(1024)
        if (len(str(data)) >= 0):
            print("RECEBIDO DO : " + data.decode('utf-8'))
        else:
            print("NENHUM DADO RECEBIDO....");
except ValueError:
	print("Erro na conexão!")
