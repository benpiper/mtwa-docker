#!/usr/bin/python
import os
import cgi
import appsitefunctions
import Cookie
import string, random, socket

# Turn on debug mode.
import cgitb
cgitb.enable()

def id_generator(size=6, chars=string.ascii_uppercase):
 return ''.join(random.choice(chars) for _ in range(size))

if 'HTTP_COOKIE' in os.environ:
 cookies = os.environ['HTTP_COOKIE']
 c = Cookie.SimpleCookie()
 c.load(cookies)
 print c.output()
else:
#Set cookie
 appsessionidvalue = socket.gethostname()+id_generator()
 c = Cookie.SimpleCookie()
 c["appSessionID"] = appsessionidvalue
# c["appSessionID"]['expires'] = 900
 print c.output()

#This will figure out what module to call based on the URL passed.  /index.py?module=viewdb for example
form = cgi.FieldStorage()
modulename = form.getvalue('module')
# print form, "<!-- (DEBUG) -->"

#This will call the fucntion to loab the base.html file for the site.  None is used because those variable for the printsite function are not used in the general page, they are used elsewhere.
appsitefunctions.printsite(modulename,None,None,None)
