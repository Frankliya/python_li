import requests
import hashlib

from lxml import etree
import json


url = 'https://www.kuaidaili.com/free/inha/1'
response = requests.get(url)
# c = hashlib.md5(response)
text = response.text
print(text)
# print(c)

