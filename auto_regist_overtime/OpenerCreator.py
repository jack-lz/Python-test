#coding=utf8
#!/usr/bin/python
#Filename:OpenerCreator.py

import urllib, urllib2
import cookielib



#通过header来自定义opener
class OpenerCreator(object):
    __instance = None
    __inited = None

    def __new__(cls, headers) :
        if (cls.__instance == None) :
            cls.__instance = object.__new__(cls, headers) 
        return cls.__instance

    def __init__(self, headers):
        if (OpenerCreator.__inited == None) :
            self.headers = headers
            OpenerCreator.__inited = True

    def setHeaders(self, headers):
        self.headers = headers

    #通过header来自定义opener
    def MakeMyOpener(self):
        cookiejar = cookielib.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
        cookie = urllib2.HTTPCookieProcessor(cookiejar)# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        opener = urllib2.build_opener(cookie) #自定义opener,并将opener跟CookieJar对象绑定
        headerlist = []
        for key, value in self.headers.items():
            elem = (key, value)
            headerlist.append(elem)
        opener.addheaders = headerlist
        urllib2.install_opener  #安装opener,我们通过urlopen使用默认opener。但你能够创建个性的openers。
        return opener
        
