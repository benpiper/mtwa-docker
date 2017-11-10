#!/usr/bin/python
import string, random

def random_generator(size=104857600, chars=string.ascii_uppercase):
 return ''.join(random.choice(chars) for _ in range(size))

print random_generator()
