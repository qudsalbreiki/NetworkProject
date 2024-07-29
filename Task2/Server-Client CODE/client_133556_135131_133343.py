# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:01:01 2023

@authors 
             Aya Al Balushi - 135131
             Khadija Al Bulushi - 133556
             Quds Al Breiki - 133343   
"""

from socket import *

serverName = "localhost"
portNumber = 45000

#1.create the client socket
clientSocket =socket(AF_INET , SOCK_STREAM) 
#2.connect to the server
clientSocket.connect((serverName, portNumber)) 
#set the flag to true as long as the client want to send more strings
flag = True
#while loop that runs until the flag is set to false when the client do want to send more strings
while flag:
    #3.read a string
    msg = input("enter a string: ")
    
    #4.send the string to the server
    clientSocket.send(msg.encode())
    
    #5.receive the message from the server
    result=clientSocket.recv(2064).decode() 
    
    #6. display the answer on screen 
    print(msg, result) 
    
    print("\n")
    
    #7. ask the user if they want to send another string
    msg2 = input("do you want to send another string? (y/n)? ")
    
    #8. convert the answer to lower case letter 
    msg2 = msg2.lower()
    #9.if statement to check whether the user entered yes or no
    if msg2 == "y":
        # send the answer to the server
        clientSocket.send(msg2.encode())
        
    else:
        #set flag to false to stop the loop
        flag = False
#10. close the socket     
clientSocket.close() 
             