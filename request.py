import requests
import pprint #Beautify print json

user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:141.0) Gecko/20100101 Firefox/141.0"}

response = requests.get('https://api.github.com', headers = user_agent)

if response.ok:
    response_json: object = response.json()
    pprint.pprint(response_json)

print(response.request.headers)
