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

#지금날짜시간 구하기
now_time = datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")

# 데이터 받기
form = cgi.FieldStorage()
user_date = form['user_date'].value
user_time = form['user_time'].value
user_carnum = form['user_carnum'].value
user_password = form['user_password'].value

# 파일에 예약내용 저장하기
f = open('c:/Bitnami/wampstack-7.4.13-0/apache2/htdocs/H_AUTO_reservation_v2/data/{}'.format(user_date),'a', encoding='utf-8')
f.write("{},{},{},{}\n".format(user_date, user_time, user_carnum, user_password))
f.close()


# HTML 본문
print("""
<!doctype html>
<html>
    <head>
        <title>향산힐스테이트 H오토 예약</title>
        <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
        <meta content="utf-8" http-equiv="encoding">
        <link rel="stylesheet" href="reservation_popup__style.css">
    </head>
    <body>
        <form action="res_status.py" method="POST"> 
            <p id="res_complete">예약이 완료되었습니다.</p>
            <p><input type="hidden" value={user_date} name="user_date"/></p>
            <input type="submit" value="확인"/>
        </form>
    </body>
</html>
""".format(user_date=user_date))