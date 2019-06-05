import sys
import os
import types
import traceback
import subprocess

f = open("/home/adam/noVNC/PID.txt","r+")

line = f.readlines()
flag = 0
f.seek(0)
for w in line:
	if w !='c'and flag != 0:
        	f.write(w)
	flag +=1
f.truncate()
f.close
f = open("/home/adam/noVNC/PID.txt","r+")
line = f.readlines()
print line
if 'c\n' not in line:
	for x in line:
		try:
			os.kill(int(x),15)
		except:
			print("Error")
	try:
 		f.write('empty')
	except OSError:
 		pass
f.close()
