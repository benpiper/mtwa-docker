#!/usr/bin/python
import string, random
import socket
import time

print '''
Waiting for 15 seconds...
'''

time.sleep(15)

def random_generator(size=5242880, chars=string.printable):
 return ''.join(random.choice(chars) for _ in range(size))

print socket.gethostname()+random_generator()
