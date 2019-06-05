import sys
import os
import types
import traceback
import subprocess

opts, args = getopt.getopt(sys.argv[1:],"h:p:")
for opt, arg in opts:
	if opt in ("-h"):
		hmi= arg
	elif opt in ("-p"):
		port=arg
path = "/home/adam/noVNC/"+hmi.strip("\n")+"_PID.txt"
f = open(path,"r+")

line = f.readlines()
flag = 0
f.seek(0)
for w in line:
	if flag != 0:
        	f.write(w)
		print(w)
	flag +=1
f.truncate()
f.close
f = open(path,"r+")
line = f.readlines()
print line
if 'c\n' not in line:
	for x in line:
		try:
			os.kill(int(x),15)
		except:
			print("Error")
	f.close()	
	os.remove(path)
try:
	f.close()
except:
	pass
