import requests
import json
from pprint import pprint



# TODO: replace with your own app_id and app_key
app_id = '********'
app_key = '**************************'

language = 'en'
word_id = 'Democracy'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
store_json=json.loads(r.text)
#print(store_json["results"][0]["lexicalEntries"][0]["entries"][0]["senses"])
for s in store_json["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]:
    print(s["definitions"])
    print(s["domains"])
#print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))
