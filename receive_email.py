# cheers http://bitsofpy.blogspot.co.uk/2010/05/python-and-gmail-with-imap.html

import imaplib, sys
import re

#try to log on with arguments given
try:
    username = str(sys.argv[1])
    password = str(sys.argv[2])
except:
    print("Please provide <gmail username> <password> arguments!")
    quit()
imap_server = imaplib.IMAP4_SSL("imap.gmail.com",993)
try:
    imap_server.login(username, password)
except:
    print("Incorrect login details!")
    quit()

imap_server.select('INBOX')

# Count the unread emails
status, response = imap_server.status('INBOX', "(UNSEEN)")
unreadcount = int(response[0].split()[2].strip(').,]'))

#If there aren't any new emails, get the fuck out of there
if unreadcount == 0:
	print "No new mail! Quitting."
	quit()
else:
	print ("%s new message from:" % unreadcount) 	

# Search for all new mail
status, unread_email_ids = imap_server.search(None, '(UNSEEN)')

def get_from(email_ids):
    fromlist = []
    for e_id in email_ids:
        _, response = imap_server.fetch(e_id, '(body[header.fields (from)])')
        fromHeader = (response[0][1][6:])
        matchObj = re.findall('<.*@', fromHeader, re.S)        
        sender = matchObj[0].strip('[@<')
        fromlist.append(sender)
    return fromlist   

if len(unread_email_ids) != 0:
	for email in get_from(unread_email_ids):		
            with open("crs_ids.txt", "a") as f:
                f.write("\n"+email)
                print (email+" added successfully")

