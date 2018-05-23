import pickle
import socket
import threading

name = input('Please, enter your name:\n')

s = socket.socket()
s.connect(('localhost', 6000))

socketID = int(s.recv(4096).decode())
socketIDs = pickle.loads(s.recv(4096))

class sender(threading.Thread):
    def __init__(self, clientSocket, socketID, name):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.socketID = socketID
        self.name = name

    def run(self):
        while True:
            msg = input('')
            self.clientSocket.send((self.socketID))

class listener(threading.Thread):
    def __init(self, clientSocket, socketID):
        threading.Thread.__init__(self)
        self.clientSocket = clientSocket
        self.socketID = socketID

    def run(self):
        while True:
            msg = self.clientSocket.recv(4096)


senderSocket = sender(s, socketID, name)
senderSocket.start()

print(senderSocket)
