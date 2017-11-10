#!/usr/bin/python

def random_generator(size=104857600, chars=string.digits):
 return ''.join(random.choice(chars) for _ in range(size))

print '''
	<Content-type: text/html\\n\\n>
	<html>
	<head>
	<title>Random Data</title>
	</head>
	<body>
  '''
print random_generator()
