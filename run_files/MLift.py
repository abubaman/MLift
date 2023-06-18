# -*- coding:utf-8 -*-
import telegram
import requests
import os
import sys
import datetime
import schedule
import time

import sqlite3

#from telegram.ext import Updater, MessageHandler, Filters


##### chatbot Setting #####
chat_token = "Enter Your Chatbot Token"


##### user Setting #####
user_info = {'number' : 1,
             'username' : 'abubaman',
             'telegram': 'Enter Your Telegram ID',
             'clg_start' :'',
             'clg_end' : '',
             'clg_type': '',
             'clg_iter': '',
             'user_gender': '',
             'user_height': 0,
             'user_weight': 0,
             'attend': 0,
             'success_fail':0,
             'calorie':0,
             'get_point':0,
             'accum_point':0
             }

## 하루에 한 번씩 _noti = 0으로 초기화 해야함. schedule로 하면 됨.(아직안함)
attend_noti = 0
sf_noti = 0

#########################################################################################

############### Initialize ################

def initBot():
    global chat_token
    global bot
    global updates

    print(user_info['username'] + ' : ' + "## initBot Start ##")

    bot = telegram.Bot(token=chat_token)
    #updates = bot.getUpdates()

############### User Info 불러오기 #################
def getUserInfo():
    ## db.sqlite3에서 user_info의 id에 해당하는 사용자 정보를 가져오는 함수
    global user_info
    global attend_noti
    global sf_noti
    
    conn = sqlite3.connect('/home/lift_abuba_kr/db.sqlite3')
    cursor = conn.cursor()

    all_list =['clg_start', 'clg_end', 'clg_type', 'clg_iter', 'user_gender', 'user_height', 'user_weight', 'attend', 'success_fail','calorie','get_point','accum_point']
    
#     query = "SELECT clg_start FROM accounts_user WHERE username='abubaman''"
#     print(query)
#     cursor.execute(query)
#     print(tuple(cursor))
    
    while True:
        time.sleep(1)
        #user info를 db에서 불러옴
        for i in all_list:
            query = "SELECT " + i +" FROM accounts_user WHERE username="+"'"+user_info['username']+"'"
            #print(query)
            cursor.execute(query)
            tu = tuple(cursor)
            #print(tu)
            user_info.update({i:tu[0][0]})
        #print(user_info)
        
        #출석 판단
        if user_info['attend']==1 and attend_noti == 0 :
            attend_noti = 1
            print("출석")
            message = user_info['username']+"님이 로그인 하였습니다."
            sendMessage(user_info['telegram'], message)
        
        #성공 판단
        if user_info['success_fail']==1 and sf_noti == 0 :
            sf_noti = 1
            print("달성")
            
            user_info['calorie'] = user_info['calorie']+1
            user_info['get_point'] = int(user_info['clg_iter'])
            user_info['accum_point'] = user_info['accum_point'] + user_info['get_point']
            
            
            query = "UPDATE accounts_user SET calorie = "+ str(user_info['calorie']) +" WHERE username='abubaman'"
            print(query)
            cursor.execute(query)
            
            message = user_info['username']+"님이 목표를 달성했습니다.\n - 챌린지 달성 횟수 : "+str(user_info['calorie'])+"/"+str(user_info['clg_type'])+"\n - 소모 칼로리 : "+str(calorieCalc())+"kcal"+"\n - 금회 누적 포인트 : "+str(user_info['get_point'])+"\n - 총 누적 포인트 : "+str(user_info['accum_point'])
            sendMessage(user_info['telegram'], message)
            #DB를 0,0으로 업데이트
            query = "UPDATE accounts_user SET attend = 0 WHERE username='abubaman'"
            print(query)
            cursor.execute(query)
            
            query = "UPDATE accounts_user SET success_fail = 0 WHERE username='abubaman'"
            print(query)
            cursor.execute(query)
            
            query = "UPDATE accounts_user SET get_point = "+ str(user_info['get_point']) +" WHERE username='abubaman'"
            print(query)
            cursor.execute(query)
            
            query = "UPDATE accounts_user SET accum_point = "+ str(user_info['accum_point']) +" WHERE username='abubaman'"
            print(query)
            cursor.execute(query)            
            
            conn.commit()#데이터 수정,삭제,추가의 경우 커밋해야 반영됨
            
    conn.close()

########## 포인트 계산 함수들 ##########
def calorieCalc():
    global user_info
    #print(user_info['calorie'])
    calorie = int(user_info['clg_iter']) * 7
    return calorie



def sendMessage(chat_id, message):
    #global chat_id
    global bot
    global user_info
    
    if message == "":
        bot.send_message(chat_id=chat_id, text="메시지가 없습니다.")
    else:
        bot.send_message(chat_id=chat_id, text=message)


def getCurrentDate():
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    current_weekday = now.weekday()
    return (current_year,current_month,current_day,current_weekday)


def getReserveDate():
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    current_weekday = now.weekday()
    dt1 = datetime.datetime(current_year, current_month, current_day, 7, 1) # 현재날짜 07시 01분
    dt2 = dt1 + datetime.timedelta(days = 1) # 1일후
    reserve_year = dt2.year
    reserve_month = dt2.month
    reserve_day = dt2.day
    reserve_weekday = dt2.weekday()

    return (reserve_year, reserve_month, reserve_day, reserve_weekday)

# 
# 
# ############### Database #################
# def setNone():
#     global user_info
#     print(user_info['id'] + ' : ' +"## setNone Start ##")
#     
#     conn = sqlite3.connect('/home/grsalad_abuba_kr/db.sqlite3') # DB 연결하고
#     cursor = conn.cursor()
#     
#     ## for db update
#     conn = sqlite3.connect('/home/grsalad_abuba_kr/db.sqlite3')
#     cursor = conn.cursor()
#     query = "UPDATE accounts_user SET grc_meal_result=? WHERE username="+user_info['id']
#     cursor.execute(query, (['none']))
#     print(user_info['id'] + "의 grc_meal_result 가 none으로 초기화되었습니다.")
#     conn.commit()
#     conn.close()



#########################################################################################
if __name__ == "__main__":
    # 현재시각을 찍고
    current_time = time.strftime('%m-%d %H:%M:%S', time.localtime(time.time()))
    print(user_info['username'] + ' : ' +"#### Main Program Start #### : " + current_time)

    # TelegramBot을 켜고
    initBot()

    ## User Info를 가져오고
    getUserInfo() #db.sqlite3로부터

    ## 종료 판단을 한 다음
    #quitDecide(1)

    ## scheduler에 반복 시간을 등록한다.
    #initSchedule()

    ## scheduler에 queue 되어 있는 함수를 주기적으로 실행 리스트에 올림. time.sleep(1)은 너무 잦은 반복을 피하기 위한 장치.
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
