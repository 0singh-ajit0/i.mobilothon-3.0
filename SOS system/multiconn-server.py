import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 5200
ThreadCount = 0
try:
		ServerSocket.bind((host, port))
except socket.error as e:
		print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)

list_of_conn_addrs = []
list_already_send = []
new_message_arrived: bool = False
new_message: str = ""

conn_objects = []


def threaded_client(connection, addr):
		connection.send(str.encode('Welcome to the Server'))
		while True:
				data = connection.recv(2048)
				# reply = 'Server Says: ' + data.decode('utf-8')
				if not data:
						break
				for i in range(ThreadCount):
					if conn_objects[i] != connection:
						conn_objects[i].sendall(data)
				print("Message from " + str(addr) + ": " + data.decode("utf-8"))
		connection.close()

while True:
		Client, address = ServerSocket.accept()
		print('Connected to: ' + address[0] + ':' + str(address[1]))
		conn_objects.append(Client)
		start_new_thread(threaded_client, (Client, address))
		ThreadCount += 1
		print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
