#!/usr/bin/python3


"""
Server side: open a TCP/IP socket on a port, listen for a message from
a client, and send an echo reply; this is a simple one-shot listen/reply
conversation per client, but it goes into an infinite loop to listen for
more clients as long as this server script runs; the client may run on
a remote machine, or on same computer if it uses 'localhost' for server
"""

from socket import *

myHost = '' 						#'' = all available interfaces on host
myPort = 50007						# listen on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost,myPort))		# bind it to server port number
sockobj.listen(5) 					# listen, allow 5 pending connects

while True:
		connection, address = sockobj.accept() # wait for next client connect
		print('Server connected by', address)  # connection is a new socket
		while True:
			data = connection.recv(1024) # read next line on client socket
			if not data: break
			connection.send(b'Echo=>' + data)
		connection.close()


