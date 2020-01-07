import requests
import json


def get_one_page(url):
    kv = {'user_agent':'Mozilla/5.0'}
    response = requests.get(url, headers=kv)
    if response.status_code == 200:
        return response.text
    return None


def main():
    url = 'http://localhost:3000/tasks/results'
    html = get_one_page(url)

    jsObj1 = json.loads(html)
    jsObj = json.dumps(jsObj1, indent=2)
    with open('pa11y-result.json', 'w') as file:
        file.write(jsObj)
        file.close()


main()
print("yes")
