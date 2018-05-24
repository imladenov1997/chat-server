import pickle
import random
import socket
import threading

class socketThread(threading.Thread):
    def __init__(self, clientSocket, threadID):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.threadID = threadID


    def run(self):
        self.clientSocket.send(str(self.threadID).encode())
        socketList = list(sockets.keys())
        socketData = pickle.dumps(socketList)
        self.clientSocket.send(socketData)

class listeningThread(threading.Thread):
    def __init__(self, clientSocket, threadID):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.threadID = threadID

    def run(self):
        while True:
            msg = self.clientSocket.recv(4096)
            self.broadcast(msg, sockets, self.clientSocket)

    def broadcast(self, msg, socket_set, sendingSocket):
        for x in socket_set:
            if socket_set[x] != sendingSocket:
                socket_set[x].send(msg)

messages = []
sockets = {}

s = socket.socket()

s.bind(('localhost', 6000))

s.listen(5)

while True:
    c, addr = s.accept()
    print("User connected")
    threadID = random.randrange(0,100)
    threadSender = socketThread(c, threadID)
    threadListener = listeningThread(c, threadID)
    sockets[threadID] = c
    threadSender.start()
    threadListener.start()


