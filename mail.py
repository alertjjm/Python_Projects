import smtplib
from email.mime.text import MIMEText
import time
print('시작')
smtpObj=smtplib.SMTP_SSL('smtp.daum.net', 465)
print('1')
smtpObj.ehlo()
print('2')
smtpObj.login('jongmin9687@daum.net', 'sdr2936735^')
print('로그인 성공')
msg=MIMEText('H~~~^^~~~H')
msg['Subject']='merongmerongmerong'
msg['To']='yeki1234@naver.com'
for i in range(0,500):
    smtpObj.sendmail('jongmin9687@daum.net', 'yeki1234@naver.com', msg.as_string())
    time.sleep(0.1)
    print(i,end='')
    print('성공')
smtpObj.quit()