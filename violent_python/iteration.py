'''
We might find it easier to use a for-loop to iterate through multiple elements.
Consider, for example: if we wanted to iterate through the entire /24  subnet of IP
addresses for 192.168.1.1 through 192.168.1.254, using a for-loop with the range
from 1 to 255 allows us to print out the entire subnet.
'''
for x in range (1,255):
    print('192.168.1.'+str(x))

'''
Similarly, we may want to iterate through a known list of ports to check
for vulnerabilities . Instead of iterating through a range of numbers, we can iterate 
through an entire list of elements.
'''

portList = [21,22,25,80,110]
for port in portList:
    print(port)

'''
Nesting our two for-loops, we can now print out each IP address and the ports
for each address.
'''

for x in range(1,255):
    for port in portList:
        print('[+] Checking 192.168.1.'+str(x)+':'+str(port))