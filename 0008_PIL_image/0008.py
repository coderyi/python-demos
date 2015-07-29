__author__ = 'coderyi'
#PIL第三库的处理
# using PIL in http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow

#https://github.com/Show-Me-the-Code/python/tree/master/JiYouMCC/0005
#第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
from PIL import Image


def change_image_size(image_path='0005.jpg', size=(1136, 640)):
    im = Image.open(image_path)
    size = (size[1], size[0]) if im.size[1] > im.size[0] else size
    im.thumbnail(size, Image.ANTIALIAS)
    im.save('result-' + image_path)

# change_image_size('0005-r.jpg')
change_image_size('0008.jpg')


#http://www.th7.cn/Program/Python/201404/193000.shtml
#python，使用PIL库对图片进行操作