from socket import *
host = '192.168.0.152'
port = 7676

#creation of socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#connect to server side
clientSocket.connect((host,port))
temp = input('Input any value in Degree Celsius: ')
clientSocket.send(temp.encode()) #sending to server

#recieved converted input in fahrenheit
tempModified = clientSocket.recv(1024)
print('Your input in fahrenheit is:')
print(tempModified.decode('utf8','strict'))

#close the socket
clientSocket.close()