import math
import requests
from requests import urllib3
from lxml import etree
import json
from multiprocessing import Pool


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


def get_one_page(url):
    retry_count = 5
    proxy = get_proxy()
    kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    while retry_count > 0:
        try:
            response = requests.get(url, headers=kv, proxies={"http": "http://{}".format(proxy)}, verify=False)
            if response.status_code == 200:
                return response
        except Exception:
            retry_count -= 1
    delete_proxy(proxy)
    return None


def scrape(url):
    print("start collect URL")
    url2 = 'https://www.nhs.uk' + url
    content = get_one_page(url2)
    if content is not None:
        html = content.text
        htmlURL = content.url
        html2 = etree.HTML(html)
        stringTotal = html2.xpath('//*[@id="main-content"]/div/form[2]/div[1]/ul/li[1]')
        tempString = stringTotal[0].text.split()
        totalResult = tempString[-2]
        pageNumber = int(math.ceil(int(totalResult) / 10))
        lastpage = int(totalResult) % 10
        fr = open('result.json')
        dict = json.load(fr)
        fr.close()
        for a in range(1, pageNumber + 1):
            url3 = htmlURL + '&ResultsOnPageValue=10&isNational=0&totalItems=' + str(
                totalResult) + '&currentPage=' + str(a)
            content1 = get_one_page(url3)
            if content1 is not None:
                html3 = content1.text
                html4 = etree.HTML(html3)
                b = 22
                if a == pageNumber:
                    b = 2 + (2 * lastpage)
                for ii in range(4, b + 2, 2):
                    name1 = html4.xpath('//*[@id="main-content"]/div/form[2]/table/tbody/tr[' + str(ii) + ']/th/a')
                    result = html4.xpath(
                        '//*[@id="main-content"]/div/form[2]/table/tbody/tr[' + str(ii) + ']/th/a/@href')
                    key = name1[0].text
                    value = result[0]
                    dict[key] = value
            else:
                with open('error.txt', 'a')as file:
                    aa = url2 + ':' + url3
                    file.write(aa)
                    continue
        print("collect finished, start to write")
        jsObj = json.dumps(dict, indent=2)
        with open('result.json', 'w')as file:
            file.write(jsObj)
            file.close()
    else:
        with open('error1.txt', 'a')as file1:
            aaa = url2
            file1.write(aaa)
            file1.close()


if __name__ == '__main__':
    file = open('url.json', 'r', encoding='utf-8')
    s = json.load(file)
    file.close()
    url = s.values()
    pool = Pool()   
    pool.map(scrape, url)
