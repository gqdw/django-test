#coding:utf-8
import smtplib
from email.mime.text import MIMEText
def sendmail(to,subject,message):
	user='35992656@qq.com' 
	passwd='jgy123qwe'
	#to='332305654@qq.com'
	
	msg=MIMEText(message.encode('utf-8'),'plain','utf-8')
	
	msg["Subject"] = 	subject	
	msg['From']	=	user
	msg['to']	=	to
	print msg.as_string()
	s=smtplib.SMTP('smtp.qq.com')
	s.login(user,passwd)
	s.sendmail(user,to,msg.as_string())
	s.close()


#sendmail('332305654@qq.com',"test","test")
