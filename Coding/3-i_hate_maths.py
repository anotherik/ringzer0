#!/usr/bin/python
import urllib2, hashlib, re
session_cookie = "" # add your PHPSESSID cookie

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', session_cookie))
req = opener.open("http://ringzer0team.com/challenges/32")

chall_message = re.findall('----- BEGIN MESSAGE -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END MESSAGE -----', req.read(), re.DOTALL)[0]

# we get: decimal + hex - binary
string_list = chall_message.encode('ascii').split()[0:7]

# we convert it to decimal and make it all int to perform the operations
result = int(string_list[0]) + int(string_list[2], 0) - int(string_list[4],2)

resp = opener.open('http://ringzer0team.com/challenges/32/' + str(result))
print re.findall('FLAG-\S*', resp.read(), re.DOTALL)[0][:-6]

