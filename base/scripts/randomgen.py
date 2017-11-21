#!/usr/bin/python
import string, random
import socket
import time

print '''
Random data generator
'''

def random_generator(size=1572864, chars=string.printable):
 return ''.join(random.choice(chars) for _ in range(size))

print socket.gethostname() + '  ' + random_generator()
