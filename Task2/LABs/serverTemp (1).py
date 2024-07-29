# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:18:18 2023

@author: s133556
"""

from socket import *
from _thread import *
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
print("server socket created")

#we kept it empty because it's the local host
serverSocket.bind(('',serverPort)) 
print("server socket binded to an address")

#qeue size is 5
serverSocket.listen(5)


#to handle multiple requests is to do threading by defining a function 
def on_new_connection(clientSocket, address):
    num1=clientSocket.recv(2064).decode()
   
   #convert to fehrenhite 
    result = (float(num1)  *(9/5)) +32
    result = str(result)
    clientSocket.send((result.encode()))
    
   
    clientSocket.close()


while True:
   
    clientSocket, address = serverSocket.accept()
    print("new connection")
    
    start_new_thread(on_new_connection, (clientSocket, address))
    