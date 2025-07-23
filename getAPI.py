import requests
URL ="http://localhost:8000/items2/555"
res= requests.get(URL)

print('status :', res.status_code)