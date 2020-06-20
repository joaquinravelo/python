import os
import subprocess
import sys 

host = input("Hostname")
command = input("Command?")

ssh = subprocess.Popen(["ssh", "%s" % host, command],
                    shell=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print(sys.stderr, "Error: %s" % error)
else:
    print (result)
