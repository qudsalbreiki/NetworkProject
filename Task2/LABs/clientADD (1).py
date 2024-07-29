# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 15:48:51 2023

@author: s133556
"""

from socket import *
#if i use (import socket) each time i need to use a function i need to say socket.Thefunction
#server name is the local host because both are running on the same machines 

#severName = "localhost'
serverName = '172.23.11.51' #ip of the device
portNumber = 55000

#1.create the client socket

clientSocket =socket(AF_INET , SOCK_STREAM) #AF_INET is type of addresses and SOCK_STREAM is 
                                              #type of the message(stream datagram etc)

#2.connect to the server
clientSocket.connect((serverName, portNumber)) #give it IP and port Number

 #read numbers
msg1 = input("enter an integer value: ")
msg2 = input("enter another integer value: ")

#sendthe numbers
clientSocket.send(msg1.encode())
clientSocket.send(msg2.encode())

#3.receive the message from the server
#if we dont add decode we will receive the message in byte format 
result=clientSocket.recv(2064).decode() #we need to store the message that we will receive and specify the size
                              #data type is byte, convert to string by decoding
print(msg1 , '+' , msg2 , '=' , result)

clientSocket.close()                                                       