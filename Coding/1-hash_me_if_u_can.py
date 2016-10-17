#!/usr/bin/python
import urllib2, hashlib, re
session_cookie = "" # add your PHPSESSID cookie

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', session_cookie))
req = opener.open("http://ringzer0team.com/challenges/13")

# get the message to be hashed
chall_message = re.findall('----- BEGIN MESSAGE -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END MESSAGE -----', req.read(), re.DOTALL)[0]

# hash the message
hashed_message = hashlib.sha512(chall_message).hexdigest()

# send the response to the server
resp = opener.open('http://ringzer0team.com/challenges/13/' + hashed_message)

# get your flag
print re.findall('FLAG-\S*', resp.read(), re.DOTALL)[0][:-6]
