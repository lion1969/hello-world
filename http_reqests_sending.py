import requests


payload = {"First Name": "John", "Last Name": "Smith"}

r = requests.get("https://httpbin.org/get", payload=payload)
print(r.url)
