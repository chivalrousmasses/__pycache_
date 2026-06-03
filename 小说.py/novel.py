import requests

headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'}
resp=requests.get('https://top.ihuaben.com/',headers=headers)

from lxml import etree

e=etree.HTML(resp.text)
types=e.xpath('/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr/td[3]/a/text()')
names=e.xpath('/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr/td[1]/a/text()')
authors=e.xpath('/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr/td[4]/a/text()')


for t,name,author in zip(types,names,authors):
    print(f'{t}--{name}--{author}')