__author__ = 'Wayne'
import urllib.request
import os
import re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
    response = urllib.request.urlopen(req)
    return response.read()




def find_imgs(page_url):
    pattern = r'src="(.*?.jpg)"'

    html = url_open(page_url).decode('utf-8')
    img_addrs = re.findall(pattern,html)
    return img_addrs

def save_imgs(img_addrs,page_num,folder):
    os.mkdir(str(page_num))
    os.chdir(str(page_num))
    for i in img_addrs:
        pattern = r'douban-group-img/(.*?).jpg'
        filename = i.split('/')[-1]
        image = url_open(i)
        with open(filename,'wb') as f:
            f.write(image)
            f.close()


def download_mm(folder='ooxx',pages=10):
    os.mkdir(folder) #新建文件夹
    os.chdir(folder) #跳转到文件夹
    folder_top = os.getcwd() #获取当前工作目录
    url = 'http://www.dbmeinv.com/dbgroup/show.htm?pager_offset='
    page_num = 1 #获取网页最新的地址
    for i in range(pages):
        page_num += i #递减下载几个网页
        page_url = url + str(page_num)  #组合网页地址
        print(page_url)
        img_addrs = find_imgs(page_url) #获取图片地址
        save_imgs(img_addrs,page_num,folder) #保存图片
        os.chdir(folder_top)

if __name__ == '__main__':
    folder = input("Please enter a folder(default is 'ooxx'): " )
    pages = input("How many pages do you wan to download(default is 10): ")
    download_mm(str(folder),int(pages))