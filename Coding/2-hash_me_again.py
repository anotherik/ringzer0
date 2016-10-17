#!/usr/bin/python
import urllib2, hashlib, re, binascii
session_cookie = "" # add your PHPSESSID cookie

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', session_cookie))
req = opener.open("https://ringzer0team.com/challenges/14")

chall_message = re.findall('----- BEGIN MESSAGE -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END MESSAGE -----', req.read(), re.DOTALL)[0]

# the chall_message we get is a binary message
# so we need to convert it to ascii before applying the hash

# first we convert it to decimal
n = int(chall_message, 2)
# and then we convert to hex and finally unhexlify to get the ascii
ascii_message = binascii.unhexlify('%x' % n)

# now we can hash the ascii_message
hashed_message = hashlib.sha512(ascii_message).hexdigest()

# send the response
resp = opener.open('https://ringzer0team.com/challenges/14/' + hashed_message)
# and get our flag
print re.findall('FLAG-\S*', resp.read(), re.DOTALL)[0][:-6]
