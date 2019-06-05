import sys
import os
import types
import traceback
import subprocess
import getopt

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)



opts, args = getopt.getopt(sys.argv[1:],"h:p:")
for opt, arg in opts:
	if opt in ("-h"):
		hmi= arg
	elif opt in ("-p"):
		port=arg

path = "/home/adam/noVNC/"+hmi.strip("\n")+"_PID.txt"

cmd=['exec /home/adam/noVNC/utils/launch.sh --vnc ' + hmi + " --listen "+port]
proc = subprocess.Popen(cmd,shell=True,preexec_fn=os.setsid)
f = open(path, "a+")
f.write(hmi.strip("\n") +" "+str(proc.pid) + '\n')
f.close()
print proc.pid


line_prepender(path,"c")
