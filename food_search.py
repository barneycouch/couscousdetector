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


try:
	food_report = food_report(str(sys.argv[1]))
	if not len(food_report) == 0:
		for k in food_report:
			print "%s is served on:" % k
			for i in food_report[k]:
				print i
	else:
		print "%s isn't being served in the near future!" % str(sys.argv[1])
except:
	print("Please provide the food you don't like:" "\n" """e.g. python food_search.py 'Cous Cous'""")
	quit()