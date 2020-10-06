import xlwt
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
host ='https://www.jianshu.com/'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}



def get_urls():
    #从首页获取文章的url
    content =requests.get(host,headers=headers).text
    soup = BeautifulSoup(content,'lxml')
    for a in soup.find_all('a',class_='title'):
        yield urljoin(host,a.get('href'))

def get_info(url):
    #获取文章的标题、作者、发布时间、正文内容
    content=requests.get(url,headers=headers).text
    soup=BeautifulSoup(content,'lxml')
    title=soup.find('h1',class_='_1RuRku').text
    author=soup.find('a',class_='_1OhGeD').text
    timestamp=soup.find('time',class_='2020-09-02T23:10:00.000Z').text
    body=soup.find('article',class_='_2rhmJa')
    p_list=[]
    for p in body.find_all('p'):
        p_list.append(p.text)
    body_str='\n'.join(p_list)
    return {'url':url,'title':title,'author':author,'timestamp':timestamp,'body':body_str}

def save_as_xls(info_list):
    #获取文章存储到本地
    workbook=xlwt.Workbook(encoding='utf8')
    worksheet=workbook.add_sheet('sheet1')
    titles=['链接','标题','作者','发布时间','正文']
    keys=['url','title','author','timestamp','body']
    for index, title in enumerate(titles):
        worksheet.write(0,index,title)
    for i,info in enumerate(info_list):
        for j,key in enumerate(keys):
            worksheet.write(i+1,j,info[key])
    workbook.save('info.xls')
def main():
    info_list =[]
    for url in get_urls():
        info_list.append(get_info(url))
    save_as_xls(info_list)

def main1():
    content =requests.get(host,headers=headers).text
    soup = BeautifulSoup(content,'lxml')
    titles=soup.find_all('a',class_='title')
    for title in titles:
        print(urljoin(host,title.get('href')))
        print(title.text)
if __name__ == '__main__':
    main1()
    