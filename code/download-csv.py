import urllib.request
import os
import json


os.makedirs('./result-csv/', exist_ok=True)

jsonFile = json.loads(open('pa11y-result.json').read())

for i in range(len(jsonFile)):
    task = jsonFile[i]['task']
    iD = jsonFile[i]['id']
    file = task + ".csv"
    print("downloading with " + file)
    localPath = os.path.join('./result-csv',file)
    url = "http://localhost:4000/" + task + "/" + iD + ".csv"
    urllib.request.urlretrieve(url,localPath)
