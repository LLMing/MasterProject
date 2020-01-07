import requests
import json
import time


def get_one_page(url):
    kv = {'user_agent':'Mozilla/5.0'}
    response = requests.get(url, headers=kv)
    if response.status_code == 200:
        return response.text
    return None


def main():
    i = 0
    fr = open('pa11y-id.json')
    model = json.load(fr)
    fr.close()
    for aa in range(len(model)):
        model_str = model[aa]
        for key, value in model_str.items():
            if key == 'id':
                a = value
                url = 'http://localhost:4000/'+ a + '/run'
                html = get_one_page(url)
                i += 1
                print(i)
                print('yes')
                time.sleep(2)

main()
print('finished')