#!/usr/bin/python
import string, random
import cgitb

cgitb.enable()

print '''
'''

def random_generator(size=10248000, chars=string.ascii_uppercase):
 print ''.join(random.choice(chars) for _ in range(size))

random_generator()
