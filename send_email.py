# import smtplib  
  
# fromaddr = 'jthebutler@gmail.com'  
# toaddrs  = 'bc389@cam.ac.uk'  
# subject = 'Oh shit'
# msg = 'There was a terrible error that occured and I wanted you to know!'  
  
  
# # Credentials (if needed)  
# username = 'jthebutler'  
# password = 'jeevesisguessable'  
  
# # The actual mail send  
# server = smtplib.SMTP('smtp.gmail.com:587')  
# server.starttls()  
# server.login(username,password)  
# server.sendmail(fromaddr, toaddrs, msg)  
# server.quit() 

#!/usr/bin/python
import smtplib
 
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
 
sender = 'jthebutler@gmail.com'
password = 'jeevesisguessable'
recipient = 'bc389@cam.ac.uk'
subject = 'Gmail SMTP Test'
body = 'blah blah blah'
 
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