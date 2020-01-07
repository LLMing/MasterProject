import string

import requests
from lxml import etree
import json


def get_one_page(url):
    kv = {'user_agent':'Mozilla/5.0'}
    response = requests.get(url, headers=kv)
    if response.status_code == 200:
        return response.text
    return None


def main():
    for a in string.ascii_uppercase:
        url = 'https://www.nhs.uk/service-search/GP/Location/Places/' + a + '/4'
        html = get_one_page(url)
        html1 = etree.HTML(html)
        result = html1.xpath('//*[@id="main-content"]/div/div[2]/div[1]/ul/li/a/@href')
        result1 = html1.xpath('//*[@id="main-content"]/div/div[2]/div[1]/ul/li/a')
        fr = open('url.json')
        model = json.load(fr)
        fr.close()
        for i in range(len(result1)):
            model[result1[i].text] = result[i]

        jsObj = json.dumps(model, indent=2)

        with open('url.json', 'w') as file:
            file.write(jsObj)
            file.close()


main()
print("yes")
