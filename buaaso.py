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
sys.setdefaultencoding('utf-8')  #���Unicode��������
sys.stdout = stdout             #�������sys ��print�޷����

class Spider:

    def __init__(self):
        self.siteURL1 ='http://graduate.buaa.edu.cn/StudentQuery.jsp'#�ύ��λ��
        self.siteURL2 = 'http://graduate.buaa.edu.cn/result.jsp'
        self.siteURL3 = 'http://graduate.buaa.edu.cn/image.jsp'
        self.url1=0
        #����һ�����ݿ����ӣ�host�Ƿ�������ip��ַ������Ǳ���������"."��user�Ƿ����û�����password�����룬database�����ݿ�������ADO�������ƺ���һЩ
        self.conn=pymssql.connect(host=".",user="sa",password="0792",database="pyspider")
        #�����α�����൱��ADO�ļ�¼��
        self.cur=self.conn.cursor()
        #ִ������
        #sql="select stuID,stuName from buaauser"
        #self.cur.execute(sql)
        #ȡ�����м�¼�����ص���һ������tuple��list��list��Ԫ���Ǽ�¼�У�tuple��Ԫ����ÿ�м�¼���ֶ�
        #for (stuID,stuName) in self.cur.fetchall():
            #print "ID:"+str(stuID)+",Title:"+stuName+ ""
            #ע�⣬��Ҫת��string���ͣ������ø�ʽ�����
        #sql="Insert into buaauser(stuName)values('xx')"
        #����һ����¼
        #self.cur.execute(sql)
        #ֻ��ִ����������������Ĳ���������Ч������쳣��������ʵ��pymssql���������
        #conn.commit()
        #�ر����ݿ������
        #conn.close()
        

    def htmldo(self):
        
        html=codecs.open(r'E:\mywork\buaauser_files\result.html','r','utf-8').read()
        #html=codecs.open(r'E:\mywork\buaauser_files\pvcount.html','r','utf-8').read()
        #print html
        pattern = re.compile(r'<tr bgcolor="#2E9FD2".*?style="WIDTH: 98px">(.*?)</td>.*?style="WIDTH: 106px">(.*?)</td>.*?style="WIDTH: 212px">(.*?)</td>.*?valign="middle">(.*?)</td>',re.S)
        #pattern = re.compile(r'<body>(.*?)</body>',re.S)
        result = re.findall(pattern,html)
        i=42289
        print len(result),sys.getsizeof(result)#42288զ�ϸ����������⣬��������
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
        #�ر����ݿ������
        self.conn.close()
        #for key in result[1]:
            #print key[1]
            #д��txt ������ʹ��
            #f=open('buaauser'+'.txt','a+')#w����a���
            #f.writelines(str(key.encode('utf-8'))+' ')
            #f.close()
            
       
           
    def geturl1(self,user):#��ȡ�����ÿҳ���������������⣬ÿҳ�ĵ�һ�����Ӳ��á�
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
                   f=open(user+'.txt','a+')#w����a���
                   f.writelines(str(title)+'\n'+url2+'\n')
                   f.close()
               #else:
                    #print '',
spider=Spider()
spider.htmldo()

#spider.geturl1(user)
