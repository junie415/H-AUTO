#!C:\Users\user\AppData\Local\Programs\Python\Python39\python.exe
#-*- coding: utf-8 -*-
import sys
import codecs
import cgi
import datetime
import cgitb
cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("content-type:text/html; charset=utf-8\r\n")
#-------------------------------------------------------------------------

# 데이터 받기
form = cgi.FieldStorage()
user_date = form['user_date'].value
user_time = form['user_time'].value
user_carnum = form['user_carnum'].value

#HTML 본문
print("""
<!doctype html>
<html>
    <head>
        <title>향산힐스테이트 H오토 예약</title>
        <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
        <meta content="utf-8" http-equiv="encoding">
        <link rel="stylesheet" href="res_cancel_style.css">
    </head>
    <body>
        <h2>예약취소</h2>
            <form action="res_cancel_popup.py" method="POST"> 
                <p>날 짜 : {user_date}</p>
                <input type="hidden" value={user_date} name="user_date"/>
                <p>시 간 : {user_time}차시({t1}:00~{t2}:00)</p>
                <input type="hidden" value={user_time} name="user_time"/>
                <p>차량번호 : {user_carnum}</p>
                <input type="hidden" value={user_carnum} name="user_carnum"/>
                <p>비밀번호 : <input type="text" name="user_password" pattern="[0-9]{a}" placeholder="****" required/></p>
                <input type="submit" value="취소하기"/>
            </form>
    </body>
</html>
""".format(user_date=user_date, user_time=user_time, t1 = str(int(user_time)+9), t2 = str(int(user_time)+10), user_carnum=user_carnum, a= {4}))