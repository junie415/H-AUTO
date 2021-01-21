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

#오늘날짜 구하기
today_date = datetime.datetime.today().strftime("%Y-%m-%d")

#HTML 본문
print("""
<!doctype html>
<html>
    <head>
        <title>향산힐스테이트 H오토 예약</title>
        <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
        <meta content="utf-8" http-equiv="encoding">
        <link rel="stylesheet" href="index_style.css">
    </head>
    <body>
        <h1>향산힐스테이트 H오토존 예약</h1>
        <div>
        <h2>날 짜</h2>
            <form action="res_status.py" method="POST"> 
                <input type="date" id="date" value={today_date} min={today_date} name="user_date"/> <input type="submit" value="조회"/>
            </form>
        </div>
    </body>
</html>
""".format(today_date=today_date))