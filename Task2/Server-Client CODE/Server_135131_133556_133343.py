# -*- coding: utf-8 -*-

"""
@authors:
             Aya Al Balushi - 135131
             Khadija Al Bulushi - 133556
             Quds Al Breiki - 133343   
"""

from socket import *
from _thread import *

# isPalindrome function: check if a string is a palindrome
# @Parameters: string
# @Returns: True if the string is a palindrome and False otherwise
def isPalindrome(string): 
    strInReverse = "" 
    # loop throug the string starting from the last index
    for i in range(len(string)-1,-1,-1):
        strInReverse = strInReverse + string[i]
    # chech if the string equals its reverse 
    return string == strInReverse


# on_new_client function: handles client communication
# @Parameters: clientSocket, address
def on_new_client(clientSocket, address):
    
    flag = True
    # LOOP while the client wants to send another string for checking
    while flag:
        # the server recieves a string from the client
        string = clientSocket.recv(1000).decode()
        # call the function isPalindrome
        palindrome = isPalindrome(string)
        
        if palindrome:
            result = "======> is a palindrome"
        else:
            result = "======> is not a palindrome"
        
        # Send the result to the client
        clientSocket.send(result.encode()) 
       
        # check if the client wants to check another string or not 
        newString = clientSocket.recv(1000).decode()
        # if the client sends y then loop again 
        if newString == "y":
            flag = True
            
        else:
            # else exit the while loop
            flag = False
            
    # Close the connection to that client
    clientSocket.close() 


serverPort = 45000

# Create server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to a specific name and port
serverSocket.bind(('',serverPort))

# 7 denotes maximum number of connections for this socket
serverSocket.listen(7)


while True:
    
    # Accept an incoming connection request
    clientSocket, address = serverSocket.accept()
    
    # Call function start_new_thread
    start_new_thread(on_new_client, (clientSocket,address))