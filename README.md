# chat-server
Simple Python Chat Application

This application uses Client-Server architecture where messages are sent via TCP Sockets. One server holds one chatroom which means
that messages are broadcast among all clients (members) of this server (chatroom).

The Client-Server architecture is implemented in the following way: 

- Server listens for connections from clients and broadcasts all received messages from clients. Sender of the message, however, 
does not receive the message it has sent

- Client connects to a server and starts sending and receiving messages

The idea is that both client and server use two threads - one for receiving and one for sending messages. 
