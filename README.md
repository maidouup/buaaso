# buaaso
Python：personal message search via SQL Injection Attacks 
http://www.2cto.com/Article/201501/373188.html
website1：http://graduate.buaa.edu.cn/ch/xuesheng/index.jhtml
运行这个buaaso.py就可以

step1：fill with test code 'or'1'='1，and you can find the 92244 datas show up ,and find the real login in page
  通过SQL攻击测试，发现漏洞，同时找到登陆的真正页面。具体通过http://www.pythonclub.org/python-network-application/observer-spider

step2:download the page and find the datas by regular expression and Python; 通过python与正则表达式找出html中的数据

step3：connect the database through the module pymssql in Python,将数据存入SQL数据库，参看http://blog.chinaunix.net/uid-27570589-id-5108429.html
####此部分为buaasoLib.py实现
step4:发现buaa的图书馆，http://buaalib.com/，登录页面，一般为学号，密码也为学号，试着登录一个账号，来自上述数据库。可以再个人信息页面http://202.112.134.140:8080/reader/redr_info.php中发现，个人的基本信息，可以抓取下来，并且统计修改密码的人数。
 step5.处理数据库，用于提取可以用的用户（没有注销账号的），where substring(stuID,3,2)='13'orsubstring (stuID,3,2)='14',可以后去某个个字段的第3个字符的2个字符比较。
 step6.获取登录页面的真实地址，与真实数据。直接在html中，地址，标签为form action，变量（数据），为id标签的
 step7.利用cookie登录第二地址，再分析页面html，利用正则表达式获取需要的个人信息，这里的findall，注意为list 与元组的组合，读取这种格式。
 step8。数据库操作，循环将userID作为postData登录，并且将数据弄下来，再讲数据更新到指定的记录中，设计，插入，更新，含变量的SQL语句，多行的python代码等。

