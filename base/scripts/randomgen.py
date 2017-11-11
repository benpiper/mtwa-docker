#!/usr/bin/python
import string, random
import socket

print '''
'''

def random_generator(size=15334400, chars=string.printable):
 print ''.join(random.choice(chars) for _ in range(size))

print socket.gethostname()+random_generator()
