import os
from socket import socket, AF_INET, SOCK_STREAM

HOST = '0.0.0.0'
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, 7070))
s.listen() #wait for connection from gui app
conn, addr = s.accept()

with conn:
    print("Connection recieved starting spyder")
    os.system("xterm spyder") #run spyder