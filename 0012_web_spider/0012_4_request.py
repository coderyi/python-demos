#伪装浏览器正规军
#http://jecvay.com/2014/09/python3-web-bug-series3.html
import urllib.request
def saveFile(data):
    save_path = '0012_4_request.txt'
    f_obj = open(save_path, 'wb') # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()


url = 'http://www.baidu.com/'
req = urllib.request.Request(url, headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
oper = urllib.request.urlopen(req)
data = oper.read()
print(data.decode())
saveFile(data)