import pickle
import random
import socket
import threading

class socketThread(threading.Thread):
    def __init__(self, c, threadID):
        threading.Thread.__init__(self)
        self.c = c
        self.threadID = threadID


    def run(self):
        c.send(str(self.threadID).encode())
        socketList = list(sockets.keys())
        socketData = pickle.dumps(socketList)
        c.send(socketData)

class listeningThread(threading.Thread):
    def __init__(self, c, threadID):
        threading.Thread.__init__(self)
        self.c = c
        self.threadID = threadID

    def run(self):
        c.recv()

messages = []
sockets = {}

s = socket.socket()

s.bind(('localhost', 6000))

s.listen(5)

while True:
    c, addr = s.accept()
    print("Connected from addr")
    threadID = random.randrange(0,100)
    thread = socketThread(c, threadID)
    sockets[threadID] = thread
    thread.start()


