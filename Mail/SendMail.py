import openpyxl
import smtplib
from email.mime.text import MIMEText
import pdb

#### check before running
excelname= "contents.xlsx"
userid = 'media@icists.org'
userpw = 'icistsmed2005'

#read excel file
excelf = openpyxl.load_workbook(filename= excelname)
excel = excelf.active

sheet = excelf['Sheet1']

google_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
google_server.ehlo()
google_server.login(userid, userpw)


#line[#, txt format number, mail address, subject, argument)
for line in sheet.rows:
    if line[0].value == '#' or line[1].value==None:
        continue
    
    with open('mail%s.txt'%(str(line[1].value)), 'r') as f:
        contents = f.read()
    
    args = line[4].value.split(',')
    
    if len(args) != contents.count('[]'):
        print("Error with count of argument!! There are %d in txt but there are %d arguments in xlsx\nCheck %s's arguments"%(len(args), contents.count('[]'),line[2].value))
        continue

    for arg in args:
        contents = contents.replace('[]', arg.lstrip(), 1)

    recipients = line[2].value

msg= MIMEText(contents, _charset = 'UTF-8')
msg['Subject'] = line[3].value
msg['To'] = recipients

print('Email Preview')
print('Subject : %s'%msg['Subject'])
print('From: %s'%userid)
print('To: %s'%recipients)
print('Contents:\n%s'%contents)

chk = input("Check and sending email! Is it alright?(yes or no)")
if chk.lower() == 'yes':
    google_server.sendmail(userid, [recipients], msg.as_string())


'''
    msg = MIMEText(contents, _charset= 'UTF-8')
    #contents -> body of mail
    msg['Subject'] -> title of mail
    msg['From'] -> cannot see in email
    msg['To'] -> seeing in mail
    
    google_server.sendmail(id, address, msg.as_string()) -> id : not using, address -> get mail , msg -> header of mail)
    '''
