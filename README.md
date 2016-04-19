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
step4:发现buaa的图书馆，http://buaalib.com/，
登录页面，一般为学号，密码也为学号，试着登录一个账号，来自上述数据库。可以再个人信息页面
http://202.112.134.140:8080/reader/redr_info.php
中发现，个人的基本信息，可以抓取下来，并且统计修改密码的人数。
 
 step5.处理数据库，用于提取可以用的用户（没有注销账号的），where substring(stuID,3,2)='13'orsubstring (stuID,3,2)='14',可以后去某个个字段的第3个字符的2个字符比较。
 
 step6.获取登录页面的真实地址，与真实数据。直接在html中，地址，标签为form action，变量（数据），为id标签的
 
 step7.利用cookie登录第二地址，再分析页面html，利用正则表达式获取需要的个人信息，这里的findall，注意为list 与元组的组合，读取这种格式。
 
 step8。数据库操作，循环将userID作为postData登录，并且将数据弄下来，再讲数据更新到指定的记录中，设计，插入，更新，含变量的SQL语句，多行的python代码等。
 目前图书馆系统的个人信息页，身份证信息隐去。
 
 ####buaaso_GW.py 网关验证登录
 buaa网关登录，现在默认的情况，登录为学号stuID（字母小写），密码为身份证号（stuIDNum）后8位。
1.buaa的网络网关登录，网页版地址为：http://gw.buaa.edu.cn/?url=www.baidu.com，
  测试发现，输入密码错误5次，则需要验证码登录，改为其他方式。

2.手机版的登录地址，http://gw.buaa.edu.cn/mobile5.html?url=www.baidu.com
  测试发现，并不存在多次错误，验证码登录的情况，所以可以通过手机版，进行密码循环破解。
  或者验证用户的密码修改情况。

表单提交为：http://202.112.136.131/cgi-bin/srun_portal
登录成功后自动转到http://202.112.136.131/phone/index.php

登录成功有两种情况：
1.出现http://202.112.136.131/phone/index.php页面：出图
里边出现一个登录的IP，或者多个（表明用户设置了可以允许多个设备同时在线，且没有超）
2.没有出现上述页面，仍是，但出现，登录人数过多的提示，说明登录成功只是人数超了。
1.response为password_error
成功情况：
2.一串数字登录成功
3.ip_exist_error		ip未下线
4.online_num_error

登出http://202.112.136.131/cgi-bin/do_logout?action=logout
get方法
参数：
action ：'logout'
response：连接已断开

根据提交的表单
发现密码被加密了。
加密的算法为MD5,所以要对应的去解密了。将传输的字符串加密post过去。

同时还有一个注销也是在同一登录页面部分，点击注销。
获取cookie后就自动的将数据登录

