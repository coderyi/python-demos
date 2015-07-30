#用Python简单处理URL
# 如果要抓取百度上面搜索关键词为Jecvay Notes的网页, 则代码如下
#http://jecvay.com/2014/09/python3-web-bug-series1.html
import urllib
import urllib.request
 
data={}
data['word']='Jecvay Notes'
 
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)