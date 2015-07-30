#http://jecvay.com/2015/02/python3-web-bug-series5.html
#零基础自学用Python 3开发网络爬虫(五): 使用第三方模块快速抓取与解析
import requests
from bs4 import BeautifulSoup
response = requests.get("http://jecvay.com")
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.text)
# print(soup.body.text)

for x in soup.findAll("a"):
    print(x['href'])