# -*- coding: cp936 -*-
import urllib
import urllib2
import re
import os
import time
import codecs
import sys
import pymssql
stdout = sys.stdout  
reload(sys) 
sys.setdefaultencoding('utf-8')  #解决Unicode编码问题
sys.stdout = stdout             #解决加入sys 后print无法输出

class Spider:

    def __init__(self):
        self.siteURL1 ='http://graduate.buaa.edu.cn/StudentQuery.jsp'#提交表单位置
        self.siteURL2 = 'http://graduate.buaa.edu.cn/result.jsp'
        self.siteURL3 = 'http://graduate.buaa.edu.cn/image.jsp'
        self.url1=0
        #创建一个数据库连接，host是服务器的ip地址，如果是本机可以用"."，user是访问用户名，password是密码，database是数据库名，比ADO的连接似乎简单一些
        self.conn=pymssql.connect(host=".",user="sa",password="0792",database="pyspider")
        #创建游标对象，相当于ADO的记录集
        self.cur=self.conn.cursor()
        #执行命令
        #sql="select stuID,stuName from buaauser"
        #self.cur.execute(sql)
        #取出所有记录，返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
        #for (stuID,stuName) in self.cur.fetchall():
            #print "ID:"+str(stuID)+",Title:"+stuName+ ""
            #注意，需要转成string类型，或者用格式化输出
        #sql="Insert into buaauser(stuName)values('xx')"
        #插入一条记录
        #self.cur.execute(sql)
        #只有执行了下面的命令，上面的操作才能生效，配合异常处理，可以实现pymssql的事务操作
        #conn.commit()
        #关闭数据库的连接
        #conn.close()
        

    def htmldo(self):
        
        html=codecs.open(r'E:\mywork\buaauser_files\result.html','r','utf-8').read()
        #html=codecs.open(r'E:\mywork\buaauser_files\pvcount.html','r','utf-8').read()
        #print html
        pattern = re.compile(r'<tr bgcolor="#2E9FD2".*?style="WIDTH: 98px">(.*?)</td>.*?style="WIDTH: 106px">(.*?)</td>.*?style="WIDTH: 212px">(.*?)</td>.*?valign="middle">(.*?)</td>',re.S)
        #pattern = re.compile(r'<body>(.*?)</body>',re.S)
        result = re.findall(pattern,html)
        i=42289
        print len(result),sys.getsizeof(result)#42288咋合格数据有问题，可以跳过
        while i<92274:
            #print result[i]
            sql="Insert into buaauser(stuID,stuName,stuSchool,stuMajor) values('%s','%s','%s','%s')"%(result[i][0],str(result[i][1]).encode('utf-8'),str(result[i][2]).encode('utf-8'),str(result[i][3]).encode('utf-8'))
            self.cur.execute(sql)
            self.conn.commit()
            i+=1
            #print i
        #sql="Insert into buaauser(stuID,stuName,stuSchool,stuMajor) values('%s','%s','%s','%s')"%(result[1][0],str(result[1][1]).encode('utf-8'),str(result[1][2]).encode('utf-8'),str(result[1][3]).encode('utf-8'))
       # self.cur.execute(sql)
        #self.conn.commit()
        #关闭数据库的连接
        self.conn.close()
        #for key in result[1]:
            #print key[1]
            #写入txt 可正常使用
            #f=open('buaauser'+'.txt','a+')#w覆盖a后加
            #f.writelines(str(key.encode('utf-8'))+' ')
            #f.close()
            
       
           
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
