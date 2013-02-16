#a barebones email send function

import smtplib, sys, re

def send_email(recipient, subject, body):

	SMTP_SERVER = 'smtp.gmail.com'
	SMTP_PORT = 587
	 
	sender = 'jthebutler@gmail.com'
	password = 'jeevesisguessable'
	recipient = recipient
	subject = subject
	body = body

	 
	headers = ["From: " + sender,
	           "Subject: " + subject,
	           "To: " + recipient,
	           "MIME-Version: 1.0",
	           "Content-Type: text/html"]
	headers = "\r\n".join(headers)
	 
	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	 
	session.ehlo()
	session.starttls()
	session.ehlo
	session.login(sender, password)
	 
	session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
	session.quit()