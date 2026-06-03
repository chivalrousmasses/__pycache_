
#%%
import requests
from lxml import etree

urls=['https://movie.douban.com/top250?start={}&filter='.format(str(i*25)) for i in range(10)]
datas=[]

for url in urls:
    headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'}
    resp=requests.get(url=url,headers=headers)
    e=etree.HTML(resp.text)
    lis=e.xpath('//*[@id="content"]/div/div[1]/ol/li')
    def get_first_text(list):
        return list[0].strip()
    for li in lis:
       title=get_first_text(li.xpath('./div/div[2]/div[1]/a/span[1]/text()'))
       detail=get_first_text(li.xpath('./div/div[2]/div[1]/a/@href'))
       aa=get_first_text(li.xpath('./div/div[2]/div[2]/p[1]/text()[1]'))
       datatype=get_first_text(li.xpath('./div/div[2]/div[2]/p[1]/text()[2]'))
       ratingnum=get_first_text(li.xpath('./div/div[2]/div[2]/div/span[2]/text()'))
       allpeople=get_first_text(li.xpath('./div/div[2]/div[2]/div/span[4]/text()'))
       datas.append([title,detail,aa,datatype,ratingnum,allpeople[:-3]])
#%%
import pandas as pd
pf=pd.DataFrame(datas,columns=['电影名','详情','导演、主演','时间、类型','评分','评分人数'])
pf.to_excel('豆瓣电影.xlsx',index=True)
#%%
import pandas as pd
pf=pd.read_excel('./豆瓣电影.xlsx',index_col=0)
pf['date']=pf['时间、类型'].apply(lambda x:x.split('/')[0].strip())
pf['country']=pf['时间、类型'].apply(lambda x:x.split('/')[1].strip())
pf['type']=pf['时间、类型'].apply(lambda x:x.split('/')[2].strip())
writer=pd.ExcelWriter('temp.xlsx')
# pf.to_excel('temp.xlsx',sheet_name='原始数据')
# writer.close()
# for i in pf['country'].unique():
#     pf[pf['country']==i].to_excel(writer,sheet_name=i)
# writer.close()

type_list=set(z for i in pf['type'] for z in i.split(' '))
type_list.remove('1978(中国大陆)')

for ty in type_list:
    pf[pf['type'].str.contains(ty)].to_excel(writer,sheet_name=ty)

writer.close()






