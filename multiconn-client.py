import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 5200

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print("1. Read from other users\n2. Broadcast your message\n")
while True:
    Input = input('input: ')
    if (Input.lower().strip() == "bye"):
        break
    if (Input == "1"):
        Response = ClientSocket.recv(1024)
        print(Response.decode("utf-8"))
    elif (Input == "2"):
        msg = input("Type your message: ")
        ClientSocket.send(str.encode(msg))

ClientSocket.close()
