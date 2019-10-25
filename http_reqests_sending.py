import requests

#payload = {"First Name": "John", "Last Name": "Smith"}

# http://192.168.0.100/relay.cgi?rN
# request state relay #N

#r = requests.get("https://192.168.2.222/relay.cgi?r2", params=payload)

# Current status of relay
r = requests.get("http://pitanie:turnonoff@192.168.2.222/relay.cgi?r1")

# Turn OFF relay #N
#r = requests.get("http://pitanie:turnonoff@192.168.2.222/relay.cgi?r1=0")

# Turn ON relay #N
#r = requests.get("http://pitanie:turnonoff@192.168.2.222/relay.cgi?r1=1")

print(r.url)
print("HTTP Status Code:", r.status_code)
print("Content:", r.content)
print(r.text)