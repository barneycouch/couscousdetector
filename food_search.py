import urllib, re, sys
from bs4 import BeautifulSoup

def food_report(food):

	food = food.title() #Caius Menu Always Capitalised
	
	htmlmenu = BeautifulSoup(urllib.urlopen("http://caiusjcr.co.uk/hall").read())
	hallsoup = htmlmenu.find_all('td', class_=re.compile('col*'))

	occurrences = {}
	for i in hallsoup:
		if food in str(i):
			occurrence = str(i.find_all('h2')[0].find_all('a')[0].string)
			#thanks for the next line http://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-python-dictionary
			try:
				occurrences[food].append(occurrence)
			except KeyError:
				occurrences[food] = [occurrence]
	return occurrences		


def pretty_food_report(food):
	pretty_message = "" #form the string that the message will consist of
	occurrences = food_report(food)
	if not len(occurrences) == 0:
		for k in occurrences:
			served = "%s is being served on:" % k
			pretty_message += (served + "\n")
			for i in occurrences[k]:
				pretty_message += (i + "\n")
	else:
		notserved = "%s isn't being served in the near future!" % str(food)
		pretty_message += notserved
	return pretty_message.replace("\n","<br />") + "<br />"