import smtplib, sys
 
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

try:
	sender = str(sys.argv[1])
	password = str(sys.argv[2])
	recipient = str(sys.argv[3])
except:
	print("Please provide <sender email> <password> arguments!")
	quit()


subject = 'The CousCous Roundup'
body = 'There is couscous coming on Saturday. Shit the bed.'
 
"Sends an e-mail to the specified recipient."
 
body = "" + body + ""
 
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