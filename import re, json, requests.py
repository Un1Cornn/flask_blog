import re, json, requests 

url = 'https://raw.githubusercontent.com/Un1Cornn/vireonsky/main/test.json'
resp = requests.get(url)
poop = json.loads(resp.text)

print(poop)