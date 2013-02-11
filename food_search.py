import urllib, re, sys, datetime
from bs4 import BeautifulSoup

def food_search(food_list):

	html = urllib.urlopen("http://www.caiusmcr.com/uploads/current_menu.htm").read()
	html_menu = BeautifulSoup(html)
	dinnerRow = html_menu.find_all('tr')[3]

	report = {}

	for food in food_list:
		for day in range(0,7):
			dinnerCell = dinnerRow.find_all('td')[day]
			if food in dinnerCell.get_text().lower():
				try:
					report[food].append(day)
				except KeyError:
					report[food] = [day]

	return report

#Converts between day index and actual day
def to_day_string(day_index):

	day = datetime.datetime.today().weekday()
	if day == day_index:
		return "Today"

	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	return days[day_index]


#Builds a report from the input report_dict (from above) and the food the user is interested in
def food_report(food_search_dict, food_list):

	if food_list[0] == '':
		return ''

	day = datetime.datetime.today().weekday()

	report = "<i><b><h3>Your Food:</h3></b></i>"

	for food_item in food_list:
		try:
			occurances = food_search_dict[food_item]
		except KeyError:
			report += "%s isn't being served in the near future.<br /><br />" % food_item.title()
			continue

		#Cull all occurrances which have already happened (or are more than 3 days away)
		futureOccurances = []
		for occurance in occurances:
			if occurance >= day and occurance - 3 < day:
				futureOccurances.append(occurance)

		occurances = futureOccurances

		if len(occurances) == 0:
			report += "%s isn't being served in the near future.<br /><br />" % food_item.title()

		else:
			report += "%s is being served " % food_item.title()

			#If not being served today, need an on ('on' Monday etc)
			if not(day in occurances):
				report += "on "

			for occurance in occurances:
				report += " %s," % to_day_string(occurance)

			#Remove last comma, add a full stop and a line break
			report = report[:-1] + "."
			report += "<br /><br />"

	return report

