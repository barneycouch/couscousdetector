# cheers http://bitsofpy.blogspot.co.uk/2010/05/python-and-gmail-with-imap.html

import imaplib
import re

username = "jthebutler"
password = "jeevesisguessable"

imap_server = imaplib.IMAP4_SSL("imap.gmail.com",993)
imap_server.login(username, password)

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
		print email