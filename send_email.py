import smtplib, sys, re
from get_menu import formatted_menu_today
from food_search import food_report, food_search


def send_roundups():

	#Get today's menu
	menu = formatted_menu_today()

	#Build food search
	food = []
	try:
		f = open("food.txt", "r")
		for line in f:
			food.append(line.rstrip())
	except:
		print("No food found.")

	food_search_dict = food_search(food)

	#Get recipients
	recipient_strings = []
	try:
		f = open("users.txt", "r")
		for line in f:
			recipient_strings.append(line.rstrip())
	except:
		print("No users found, qutting.")
		quit()

	recipients = {}
	for r in recipient_strings:

		recipient_details = r.split(',')
		user = recipient_details.pop(0)

		for food_item in recipient_details:
			try:
				recipients[user].append(food_item)
			except KeyError:
				recipients[user] = [food_item]

	#Send emails
	subject = "The Food Roundup"
	sender = "Jeeves <jthebutler@gmail.com>"
	session = open_session()

	for r in recipients:
		user_food_report = food_report(food_search_dict, recipients[r])

		headers = ["From: " + sender, "Subject: " + subject, "To: " + r, "MIME-Version: 1.0","Content-Type: text/html"]

		body = "Here's your food roundup!<br>" + user_food_report + menu + "<br /><br /><i>- Jeeves</i><br /><br /><br /><br />(To unsubscribe, send an email to jthebutler@gmail.com with 'unsubscribe' in the message)"

		headers = "\r\n".join(headers)
		session.sendmail(sender, r, headers + "\r\n\r\n" + body)

	session.quit()


def open_session():
	SMTP_SERVER = 'smtp.gmail.com'
	SMTP_PORT = 587

	try:
		sender = str(sys.argv[1])
		password = str(sys.argv[2])
	except:
		print("Please provide <gmail username> <password> arguments!")
		quit()

	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	 
	session.ehlo()
	session.starttls()
	session.ehlo
	session.login(sender, password)

	return session

send_roundups()