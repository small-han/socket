#import socket module 
from socket import *
import sys # In order to terminate the program
import threading
import time

serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket
serverSocket.bind(('127.0.0.1',6789))
serverSocket.listen(10)

def tcp(connectionSocket,addr):
    try:
        message =connectionSocket.recv(1024).decode() 
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =f.read()
        #Send one HTTP header line into socket
        connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')

        #Send the content of the requested file to the client

        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.send(b'HTTP/1.1 404 Not Found')
        #Close client socket
        connectionSocket.close()

while True:
    #Establish the connection 
    print('Ready to serve...')
    connectionSocket, addr =serverSocket.accept() 
    t=threading.Thread(target=tcp,args=(connectionSocket,addr))
    t.start()

serverSocket.close()

sys.exit()#Terminate the program after sending the corresponding data

