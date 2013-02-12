#Jeeves, the infamous Couscous detector.

##Introduction
Nobody likes couscous, so we built this to email us when it's tragically on the menu. By popular demand it's expanded to tell you when other horrible dishes are avilable, and there's more hall amelioration measures in the pipeline.

##Usage

`food_search.py` scrapes the hall menu for specified foods and returns a food report. 'food_search()' does the actual menu scrpaing, whilst 'food_report()' prepares per-user reports.

`get_menu.py` fetches the daily menu, also includes functions to fetch the menu on a specific day (Monday:0, Sunday:6) and to return the unformatted menu.

`receive_email.py` and `send_email.py` check our inbox for new subscribers and send out the email alerts to our mailing list, respectively.

`users.txt` forms our mailing list, holding those unlucky enough to be subscribed to our emails of doom. Also includes their notified foods, with format (per line) "user-email,food1,food2,ect"

`food.txt` includes all the foods we scrape for, to avoid more scraping than needed.