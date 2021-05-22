'''
A TCP client can help us to test for services,
send garbage data, fuzz, or any number of other tasks.
'''

import socket

target_host = '0.0.0.0'
target_port = 9998

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host,target_port))

# Send some data
client.send(b'Hello World')

# Recieve some data
response = client.recv(4096)

print(response.decode())
client.close()