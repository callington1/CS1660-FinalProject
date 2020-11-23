import os
from socket import socket, AF_INET, SOCK_STREAM

HOST = '0.0.0.0'
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, 9191))
s.listen() #wait for connection from gui app
conn, addr = s.accept()

with conn:
    print("Connection recieved starting git")
    os.system("xterm bash") #run git bash