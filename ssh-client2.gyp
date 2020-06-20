import os
import subprocess
import sys 

host = raw_input(" Which host would you like to connect to?")
command = raw_input(" Which command would you like to run on it?")
extra = yes;
while extra == 'yes':
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
