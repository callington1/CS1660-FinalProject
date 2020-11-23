import os
from socket import socket, AF_INET, SOCK_STREAM

HOST = '0.0.0.0'
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, 5151))
s.listen(1) #wait for connection from gui app
conn, addr = s.accept()

print("Connection recieved starting hadoop")
os.system("xterm -hold /spark/bin/spark-shell") #run shell script to start spark