#Jeeves, the infamous Couscous detector.

##Introduction
Nobody likes couscous, so we built this to email us when it's tragically on the menu. By popular demand it'll tell you when other horrible dishes are available.

##Usage

`couscous.py` scrapes the hall menu for our hated foods, provided as an argument. So `python couscous.py "Soup"` will return a list of the days the dreaded Soup is due.

`receive_email.py` and `send_email.py` check our inbox for new subscribers and provide and alternate (not currently used) way to send out the email alerts, respectively.

`users.txt` holds those unlucky enough to be subscribed to our emails of doom.