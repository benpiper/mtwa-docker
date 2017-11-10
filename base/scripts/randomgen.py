#!/usr/bin/python
import string, random

def random_generator(size=10485760, chars=string.ascii_uppercase):
 print ''.join(random.choice(chars) for _ in range(size))
