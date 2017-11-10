#!/usr/bin/python
import string, random
import cgitb

cgitb.enable()

def random_generator(size=10485760, chars=string.ascii_uppercase):
 print ''.join(random.choice(chars) for _ in range(size))

random_generator()
