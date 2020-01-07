import urllib.request
import os
import json


os.makedirs('./result-json/', exist_ok=True)

jsonFile = json.loads(open('pa11y-result.json').read())

for i in range(len(jsonFile)):
    task = jsonFile[i]['task']
    iD = jsonFile[i]['id']
    file = task + ".json"
    print("downloading with " + file)
    localPath = os.path.join('./result-json',file)
    url = "http://localhost:4000/" + task + "/" + iD + ".json"
    urllib.request.urlretrieve(url,localPath)
