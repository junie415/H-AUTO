#!C:\Users\user\AppData\Local\Programs\Python\Python39\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import cgi
import datetime
import cgitb
import time
cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("content-type:text/html; charset=utf-8\r\n")
#-------------------------------------------------------------------------

# 데이터 받기
form = cgi.FieldStorage()
user_date = form['user_date'].value
user_time = form['user_time'].value
user_carnum = form['user_carnum'].value
user_password = form['user_password'].value

# 비밀번호 확인
li=[]

num_lines = sum(1 for line in open('c:/Bitnami/wampstack-7.4.13-0/apache2/htdocs/H_AUTO_reservation_v2/data/{}'.format(user_date)))
f=open('c:/Bitnami/wampstack-7.4.13-0/apache2/htdocs/H_AUTO_reservation_v2/data/{}'.format(user_date),'r', encoding='utf-8')

for i in range(1,num_lines+1):
    mystring = f.readline()
    mystring=mystring.rstrip()
    li=mystring.split(',')
    if (li[0] == user_date and li[1] == user_time and li[2] == user_carnum and li[3] == user_password):
        print("""
                <html>
                <head>
                        <link rel="stylesheet" href="res_cancel_popup_style.css">
                </head>
                <body>
                <form action="res_status.py" method="POST"> 
                        <p>예약이 취소되었습니다.</p>
                        <p><input type="hidden" value={user_date} name="user_date"/></p>
                        <input type="submit" value="확인"/>
                </form>
                </body>
                </html>   
        """.format(user_date=user_date))

        with open("c:/Bitnami/wampstack-7.4.13-0/apache2/htdocs/H_AUTO_reservation_v2/data/{}".format(user_date), "r") as f:
                lines = f.readlines()
        with open("c:/Bitnami/wampstack-7.4.13-0/apache2/htdocs/H_AUTO_reservation_v2/data/{}".format(user_date), "w") as f:
                for line in lines:
                        if (line.strip("\n") != user_date +","+ user_time +","+ user_carnum +","+ user_password):
                                f.write(line)

    else:
        print("""
                <html>
                <head>
                        <link rel="stylesheet" href="res_cancel_popup_style.css">
                </head>
                <body>
                        <p>비밀번호가 틀렸습니다.</p>
                        <button type="button" onclick="history.back()">돌아가기</button>
                </body>
                </html>   
        """)