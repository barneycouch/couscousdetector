import urllib, re, sys
from bs4 import BeautifulSoup

def get_cli_input():
	try:
		food = str(sys.argv[1]).title()  #.title() capitalises first letter, as used by the menu system
	except:
		print("Please provide the food you don't like:" "\n" """e.g. python food_search.py 'Cous Cous'""")
		quit()
	return food

sysarg = get_cli_input()

def find_menu():
	hallsoup = BeautifulSoup(urllib.urlopen("http://caiusjcr.co.uk/hall").read())
	return hallsoup.find_all('td', class_=re.compile('col*'))

#print find_menu(sysarg)

def food_occurrences(menu, food):
	occurrences = {}
	for i in menu:
		try:
			if food in str(i):
				occurrence = str(i.find_all('h2')[0].find_all('a')[0].string)
				#thanks for the next line http://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-python-dictionary
				try:
					occurrences[food].append(occurrence)
				except KeyError:
					occurrences[food] = [occurrence]
		except:
			print("")
	return occurrences

food_dict = food_occurrences(find_menu(), sysarg)


#anyway to get this last line functional? I know there's a map in there somewhere
for k in food_dict:
	print "%s is served on:" % k
	for i in food_dict[k]:
		print i