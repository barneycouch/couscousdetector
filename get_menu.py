#fetches the daily menu, also includes functions to fetch the menu on a specific day (Monday:0, Sunday:6) and to return the unformatted menu.
import urllib, datetime, re
from bs4 import BeautifulSoup


#clean up html, make sure no newlines etc
def format_item_string(item):
	return item.replace("\n", "").replace("  ", " ").replace("\r", "").replace(u'\u2019', u'\'').strip()

#don't consider html tags or separators as food
def check_item_string(item):
	return not("Tag" in str(type(item)) or item == "or" or item == " " or item == "" or "(" in item or ")" in item or "contain" in item)


def menu_day(day):

	### Get menu
	html = urllib.urlopen("http://www.caiusmcr.com/uploads/current_menu.htm").read()
	html_menu = BeautifulSoup(html)


	### Get specific row for dinner (could be adapted for lunch at a later date)
	#TODO: Also need to grab veggie option
	dinnerRow = html_menu.find_all('tr')[3]


	### Get actual cell for today and build list of dinner items
	dinnerCell = dinnerRow.find_all('td')[day]

	dinnerItemTags = dinnerCell.find_all('p')
	dinnerItems = []

	for itemTag in dinnerItemTags:
		dinnerItems.append(itemTag.get_text())


	### Create arrays ready for courses, and create bools to track where we're at
	starters = []
	mains = []
	desserts = []

	starters_found = False
	mains_found = False

	### This is where it gets funky
	for item in dinnerItems:

		item = item.encode('ascii', 'ignore')
	
		if not(starters_found):
			if "*" in item:
				starters_found = True
			elif check_item_string(item):
				starters.append(format_item_string(item))
			continue


		if not(mains_found):
			if "*" in item:
				mains_found = True
			elif check_item_string(item):
				mains.append(format_item_string(item))
			continue

		if check_item_string(item):
			desserts.append(format_item_string(item))


	#Get veggie option (if not saturday)
	if not(day == 5):
		veggieRow = html_menu.find_all('tr')[4]
		veggieCell = veggieRow.find_all('td')[day]
		veggieString = format_item_string(veggieCell.find_all('p')[2].get_text()) + "(V)"

		#Shove it into the mains array
		mains = mains + [veggieString]


	if day == 5:
		return {"mains" : starters + mains, "dessert" : desserts} #Saturday formatiing
	else:
		return {"starters" : starters, "mains" : mains, "dessert" : desserts}


def menu_today():
	return menu_day(datetime.datetime.today().weekday())		

def formatted_menu_day(day):
	menu = menu_day(day)

	#Build output string
	output = "<b><i><h3>The Menu Today:</h3></i></b>"

	if "starters" in menu:
		output += "<b>Starters</b><br />"
		for item in menu['starters']:
			output += item + "<br />"
		output += "<br />"
	
	output += "<b>Mains</b><br />"
	for item in menu['mains']:
		output += item + "<br />"

	output += "<br /><b>Dessert</b><br />"
	for item in menu['dessert']:
		output += item + "<br />"

	return output

def formatted_menu_today():
	return formatted_menu_day(datetime.datetime.today().weekday())