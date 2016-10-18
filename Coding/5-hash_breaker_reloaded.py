#!/usr/bin/python
import urllib2, hashlib, re, random
session_cookie = "" # add your PHPSESSID cookie

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', session_cookie))
req = opener.open("http://ringzer0team.com/challenges/57")

chall_message = re.findall('----- BEGIN HASH -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END HASH -----<br />\r\n\t\t</div>\r\n\t\t<br />\r\n\t\t<div class="message">\r\n\t\t----- BEGIN SALT -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END SALT -----', req.read(), re.DOTALL)[0]

HASH = chall_message[0]
SALT = chall_message[1]

# the same as hash_breaker exercise, except now we need to append the SALT to the generated hash
while 1:
	new_number = random.randrange(0,10001)
 	number_hash_salted = hashlib.sha1(str(new_number) + SALT).hexdigest()
 	if number_hash_salted == HASH:
 		print number_hash_salted+":"+str(new_number)
 		break

resp = opener.open('http://ringzer0team.com/challenges/57/' + str(new_number))
print re.findall('FLAG-\S*', resp.read(), re.DOTALL)[0][:-6]

