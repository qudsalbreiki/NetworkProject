# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 16:00:55 2023

@author: s133556
"""

from socket import *

serverPort = 55000
#create the server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
print("server socket created")

#bind the socket to an address
serverSocket.bind(('',serverPort)) #bind takes one argumant so we double the brackets to pass two
print("server socket binded to an address")
#listen for the client request the main socket
serverSocket.listen(5)#max queue size

#communication starts

#this will run forever i'll keep accepting connection requests 
while True:
    #accept incoming connections
    clientSocket, address = serverSocket.accept()
    print("new connection")
    
    #recieve the messaage 
    num1=clientSocket.recv(2064).decode()
    num2=clientSocket.recv(2064).decode()
   
    result = int(num1) + int(num2)
    result = str(result)
    clientSocket.send((result.encode()))
    
    #close client socket
    clientSocket.close()
