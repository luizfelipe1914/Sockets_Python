#!/usr/bin/env python3

#-*- coding: utf-8 -*-

import socket

def start_server(host, port):
    sock = (host, port)
    server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_tcp.bind(sock)
    server_tcp.listen(5)
    print("AGUARDANDO CONEXÕES NA PORTA TCP 5555...")
    while (True):
        try:
            (con, address) = server_tcp.accept()
            print("O HOST: " + str(address[0]) + " ESTÁ CONECTADO")
            while(True):
                inp = con.recv(1024)
                if(len(str(inp)) != 0 or inp is None):
                    print(address[0] +  " ENVIOU-LHE: " + inp.decode("utf-8"))
                    out = input("SUA RESPOSTA: ")
                    con.send(out.encode("utf-8"))
                else:
                    print("NENHUM DADO RECEBIDO DE" + address[0])

        
        except ValueError:
             print("ERRO: Accept")
           


def main():
    print("O IP DEFAULT DE ABERTURA DO SOCKET É O 127.0.0.1 E A PORTA TCP DEFAULT É A 5555....")
    start_server('', 5555)
    

if __name__ == '__main__':
    main()

    


