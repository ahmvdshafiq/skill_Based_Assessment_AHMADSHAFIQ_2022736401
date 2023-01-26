from socket import *
host = "192.168.0.152"
port = 7676

#Creation of TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, port))

#socket wait for incoming connection request
serverSocket.listen(1)
print('Waiting for connection: ')
while True:
        connectionSocket,addr = serverSocket.accept() 
        temp = connectionSocket.recv(1024).decode() 

       #converting string to float
        tempCelsius=float(temp) 
        
       #formula for convert celsius to fahrenheit
        tempFahrenheit = (tempCelsius*1.8)+32 
        tempModified=str(tempFahrenheit) 
        connectionSocket.send(tempModified.encode())
        
        #close the socket 
        connectionSocket.close()
