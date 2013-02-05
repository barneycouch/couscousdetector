import urllib, re, sys
from bs4 import BeautifulSoup

try:
	hatedfood = str(sys.argv[1]).title()  #.title() capitalises first letter, as used by the menu system
except:
	print("Please provide the food you don't like:" "\n" """e.g. python food_search.py 'Cous Cous'""")
	quit()	

hallsoup = BeautifulSoup(urllib.urlopen("http://caiusjcr.co.uk/hall").read())

def find_menu(soup):
	return soup.find_all('td', class_=re.compile('col*'))

food_occurrences = {}

for i in find_menu(hallsoup):
	try:
		if hatedfood in str(i):
			occurence = str(i.find_all('h2')[0].find_all('a')[0].string)
			#thanks for the next line http://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-python-dictionary
			try:
				food_occurrences[hatedfood].append(occurence)
			except KeyError:
				food_occurrences[hatedfood] = [occurence]
	except:
		print("")


for k in food_occurrences:
	print "%s is served on:" % k
	for i in food_occurrences[k]:
		print i