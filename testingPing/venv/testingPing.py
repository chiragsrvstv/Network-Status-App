import subprocess
import urllib.request
import string
import ipaddress
import win32api
from colorama import Fore, Back, Style


 #def ping(host):
  #  param ='-n' if platform.system().lower() =='windows' else '-c'
    # command =['ping', param, '1', host]
  #  return subprocess.call(command) == 0



def extract_from_file(path):
    file = open(path)  # replace path with actual directory here
    content = file.read()
    content = str(content)
    final_content = content.split('\n')
    return final_content


def ping_hosts(hosts):
    for i in range(len(hosts)):
        output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(hosts[i])],
                                  stdout=subprocess.PIPE).communicate()[0]
        # Here timeout for ping response is set to a low value of 500ms


        if "Destination host unreachable" in output.decode('utf-8'):
            print(Fore.RED + str(hosts[i]), "is down")
            #win32api.MessageBox(0, str(hosts[i]) + 'is down', 'Alert')
            #print(output)
            #print("------------------------------------------")
        elif "Request timed out" in output.decode('utf-8'):
            print(Fore.RED + str(hosts[i]), "is down")
            #print(output)
            #print("------------------------------------------")
        else:
            print(Fore.GREEN + str(hosts[i]), "is up")
            #win32api.MessageBox(0, str(hosts[i]) + ' is Alive', 'Alert')
            #print(output)
            #print("------------------------------------------")



def ping_ips_from_file(path):
    hosts = list(extract_from_file(path))
    ping_hosts(hosts)


#enter the network address in CIDR format for this func
def ping_network_id(network_id):
    network = ipaddress.ip_network(network_id)
    hosts = list(network.hosts())
    for i in range(len(hosts)):
        ping_hosts(hosts)
        #toping = Popen(['ping', '-n', '3', i], stdout=PIPE)
        #output = toping.communicate()[0]
        #hostalive = toping.returncode
        #print(output)

        #if hostalive == 0:
        #    print(i, "is reachable")
        #else:
        #    print(i, "is not reachable")



#ping_network_id('172.30.144.0/26')
path_to_iplist = r'C:\Users\Chirag\Desktop\list_ip.txt'
#ping_ips_from_file(path_to_iplist)

