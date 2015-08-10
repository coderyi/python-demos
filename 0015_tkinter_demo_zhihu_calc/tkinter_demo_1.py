
#http://www.cnblogs.com/fuyunbiyi/archive/2012/06/13/2548497.html  Python下用Tkinter进行GUI编程

#-*- encoding=UTF-8 -*-
__author__ = 'fyby'
from tkinter import *
class App:
    def __init__(self, master):
        #构造函数里传入一个父组件(master),创建一个Frame组件并显示
        frame = Frame(master)
        frame.pack()
        #创建两个button，并作为frame的一部分
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT) #此处side为LEFT表示将其放置 到frame剩余空间的最左方
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("hi there, this is a class example!")

win = Tk()
app = App(win)
win.mainloop()