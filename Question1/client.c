//C library for socket, file descriptor,
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

// error handling function
void error(const char *msg) {
    perror(msg);
    exit(1);
}

int main() {
    int sock_fd;
    struct sockaddr_in server_address;
    char buffer[256];
    int x;

    // create socket
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd < 0)
        error("Unable to create socket");

    // set up server address for ip address and port
    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = inet_addr("192.168.0.152");
    server_address.sin_port = htons(8888);

    // connecting to the server
    if (connect(sock_fd, (struct sockaddr *) &server_address, sizeof(server_add>
        error("Error connecting");

    
// clear the buffer
    bzero(buffer, sizeof(buffer));

    // reading the random number from server side
    x = read(sock_fd, buffer, sizeof(buffer)-1);
    if (x < 0)
	error("Unable to read the socket");

    // print the random number
    printf("The Random number from server is: %s\n", buffer);

    // close the socket
    close(sock_fd);
    return 0;
}
