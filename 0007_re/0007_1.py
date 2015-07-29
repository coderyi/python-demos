__author__ = 'coderyi'
# -*- coding: utf-8 -*-
#re 正则表达式
#https://github.com/Show-Me-the-Code/python/blob/master/JiYouMCC/0012/0012.py
#第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入
# 「北京是个好城市」，则变成「**是个好城市」。
import re


def word_change(input_word, filtered_words):
    result = input_word
    for word in filtered_words:
        if word in result:
            strinfo = re.compile(word)
            print(strinfo)
            print(word)
            result = strinfo.sub('*' * len(word), result)
    return result

file = open('filtered_words.txt')
filtered_words = [line.replace('\n', '') for line in file]

print (word_change('lovely boy', filtered_words))
print (word_change('程序员在上班。', filtered_words))
print (word_change('我妈妈是农民。', filtered_words))


#http://outofmemory.cn/code-snippet/992/Python-regular-expression-re-module-operation-guide
#python正则表达式模块简介