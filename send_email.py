import smtplib, sys, re

def send_email_to_list(body):

	SMTP_SERVER = 'smtp.gmail.com'
	SMTP_PORT = 587

	try:
		sender = "jthebutler@gmail.com"
		password = "jeevesisguessable"
	except:
		print("Please provide sender <email> <password> arguments!")
		quit()


	subject = 'The Food Roundup'

	body = "Here's your food roundup!<br><br>" + body + "<br>-Jeeves"

	recipients = []

	f = open("crs_ids.txt", "r")
	for line in f:
		recipients.append(line.rstrip())	

	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	 
	session.ehlo()
	session.starttls()
	session.ehlo
	session.login(sender, password)

	print "Sending email to:"

	for i in recipients:
		cam_email_full = str(i + "@cam.ac.uk")
		print cam_email_full
		headers = ["From: " + sender,
	           "Subject: " + subject,
	           "To: " + cam_email_full,
	           "MIME-Version: 1.0",
	           "Content-Type: text/html"]
		headers = "\r\n".join(headers)
		session.sendmail(sender, cam_email_full, headers + "\r\n\r\n" + body)
	session.quit()
	# print '\n'