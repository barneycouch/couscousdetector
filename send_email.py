import smtplib, sys
 
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

try:
	sender = str(sys.argv[1])
	password = str(sys.argv[2])
except:
	print("Please provide sender <email> <password> arguments!")
	quit()


subject = 'The CousCous Roundup'
body = 'There is couscous coming on Saturday. Shit the bed.'

body = "" + body + ""
 
recipients = []

f = open("crs_ids.txt", "r")
for line in f:
	recipients.append(line.rstrip())	

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
session.ehlo()
session.starttls()
session.ehlo
session.login(sender, password)

print "\nSending email to:\n"
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
print '\n'