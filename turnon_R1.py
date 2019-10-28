import requests

print("Turning Off Relay#1:")
r = requests.get("http://pitanie:turnonoff@192.168.2.222/relay.cgi?r1=1")
print("Status of Relay#1:")
r = requests.get("http://pitanie:turnonoff@192.168.2.222/relay.cgi?r1")
print(r.text)