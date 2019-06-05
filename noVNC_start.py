import sys
import os
import types
import traceback
import subprocess

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


d  = open("/home/adam/noVNC/device.txt","r+")
dev = d.readlines()

for  ip in dev:

	cmd=['exec /home/adam/noVNC/utils/launch.sh --vnc ' + ip]
	proc = subprocess.Popen(cmd,shell=True,preexec_fn=os.setsid)
	f = open("/home/adam/noVNC/PID.txt", "a+")
	f.write(str(proc.pid) + '\n')
	f.close()
	print proc.pid

line_prepender("/home/adam/noVNC/PID.txt","c")
