from socket import *
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

username =#todo 请用base64编码， 
password=#如上

clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect(("smtp.163.com",25))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO SMTP.163.com\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

clientSocket.send("AUTH LOGIN\r\n".encode())
recv2=clientSocket.recv(1024).decode()
print(recv2)

clientSocket.send(username)
recv2=clientSocket.recv(1024)
print(recv2)

clientSocket.send(password)
recv2=clientSocket.recv(1024).decode()
print(recv2)
# Send MAIL FROM command and print server response.
clientSocket.send("MAIL FROM: <13378766179@163.com>\r\n".encode())
recv2=clientSocket.recv(1024).decode()
print(recv2)

# Send RCPT TO command and print server response.
clientSocket.send("RCPT TO: <13378766179@163.com>\r\n".encode())
recv2=clientSocket.recv(1024).decode()
print(recv2)

# Send DATA command and print server response.
clientSocket.send("DATA\r\n".encode())
recv2=clientSocket.recv(1024).decode()
print(recv2)

# Send message data.
clientSocket.send("FROM:han\r\nTo:han\r\nSubject:hello\r\n\r\nHello,world\r\n.\r\n".encode())
recv2=clientSocket.recv(1024).decode()
print(recv2)

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
recv2=clientSocket.recv(1024).decode()
print(recv2)