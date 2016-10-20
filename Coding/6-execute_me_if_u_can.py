#!/usr/bin/python
import urllib2, re, os
session_cookie = "" # add your PHPSESSID cookie

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', session_cookie))
req = opener.open("http://ringzer0team.com/challenges/121")

chall_message = re.findall('----- BEGIN SHELLCODE -----<br />\r\n\t\t(.*?)<br />\r\n\t\t----- END SHELLCODE -----', req.read(), re.DOTALL)[0]

# in the chall_message we get a shellcode
# we need to execute the shellcode, retrieve the output and send it back to the server, being this our answer
# to do so, I wrote a C program to execute the shellcode; compiled it -> execute -> save the output and send  
# NOTE: The output text of the shellcode is displayed on stdin (0) stream, so we need to '0>' to store it. 

# creation of c program
shellcode_c_prog = '#include <stdio.h>\n#include <string.h>\nchar *shellcode = "'+ chall_message[:-1] + '";\nint main(void){\n(*(void(*)()) shellcode)();\nreturn 0;\n}'
f = open('shellcode.c','wb') 
f.write(shellcode_c_prog) # write the program to disk
f.close()

# compile -> execute and store the output in answer.txt
os.system("gcc shellcode.c -o shellcode && ./shellcode 0> answer.txt")

f = open('answer.txt','r')
answer = f.readline().strip()
f.close()

print "Shellcode executed: " + answer

resp = opener.open("http://ringzer0team.com/challenges/121/" + answer)
print re.findall('FLAG-\S*', resp.read(), re.DOTALL)[0][:-6]