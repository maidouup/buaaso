# buaaso
Python：personal message search via SQL Injection Attacks 
http://www.2cto.com/Article/201501/373188.html
website1：http://graduate.buaa.edu.cn/ch/xuesheng/index.jhtml
运行这个buaaso.py就可以

step1：fill with test code 'or'1'='1，and you can find the 92244 datas show up ,and find the real login in page
  通过SQL攻击测试，发现漏洞，同时找到登陆的真正页面。具体通过http://www.pythonclub.org/python-network-application/observer-spider

step2:download the page and find the datas by regular expression and Python; 通过python与正则表达式找出html中的数据

step3：connect the database through the module pymssql in Python,将数据存入SQL数据库，参看http://blog.chinaunix.net/uid-27570589-id-5108429.html

