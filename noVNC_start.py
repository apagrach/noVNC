import sys
import os
import types
import traceback
import subprocess
import getopt


#Preapender is used to write a 'c' to the start of the log file for each device
#this is used to prevent shutting down the server while another user still has a window open
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


#Command line args are used to specify the device
#-h takes the ip address and VNC server port ex. 197.168.0.10:5900
#-p takes the websocket port for the VNC server ex. 6080. each port number must be diffrent for each instance of noVNC
opts, args = getopt.getopt(sys.argv[1:],"h:p:")
for opt, arg in opts:
	if opt in ("-h"):
		hmi= arg
	elif opt in ("-p"):
		port=arg

#A new file path for the log file is created based on the ips
path = "/home/adam/noVNC/"+hmi.strip("\n")+"_PID.txt"

# Popen si used to start the server. The PID of the server is writen to the log file
cmd=['exec /home/adam/noVNC/utils/launch.sh --vnc ' + hmi + " --listen "+port]
proc = subprocess.Popen(cmd,shell=True,preexec_fn=os.setsid)
f = open(path, "a+")
f.write(str(proc.pid) + '\n')
f.close()
print proc.pid


line_prepender(path,"c")
