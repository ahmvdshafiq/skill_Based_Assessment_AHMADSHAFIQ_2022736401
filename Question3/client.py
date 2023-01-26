import socket

def main():
    #IP and port of the server
    host = "192.168.0.152"
    port = 8888

    # Create socket
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    sockfd.connect((host, port))

    # Request a quote from server
    quote = sockfd.recv(1024)
    print("Quotes for today is -> %s" % quote.decode('utf-8'))

    # Close socket
    sockfd.close()