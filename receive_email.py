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
	print ("%s new message." % unreadcount) 	

# Search for all new mail
status, unread_email_ids = imap_server.search(None, '(UNSEEN)')
unread_email_ids = unread_email_ids[0].split(' ')


def get_new_users(email_ids):
    new_users = {}
    unsubscribe_users = []
    for e_id in email_ids:

        #Get sender
        _, response = imap_server.fetch(e_id, '(body[header.fields (from)])')
        fromHeader = (response[0][1][6:])
        matchObj = re.findall('<.*>', fromHeader, re.S)
        sender = matchObj[0].strip('[<>')

        #Get subject text
        _, response = imap_server.fetch(e_id, '(body[header.fields (subject)])')
        subject_text = response[0][1][9:]
        food_items = subject_text.split(",")

        #Check to see if the user wants to unsubscribe
        _, response = imap_server.fetch(e_id, '(UID BODY[TEXT])')
        if 'un' in response[0][1].lower():
            unsubscribe_users.append(sender)

        #Ensure all whitespace is trimmed from food items
        food_itemsT = []
        for item in food_items:
            food_itemsT.append(item.strip())
        food_items = food_itemsT

        new_users[sender] = food_items

    return new_users, unsubscribe_users

#load in all the food we currently scrape for
new_food = []
all_food = ""
try:
    food_txt = open("food.txt", "r")
    all_food = food_txt.read()
    food_txt.close()
except:
    print("Food file not found, creating new.")


#Completely load in all recipients
recipients = {}
try:
    f = open("users.txt", "r")
    for line in f:
        recipient_details = line.split(",")
        user = recipient_details.pop(0)
        recipients[user] = recipient_details
    f.close()
except:
    print("Users file not found, creating new.")

#Set new keys corresponding to new users
new_user_details, unsubscribe_users = get_new_users(unread_email_ids)
for user in new_user_details:
    recipients[user] = new_user_details[user]

    #check for new food
    for food_item in new_user_details[user]:
        if not(food_item in all_food) and not(food_item in new_food):
            new_food.append(food_item)

#Unsubscribe users
for u in unsubscribe_users:
    recipients.pop(u)

#Write back out
f = open("users.txt", "w")
file_string = ""
for user in recipients:
    file_string += user+","
    for food_item in recipients[user]:
        file_string += food_item + ","
    file_string = file_string[:-1]
    file_string += "\n"

f.write(file_string[:-1])
f.close()    

#Write food.txt back out
food_txt = open("food.txt", "a")

for food_item in new_food:
    food_txt.write(food_item + "\n")
food_txt.close()


