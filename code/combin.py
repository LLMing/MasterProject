
import requests
from lxml import etree
import json


def get_one_page(url):
    kv = {'user_agent':'Mozilla/5.0'}
    response = requests.get(url, headers=kv, proxies={"http": 'http://119.179.181.85:8060'})
    if response.status_code == 200:
        return response.text
    return None


def main():
    file = open('result.json', 'r', encoding='utf-8')
    s = json.load(file)
    file.close()
    url1 = list(s.values())
    for i in url1:
        url = 'https://www.nhs.uk' + i
        print(url)
        html = get_one_page(url)
        html1 = etree.HTML(html)
        result = html1.xpath('//*[@id="aspnetForm"]/div/div[1]/div/div/div/div/div/h1')
        print(result)
        # result1 = html1.xpath('//*[@id="aspnetForm"]/div/div[1]/div/div/div/div/div/p/strong')
        # print(result1)
        result2 = html1.xpath('//*[@id="aspnetForm"]/div/div[1]/div/div/div/div/div/p/span[2]')
        if result:
            key = result[0].text
            # value = result1[0].xpath('string(.)')
            str1 = result2[0].xpath('string(.)')
            str1 = str(str1)
            aaa = str1.rsplit(',',1)
            print(aaa)
            value = aaa[1].replace('\r','').replace('\n','').rstrip().lstrip()
            print(value)
            fr = open('combin.json')
            model = json.load(fr)
            fr.close()
            model[key] = value

            jsObj = json.dumps(model, indent=2)

            with open('combin.json', 'w') as file:
                file.write(jsObj)
                file.close()


main()
print("yes")
