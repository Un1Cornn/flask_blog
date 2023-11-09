import re, json, requests 

app = fetch_github_data(__name__)

url = 'https://raw.githubusercontent.com/Un1Cornn/vireonsky/main/test.json'
resp = requests.get(url)
poop = json.loads(resp.text)