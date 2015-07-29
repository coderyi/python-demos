
# -*- coding: utf-8 -*-

#json处理， 通过xlwt处理excel表格，

'''
https://github.com/Show-Me-the-Code/python/tree/master/JiYouMCC/0014
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中
'''

import xlwt
import json


file = xlwt.Workbook(encoding='utf-8')  # 注意这里的Workbook首字母是大写
table = file.add_sheet('student', cell_overwrite_ok=True) # 新建一个sheet
txt = open('student.txt').read()
json_txt = json.loads(txt)
print(json_txt)
for x in range(len(json_txt)):
    table.write(x, 0, x + 1) # 写入数据table.write(行,列,value)
    for y in range(len(json_txt[str(x + 1)])):
        print(range(len(json_txt[str(x + 1)])))
        print(json_txt[str(x + 1)])
        table.write(x, y + 1, json_txt[str(x + 1)][y])
file.save('students.xls')



# http://liluo.org/blog/2011/01/python-using-xlrd-xlwt-operate-excel/
#Python 使用 Xlrd/xlwt 操作 Excel

#http://www.cnblogs.com/coser/archive/2011/12/14/2287739.html
#Python处理JSON