#!/usr/bin/python
import urllib2, hashlib, re, random
session_cookie = "" # add your PHPSESSID cookie

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', session_cookie))
req = opener.open("http://ringzer0team.com/challenges/56")

chall_message = re.findall('----- BEGIN HASH -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END HASH -----', req.read(), re.DOTALL)[0]

# first step identify the type of hash: https://md5hashing.net/hash_type_checker
# so we get its a sha1 type, now we have to break it
# if we go to some online sha1 breaker like https://hashkiller.co.uk/sha1-decrypter.aspx 
# we find out that the decrypted values are always numbers in a range from 1 to 9999 

# in order to crack an hash all we can do its generate an hash (from the plaintext) and compare we the hash we have from the chall_message

while 1:
	new_number = random.randrange(0,10001)
	number_hash = hashlib.sha1(str(new_number)).hexdigest()
	if number_hash == chall_message:
		print number_hash+":"+str(new_number)
		break

resp = opener.open('http://ringzer0team.com/challenges/56/' + str(new_number))
print re.findall('FLAG-\S*', resp.read(), re.DOTALL)[0][:-6]

