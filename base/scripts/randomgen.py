#!/usr/bin/python
import string, random
import socket

print '''
'''
print socket.gethostname()

def random_generator(size=15372000, chars=string.printable):
 print ''.join(random.choice(chars) for _ in range(size))

random_generator()
