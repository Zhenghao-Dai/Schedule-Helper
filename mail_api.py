import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import COMMASPACE
import schedule_api as api
import time

import json
'''
SENDER = 'your.schedule.notification@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
USER_ACCOUNT = {'username': 'your.schedule.notification',
                'password': 'q82070002'}'''

SENDER = 'yourotification@163.com'
SMTP_SERVER = 'smtp.163.com'
USER_ACCOUNT = {'username': 'yourotification',
                'password': 'NLRJIAHHXKFKXLHC'}
SUBJECT = "Open spots"

file_name="suscrible_list.json"
def store(data):
    with open(file_name,'w')as fw:
        json.dump(data,fw)
def load():
    with open(file_name,'r')as f:
        data=json.load(f)
        return data
def add(course,contact_info):
    a=api.schedule_api()
    course_id=course.split(" ") [ 0 ]
    course_sec=course.split(" ")[ 1 ]
    
    a.get_course_remain(course_id,course_sec,"")
    old_json=load()
    if old_json.get(course):
        old_json[course].append(contact_info)
    else:
        old_json[course]=[contact_info]
    store(old_json)
    send_mail(contact_info,"You have successfully subscribe "+course+" , you will receive notification when your requested section is open.")
    
def poll_spot():
    a=api.schedule_api()
    old_json=load()
    for course in old_json:
        ###if open ,send notfication, delete message fuc

        course_id=course.split(" ") [ 0 ]
        course_sec=course.split(" ")[ 1 ]
        new_contact_info=[]
        for y in old_json[course]:
            try:
                remain_num=a.get_course_remain(course_id,course_sec,"")
            except:
                pass
            #if remain =0
            #print(course,remain_num)
            if remain_num != 0:
                send_mail(y,"Your section "+course +" has "+ str(remain_num)+" spots. If you want to keep track this section, please subscribe again" )
                print(y,"has sent")
            else:   
                new_contact_info.append(y)
        
        #assign to to dict
        old_json[course]=new_contact_info
    store(old_json) 
    


def send_mail(receivers, text, sender=SENDER, user_account=USER_ACCOUNT, subject=SUBJECT):
    msg_root = MIMEMultipart()  # 创建一个带附件的实例
    msg_root['Subject'] = subject  # 邮件主题
    msg_root['To'] = receivers  # 接收者
    msg_text = MIMEText(text, 'html', 'utf-8')  # 邮件正文
    msg_root.attach(msg_text)  # attach邮件正文内容

    #smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp = smtplib.SMTP('smtp.163.com', 25)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user_account['username'], user_account['password'])
    smtp.sendmail(sender, receivers, msg_root.as_string())

if __name__ == "__main__":
    print(time.localtime(time.time()).tm_hour)
    send_mail("827142908@qq.com","You have section 31646 opened")
    while True:
        if time.localtime(time.time()).tm_hour >8:
            poll_spot()
            time.sleep(300)
        else:
            poll_spot()
            time.sleep(300)
