#!/usr/bin/env python
#-*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
def mail(messageToSend, mailProf):

	fromaddr = "embesystem@gmail.com"
	toaddr = mailProf
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "La liste des absents du #date"
	 
	body = messageToSend
	msg.attach(MIMEText(body, 'plain'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "embedded2018")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
#mail('Hello World', 'corentin.lefor@gmail.com')
