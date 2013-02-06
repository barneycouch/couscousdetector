import urllib, datetime, re
from bs4 import BeautifulSoup

def format_item_string(item):
	return item.replace("\n", "").replace("  ", " ").replace("\r", "").replace(u'\u2019', u'\'').encode('ascii', 'ignore')

def menu_today():
	return menu_day(datetime.datetime.today().weekday())

def menu_day(day):

	### Get menu
	html = urllib.urlopen("http://www.caiusmcr.com/uploads/current_menu.htm").read()
	html_menu = BeautifulSoup(html)


	### Get specific row for dinner (could be adapted for lunch at a later date)
	#TODO: Also need to grab veggie option
	dinnerRow = html_menu.find_all('tr')[3]


	### Get actual cell for today and build list of dinner items
	dinnerCell = dinnerRow.find_all('td')[day]

	dinnerItemTags = dinnerCell.find_all('span')
	dinnerItems = []

	for itemTag in dinnerItemTags:
		dinnerItems.append(itemTag.contents[0])


	### Create arrays ready for courses, and create bools to track where we're at
	starters = []
	mains = []
	desserts = []

	starters_found = False
	first_starter_found = False # Needed as 'veg cous cous' is stupidly spaced over two spans
	mains_found = False


	### This is where it gets funky
	for item in dinnerItems:

		if not(starters_found):
			if "*" in item:
				starters_found = True
			elif item == "or":
				first_starter_found = True
				starters.append("")
			elif not("Tag" in str(type(item))):
				if first_starter_found:
					starters[2] = starters[2] + format_item_string(item)
				else:
					starters.append(format_item_string(item))
			continue


		if not(mains_found):
			if "*" in item:
				mains_found = True
			elif not("Tag" in str(type(item)) or " or " in item or item == " "):
				mains.append(format_item_string(item))
			continue

		if not("Tag" in str(type(item))):
			desserts.append(format_item_string(item))

	if day == 5:
		return {"mains" : starters + mains, "dessert" : desserts} #Saturday formatiing
	else:
		return {"starters" : starters, "mains" : mains, "dessert" : desserts}

def formatted_menu_today():
	return formatted_menu_day(datetime.datetime.today().weekday())

def formatted_menu_day(day):
	menu = menu_day(day)

	#Build output string
	output = "<br /><b><i>The Menu Today:</i></b><br /><br />"

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
