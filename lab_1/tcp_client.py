from socket import *
import sys
s = socket(AF_INET, SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))
message = "GET /"+sys.argv[3]+" HTTP/1.1\r\n"
s.send(message.encode())
print(s.recv(1024).decode())
s.close()
