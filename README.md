#Jeeves, the infamous Couscous detector.

##Introduction
Nobody likes couscous, so we built this to email us when it's tragically on the menu. By popular demand it's expanded to tell you when other horrible dishes are avilable, what the daily menu is, if you've booked for hall.

##For the Public
Send an email to `jthebutler@gmail.com` with the foods you don't like in the subject field, separated by commas.

e.g. `Cous Cous, Salad, Pie`

##For the Devs

`send_email.py` sends out the emails to all our subscribed users, calling on `food_search.py` and `get_menu.py` to find that food and retrieve the daily menu.

`receive_email.py` monitors our inbox for new subscribers and their preferences.

`check_bookings.py` will alert a user if they haven't booked in for hall on a particular day.

User preferences and total food tracked are stored in `users.txt` (in the form `user-email,food1,food2`) and `food.txt` (one food per line), both in the `.gitignore` file so not appearing here. If you can't run this script create these first.
