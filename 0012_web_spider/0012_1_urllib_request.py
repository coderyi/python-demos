# http://jecvay.com/2014/09/python3-web-bug-series1.html
#用Python抓取指定页面
#encoding:UTF-8
import urllib.request
 
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)