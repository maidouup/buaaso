# -*- coding: cp936 -*-
import urllib
import urllib2
import re
import os
import time
import sys
#import Image
stdout = sys.stdout  
reload(sys) 
sys.setdefaultencoding('utf-8')  #解决Unicode编码问题
sys.stdout = stdout             #解决加入sys 后print无法输出
user_agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
headers={'User-Agent' : user_agent}            
from urllib2 import Request, urlopen, URLError, HTTPError

class Spider:

    def __init__(self):
        self.siteURL1 ='http://graduate.buaa.edu.cn/StudentQuery.jsp'#提交表单位置
        self.siteURL2 = 'http://graduate.buaa.edu.cn/result.jsp'
        self.siteURL3 = 'http://graduate.buaa.edu.cn/image.jsp'
        self.url1=0
        self.postdata=urllib.urlencode({'studentname':'曹兴兴',
                                        'code':''
                                        })
        cookie = cookielib.CookieJar()    
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

    def url_proxy(self):#出现url_open error 1006错误，设置代理，同时也可以用time的sleep函数
        proxylist =(
            '211.167.112.14:80',
            '210.32.34.115:8080',
            '115.47.8.39:80',
            '211.151.181.41:80',
            '219.239.26.23:80')
        #enable_proxy=True
        proxy ='http://210.32.34.115:8080'
        #null_proxy_handler = urllib2.ProxyHandler({})
        #if enable_proxy:
        opener = urllib2.build_opener(urllib2.ProxyHandler({'http':proxy}),urllib2.HTTPHandler(debuglevel=1))
        #else:
        #opener = urllib2.build_opener(null_proxy_handler)
        urllib2.install_opener(opener)
    def htmldo(self):
        #html=open(r'E:\mywork\buaauser_files\result.html','r').open()
        html=open(r'E:\mywork\spider\tuispider','r').open()
        print html

           
    def geturl1(self,user):#获取版块中每页的帖子链接与主题，每页的第一个链接不用。
               #print item[1],item[3],item[4]
               url2=self.siteURL3+item[1]+"?au="+user
               #print url2
               #self.url_proxy()
               request = urllib2.Request(url2,headers = headers)
               response = urllib2.urlopen(request,timeout=5)
               page2 = response.read().decode('utf-8')
               pattern2 = re.compile(r'<li class="f">.*?</li><li>(.*?)</li>',re.S)
               result = re.findall(pattern2,page2)
               #print len(result[0])
               #print(len(result1))
               if len(result[0])>7:
                   #print url2,item[3]
                   title=item[3].encode('utf-8')
                   f=open(user+'.txt','a+')#w覆盖a后加
                   f.writelines(str(title)+'\n'+url2+'\n')
                   f.close()
               #else:
                    #print '',
spider=Spider()
spider.htmldo()
#spider.geturl1(user)
