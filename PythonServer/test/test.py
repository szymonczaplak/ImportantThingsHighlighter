import requests


r = requests.post("http://127.0.0.1:8000/")
print(r.text)
