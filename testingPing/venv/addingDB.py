#!/usr/bin/env python3
import psycopg2
import subprocess
import string
import ipaddress
from colorama import Fore, Back, Style
import time

#establishing connection with database
conn = psycopg2.connect("dbname = hostinfo user=postgres password=1234")
cursor = conn.cursor()

# a function which takes list of hosts as argument and pings them
def ping_hosts(hosts):
    for i in range(len(hosts)):
        output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(hosts[i])],
                                  stdout=subprocess.PIPE).communicate()[0]
        # Here timeout for ping response is set to a low value of 500ms
        if "Destination host unreachable" in output.decode('utf-8'):
            # committing changes to the status on database
            update_status_error(i)
            print(Fore.RED + str(hosts[i]), "is down")
            print(cursor.fetchall())
            print("-------------------------------")
        elif "Request timed out" in output.decode('utf-8'):
            # committing changes to the status on database
            update_status_error(i)
            print(Fore.RED + str(hosts[i]), "is down")
            print(cursor.fetchall())
            print("-------------------------------")

        elif "Ping request could not find host" in output.decode('utf-8'):
            update_status_error(i)
            print(Fore.RED + str(hosts[i]), "is down")
            print(cursor.fetchall())
            print("-------------------------------")

        else:
            # committing changes to the status on database
            update_status_success(i)
            print(Fore.GREEN + str(hosts[i]), "is up")
            print((cursor.fetchall()))
            print("-------------------------------")

def update_status_error(host_ip):
    cursor.execute("update details set status='Failed' where details.ip_address=(%s);", [str(hosts[host_ip])])
    # to display results on console
    cursor.execute("select name from details where ip_address=(%s);", [str(hosts[host_ip])])

def update_status_success(host_ip):
    cursor.execute("update details set status='Success' where details.ip_address=(%s);", [str(hosts[host_ip])])
    # to display results on console
    cursor.execute("select name from details where ip_address=(%s);", [str(hosts[host_ip])])

def ping_hosts_every(seconds):
    c = 1
    while(c>0):
        time.sleep(seconds)
        ping_hosts(hosts)
        conn.commit()



query_to_fetch_ips = """select ip_address from details"""
cursor.execute(query_to_fetch_ips)
result = cursor.fetchall()

# creating a list of hosts fetched from database
hosts = list((sum(result, ())))

ping_hosts_every(2)
conn.close()