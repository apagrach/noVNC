import sys
import os
import types
import traceback
import subprocess
import getopt

#Command line args are used to specify the device
#-h takes the ip address and VNC server port ex. 197.168.0.10:5900
#-p takes the websocket port for the VNC server ex. 6080. each port number must be diffrent for each instance of noVNC
opts, args = getopt.getopt(sys.argv[1:],"h:p:")
for opt, arg in opts:
	if opt in ("-h"):
		hmi= arg
	elif opt in ("-p"):
		port=arg

#The log file name and location is based on the Device IP and port		
path = "/home/adam/noVNC/"+hmi.strip("\n")+"_PID.txt"
f = open(path,"r+")


#In the log file the number of lines with 'c' specifieys the number of current users
#of that server. When a user closes thier session one 'c' is removed from the file
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

#If all users are done with the server then the server will be shut down by killing the proccess
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
