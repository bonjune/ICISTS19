import openpyxl
import smtplib
from email.mime.text import MIMEText

#엑셀 데이터 로딩

test = openpyxl.load_workbook(filename = "test.xlsx")
te = test.active
now = test['Sheet1']

# ok = False
# for i in now.rows:
#     if(i[0].value == '#'):
#         ok = True
#         continue
#     if(ok == True):
#         print(i[0].value, i[3].value)

# 메일 전송

me = 'icists@icists.org'
you = 'sk_ans_mc@kaist.ac.kr'

# msg = MIMEText(contents, _charset="UTF-8")
# msg['Subject'] = 'test'
# msg['From'] = me
# msg['To'] = you

#포트 연결 및 암호화
google_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
google_server.ehlo()

#앱 비밀번호는 기기에 맞는 App password를 입력해주어야 함.
google_server.login('bsho0330@gmail.com', 'cfkysjidlmtewsvq')

#메일 전송
first = True
for i in now.rows:
    if(first) :
        first = False
        continue
    contents = i[2].value
    msg = MIMEText(contents, _charset="UTF-8")
    adress = []
    adress.append(i[3].value)
    print(type(i[3].value))
    print(i[3].value)
    msg['Subject'] = '19TD Test Mail'
    msg['From'] = me
    msg['To'] = you
    google_server.sendmail('icists@icists.org', adress, msg.as_string())

#서버 종료
google_server.quit()
