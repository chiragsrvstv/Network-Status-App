import ctypes, sys
import platform
from subprocess import Popen, PIPE
import urllib.request
import pythonping
import string
import os
import sys
import ipaddress


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    def efficient_ping(network_id):
        network = ipaddress.ip_network(network_id)
        for i in network.hosts():
            i = str(i)
            toping = Popen(['ping', '-n', '3', i], stdout=PIPE)
            output = toping.communicate()[0]
            hostalive = toping.returncode
            print(output)

            if hostalive == 0:
                print(i, "is reachable")
            else:
                print(i, "is not reachable")


    # efficient_ping('172.25.144.0/26')
    toping = Popen(['ping', '-c', '3', '172.30.144.26'], stdout=PIPE)
    output = toping.communicate()[0]
    print(output)
    # Code of your program here

else:

    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)