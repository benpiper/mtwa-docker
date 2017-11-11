#!/usr/bin/python
import string, random
import cgitb

cgitb.enable()

print '''
'''

def random_generator(size=20496000, chars=string.printable):
 print ''.join(random.choice(chars) for _ in range(size))

random_generator()
