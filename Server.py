#My First Server

import socket
#here we mention kind of conn, and ipv4 or 6 - by default its tcp and ipv4
s=socket.socket()

s.bind(('localhost', 9999))

print("Waiting for connection.")

while True:
    # will listen to 3 clients
    s.listen(3)
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print("Client onboard: ", addr, name)
    c.send(bytes("Welcome to Sakshi' server", 'utf-8'))
    c.close()