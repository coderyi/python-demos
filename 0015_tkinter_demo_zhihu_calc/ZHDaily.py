#-*- coding: utf-8 -*-

# ZHDaily
# Show the list of zhihu-daily items
#
# History:
# 2014-04-29 YW fix [ValueError: day is out of range for month]
# 2014-03-18 Mr.Q.Young(Yorn Wat) created.
#
#https://github.com/mrqyoung/ZHDaily
__version__ = '0.2'


try:
    from tkinter import *
except ImportError:
    from Tkinter import *

import os
from datetime import date as D, date
from datetime import timedelta as TimeDelta


class App():
    def __init__(self, parent, *args, **kw):
        self.master = self._initCanvas(parent)
        #self.master = parent
        today = date.today()
        print(today)
        self.theDateBefore = today + TimeDelta(days=2)
        print(self.theDateBefore)

        self.loadDaily()
        
    def _initCanvas(self, master):
        canvas = Canvas(master)
        frame = Frame(canvas)
        scrollbar = Scrollbar(master, orient=VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(fill=Y, side=RIGHT)
        canvas.pack(side=LEFT, fill=BOTH, expand=YES)
        frame_id = canvas.create_window((0,0), window=frame, anchor=N+W)
        frame.bind("<Configure>", lambda e:canvas.config(scrollregion='0 0 %s %s' % (frame.winfo_reqwidth(), frame.winfo_reqheight())))
        canvas.bind("<Configure>", lambda e:canvas.itemconfig(frame_id, width=e.width))
        buttonMore = Button(canvas, text='more >>', command=self.loadDaily)
        buttonMore.pack(side=BOTTOM, fill=X)
        return frame
    
    def loadDaily(self):
        self.theDateBefore = self.getTheDate(self.theDateBefore)
        print(self.theDateBefore)
        storiesAndLabel = self.getStoriesAndLabel(self.theDateBefore)
        print(storiesAndLabel)
        self.DailyFrame(self.master, storiesAndLabel).pack()
        
    def getTheDate(self, d):
        return d - TimeDelta(days=1)

    def getStoriesAndLabel(self, date_before):
        zhdh = ZHDHelper(date_before.strftime('%Y%m%d'))
        return (zhdh.getStories(), zhdh.date_label)

    class DailyFrame(Frame):
        def __init__(self, master, storiesAndLabel):
            Frame.__init__(self, master)
            self.master = master
            self.stories = storiesAndLabel[0]
            self.label = storiesAndLabel[1]
            self.newLabel().pack(fill=X, side=TOP, padx=8, pady=2)
            self.newListbox().pack(fill=X, side=TOP, ipadx=16, padx=8)
            return None
        def newLabel(self):
            return Label(self.master, bg='CornflowerBlue', fg='white', height=2, padx=8, text = self.label)
        def newListbox(self):
            listbox = Listbox(self.master, height=len(self.stories), selectmode=SINGLE, relief=FLAT)
            for story in self.stories: listbox.insert(END, story.title)
            listbox.bind('<<ListboxSelect>>', self.openThisStory)
            return listbox
        def openThisStory(self, event): #FIXME
            index = int(event.widget.curselection()[0])
            print(index,self.stories[index].share_url)
            cmd = fav_browser + self.stories[index].share_url if fav_browser else 'start ' + self.stories[index].share_url
            print(cmd)

            os.system(cmd)
            


##################################################################
#-*- coding: utf-8 -*-

# zhdhelper
# Get the list of zhihu-daily items
#
# History:
# 2014-03-18 Mr.Q.Young(Yorn Wat) created.
#


import json


class Story():
    ''' A Story/item '''
    
    def __init__(self, i, t, s_u, img_s, u, img, ga, th = None):
        self.id = i
        self.title = t
        self.share_url = s_u
        self.image_source = img_s
        self.url = u
        self.image = img
        self.ga_prefix = ga
        self.thumbnail = th
        


class ZHDHelper():
    ''' Get zhihu-daily items
    
    input: String url; output: Story[] stories
    '''
    
    def __init__(self, date = None):
        url_latest = 'http://news-at.zhihu.com/api/2/news/latest'
        url_before = 'http://news-at.zhihu.com/api/2/news/before/'
        self.url = url_before + date if date else url_latest
        #eg: http://news-at.zhihu.com/api/2/news/before/20140318
        self.date_label = None

    def getWebRaw(self): #FIXME
        userAgent = 'JUC (Linux; U; 2.3.7; zh-cn; MB200; 480*800) UCWEB7.9.3.103/139/999'
        headers = {'User-Agent': userAgent}
        try:
            import urllib.request as Req
        except ImportError:
            import urllib as Req
        print(self.url)
        request = Req.Request(self.url, None, headers)
        response = Req.urlopen(request)
        bytesWebRaw = response.read()
        print(bytesWebRaw.decode('utf-8'))
        return bytesWebRaw.decode('utf-8')

    def getWebRaw2(self, headers):#del--
        import urllib

        request = urllib.Request(self.url, None, headers)
        return urllib.urlopen(request)

    def getStories(self):
        stories = []
        dictStories = json.loads(self.getWebRaw())
        self.date_label = dictStories['date']
        for item in dictStories['news']:
            story = Story(item['id'],
                          item['title'],
                          item['share_url'],
                          item['image'],
                          item['url'],
                          item['image'],
                          item['ga_prefix'],
                          item['thumbnail']
                         )
            stories.append(story)
        return stories



##################################################################

if __name__ == '__main__':
    root = Tk()
    root.geometry('480x640')
    root.title('知乎日报')
    fav_browser = ''
    app = App(root)
    root.mainloop()
