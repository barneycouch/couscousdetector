import smtplib, sys, re
from get_menu import formatted_menu_today
from food_search import food_report, food_search


def send_roundups():

	#Get today's menu
	menu = formatted_menu_today()

	#Build food search
	food = []
	f = open("food.txt", "r")
	for line in f:
		food.append(line.rstrip())

	food_search_dict = food_search(food)

	#Get recipients
	recipient_strings = []
	f = open("crs_ids.txt", "r")
	for line in f:
		recipient_strings.append(line.rstrip())

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
		cam_email_full = r + "@cam.ac.uk"
		user_food_report = food_report(food_search_dict, recipients[r])

		headers = ["From: " + sender, "Subject: " + subject, "To: " + cam_email_full, "MIME-Version: 1.0","Content-Type: text/html"]

		body = "Here's your food roundup!<br>" + user_food_report + menu + "<br /><i>- Jeeves</i>"

		headers = "\r\n".join(headers)
		session.sendmail(sender, cam_email_full, headers + "\r\n\r\n" + body)

	session.quit()


def open_session():
	SMTP_SERVER = 'smtp.gmail.com'
	SMTP_PORT = 587

	sender = "jthebutler@gmail.com"
	password = "########"

	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	 
	session.ehlo()
	session.starttls()
	session.ehlo
	session.login(sender, password)

	return session

send_roundups()
