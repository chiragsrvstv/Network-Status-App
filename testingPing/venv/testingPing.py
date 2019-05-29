import platform
import subprocess
import urllib.request
import string
from flask import Flask, render_template, redirect, url_for,request
from flask import make_response

def ping(host):
    param ='-n' if platform.system().lower() =='windows' else '-c'
    command =['ping', param, '1', host]
    return subprocess.call(command) == 0



def ping_from_list(path):
    file = open(path)  # replace path with actual directory here
    content = file.read()
    content = str(content)
    final_content = content.split('\n')

    for ips in final_content:
        ping(ips)

        if(ping(ips) == False):
            print("Failed" + " " + ips)
        else:
            print("Connected" + " " + ips)


path_to_iplist = r'C:\Users\Chirag\Desktop\list_ip.txt'
ping_from_list(path_to_iplist)
#ping("https://www.google.com/"

app = Flask(__name__)

@app.route("/")
def home():
    return "hi"
@app.route("/index")

@app.route('/login', methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run(debug = True)



