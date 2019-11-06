import requests

print("Turning Off Relay#2:")
r = requests.get("http://pitanie:turnonoff@192.168.2.222/relay.cgi?r2=0")
#print("Status of Relay#1:")
#r = requests.get("http://pitanie:turnonoff@192.168.2.222/relay.cgi?r2")
#print(r.text)