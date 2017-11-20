#!/usr/bin/python
import string, random
import socket
import time

print socket.gethostname()

print '''
Waiting for 15 seconds...
'''

time.sleep(15)

def random_generator(size=2621440, chars=string.printable):
 return ''.join(random.choice(chars) for _ in range(size))

print random_generator()
