# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:15:43 2023

@author: s133556
"""

from socket import *



serverName = 'localhost' 
portNumber = 12000

clientSocket =socket(AF_INET , SOCK_STREAM) 

clientSocket.connect((serverName, portNumber)) 

temp = input("enter a tempreture in celilus: ")

clientSocket.send(temp.encode())

result=clientSocket.recv(2064).decode() 
print(result)

clientSocket.close()                                                       