from selenium import webdriver
from pprint import pprint
import requests
import openpyxl
from bs4 import BeautifulSoup
import os
os.chdir("F:\crawler")
os.getcwd()
url ="https://list.jd.com/list.html?cat=9987,653,655"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
def get_site_content(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver.page_source
html = get_site_content(url)
soup = BeautifulSoup(html,'lxml')
items=soup.find_all("li",class_="gl-item")

wb=openpyxl.Workbook()
ws=wb.active
ws.title="手机"
ws.append(["序号","产品","价格","链接"])
for i,item in items:
    price=item.find("strong",class_="J_price").i.get_text()
    title=item.find("div",class_="p-name").em.get_text()
    href="https:"+item.find("a").attrs["href"]
    if not href.startswith("http"):
        href="https:"+href
    ws.append((i+1,title,price,href))
wb.save("cellphone.xlsx")