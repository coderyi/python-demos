# -*- coding: utf-8 -*-

#https://github.com/Show-Me-the-Code/python/tree/master/JiYouMCC/0011
'''
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
'''
def word_check(input_word, filtered_words):
    for word in filtered_words:
        # print(word)
        # print(input_word)
        if word in input_word:

            return 'Freedom'
    return 'Human Rights'




file = open('filtered_words.txt')
filtered_words=[line.replace('\n','') for line in file]
print (word_check('程序员在上班。', filtered_words))
print (word_check('我妈妈是农民。', filtered_words))