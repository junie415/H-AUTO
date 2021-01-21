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

# 오늘날짜 구하기
today_date = datetime.datetime.today().strftime("%Y-%m-%d")

# 데이터 받기
form = cgi.FieldStorage()
user_date = form['user_date'].value

# 예약현황 딕셔너리에 담기
li=[]
res_status=[]
dic={'1차시':'예약 가능', '2차시':'예약 가능', '3차시':'예약 가능', '4차시':'예약 가능', '5차시':'예약 가능', '6차시':'예약 가능', '7차시':'예약 가능', '8차시':'예약 가능', '9차시':'예약 가능', '10차시':'예약 가능', '11차시':'예약 가능', '12차시':'예약 가능'}
try:
    num_lines = sum(1 for line in open('c:/Bitnami/wampstack-7.4.13-0/apache2/htdocs/H_AUTO_reservation_v2/data/{}'.format(user_date)))
    f=open('c:/Bitnami/wampstack-7.4.13-0/apache2/htdocs/H_AUTO_reservation_v2/data/{}'.format(user_date),'r', encoding='utf-8')

except:
    f=open('c:/Bitnami/wampstack-7.4.13-0/apache2/htdocs/H_AUTO_reservation_v2/data/{}'.format(user_date),'w', encoding='utf-8')
    num_lines = sum(1 for line in open('c:/Bitnami/wampstack-7.4.13-0/apache2/htdocs/H_AUTO_reservation_v2/data/{}'.format(user_date)))


for i in range(1,num_lines+1):
    mystring = f.readline()
    mystring=mystring.rstrip()
    li=mystring.split(',')
    res_status.append(li)
    for j in range(1,13):
        if (res_status[i-1][1] == str(j)):
            dic[str(j)+'차시'] = res_status[i-1][2]

# 예약여부에 따라 예약하기, 예약취소 표시하기
contents=[]

for i in range(1,13):
    if len(dic[str(i)+'차시']) == 4 :
        content = ("""<form action="res_cancel.py" method="POST">        
                    {n}차시({t1}:00~{t2}:00) : 예약 완료({car_num})
                    <input type="hidden" value={user_date} name="user_date"/>
                    <input type="hidden" value={n} name="user_time"/>
                    <input type="hidden" value={car_num} name="user_carnum"/>
                    <input type="submit" value="예약취소"/> 
                    </form>""".format(car_num=dic[str(i)+'차시'], user_date=user_date, n=str(i), t1=str(i+9), t2=str(i+10)))
        contents.append(content)
    else :
        content = ("""<form action="reservation.py" method="POST">        
                    {n}차시({t1}:00~{t2}:00) : {ok}
                    <input type="hidden" value={user_date} name="user_date"/>
                    <input type="hidden" value={n} name="user_time"/>
                    <input type="submit" value="예약하기"/> 
                    </form>""".format(ok=dic[str(i)+'차시'], user_date=user_date, n=str(i), t1=str(i+9), t2=str(i+10)))
        contents.append(content)

# HTML 본문
print("""
<!doctype html>
<html>
    <head>
        <title>향산힐스테이트 H오토 예약</title>
        <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
        <meta content="utf-8" http-equiv="encoding">
        <link rel="stylesheet" href="res_status_style.css">
    </head>
    <body>
        <h1>향산힐스테이트 H오토존 예약</h1>
        <div>
            <h2>날 짜</h2>
                <form action="res_status.py" method="POST"> 
                    <input type="date" id="date" value={user_date} min={today_date} name="user_date"/> <input type="submit" value="조회"/>
                </form>
            <h2 id="res">예약현황<small> {user_date}</small></h2> 
                <div id="contents">
                    <div id=c1>
                    {content_1}
                    </div>
                    <div id=c2>
                    {content_2}
                    </div>
                    <div id=c3>
                    {content_3}
                    </div>
                    <div id=c4>
                    {content_4}
                    </div>
                    <div id=c5>
                    {content_5}
                    </div>
                    <div id=c6>
                    {content_6}
                    </div>
                    <div id=c7>
                    {content_7}
                    </div>
                    <div id=c8>
                    {content_8}
                    </div>
                    <div id=c9>
                    {content_9}
                    </div>
                    <div id=c10>
                    {content_10}
                    </div>
                    <div id=c11>
                    {content_11}
                    </div>
                    <div id=c12>
                    {content_12}
                    </div>
                </div>
        </div>
    </body>
</html>
""".format(today_date=today_date, user_date=user_date, content_1=contents[0], content_2=contents[1], content_3=contents[2], content_4=contents[3], content_5=contents[4], content_6=contents[5], content_7=contents[6], content_8=contents[7], content_9=contents[8], content_10=contents[9], content_11=contents[10], content_12=contents[11]))