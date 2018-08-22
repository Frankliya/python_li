import requests
from lxml import etree
import json

def get_data(num):
    url = 'https://www.kuaidaili.com/free/inha/'+str(num)
    response = requests.get(url)
    text = response.text
    return text


def handle_data(html):
    html = etree.HTML(html)
    items = []
    code = html.xpath('//div[@id="list"]/table/tbody/tr/td[1]/text()')
    post_id = html.xpath('//div[@id="list"]/table/tbody/tr/td[2]/text()')
    ip_type = html.xpath('//div[@id="list"]/table/tbody/tr/td[4]/text()')
    print(code)
    print(type(code))


    return items

#保存数据
# def save(items):
# 	f = open("qiushi.txt","w")
# 	json.dump(items,f,ensure_ascii=False)

def main():
    text = get_data(1)
    items = handle_data(text)
    print(items)

if __name__ == '__main__':
    main()