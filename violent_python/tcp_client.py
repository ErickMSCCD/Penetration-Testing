'''
A TCP client can help us to test for services,
send garbage data, fuzz, or any number of other tasks.
'''

import socket

target_host = 'www.google.com'
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host,target_port))

# Send some data
client.send('GET / HTTP/1.1\R\nHost: google.com\r\n\r\n')

# Recieve some data
response = client.recv(4096)

print(response)