import random
import threading
import socket

#array of quotes
quotes = ["Life is a flower of which love is the honey. — Victor Hugo",
"Keep calm and carry on. — Winston Churchill",
"Life would be tragic if it weren’t funny. — Stephen Hawking",
"The greatest pleasure of life is love.” — Euripides",
"Life is about making an impact, not making an income. — Kevin Kruse"]

#random quotes from array and send to client
def handle_client(sockfd):
    quoteArray = random.choice(quotes)
    sockfd.sendall(quoteArray.encode())
    sockfd.close()

def main():
    #server ip and port
    host = "192.168.0.152"
    port = 8888

    #create and bind socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))

    #listen for client
    server.listen(5)
    print("Waiting %s:%d for request" % (host, port))

    #start connections and execute handle_client function
    while True:
        client, addr = server.accept()
        print("Accepting client connection from %s" % str(addr))
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

#call main function
main()