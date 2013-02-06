#Jeeves, the infamous Couscous detector.

##Introduction
Nobody likes couscous, so we built this to email us when it's tragically on the menu. By popular demand it's expanded to tell you when other horrible dishes are avilable, and there's more hall amelioration measures in the pipeline.

##Usage

`food_search.py` scrapes the hall menu for our hated foods, provided as an argument. So `python food_search.py "Soup"` will return a list of the days the dreaded Soup is due.

`get_menu.py` fetches the daily menu, also includes functions to fetch the menu on a specific day (Monday:0, Sunday:6) and to return the unformatted menu.

`receive_email.py` and `send_email.py` check our inbox for new subscribers and send out the email alerts to our mailing list, respectively.

`crs_ids.txt` forms our mailing list, holding those unlucky enough to be subscribed to our emails of doom.

`main.py` calls the other scripts, with `crsid`, `crs password` (both currently unused), `email`, `password` arguments.