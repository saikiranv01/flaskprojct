import requests

url = 'http://localhost:5000/movie?title=logan'
r = requests.get(url)

print(r.json())
