#A sweary couscous detector in 8 lines of Python.
import urllib, re, sys
from bs4 import BeautifulSoup

try:
	hatedfood = str(sys.argv[1])
except:
	print("Please provide the food you don't like:" "\n" """e.g. python couscous_mk2.py 'Cous Cous'""")
	quit()	

hallsoup = BeautifulSoup(urllib.urlopen("http://caiusjcr.co.uk/hall").read())

def find_menu(soup):
	return soup.find_all('td', class_=re.compile('col*'))

for i in find_menu(hallsoup):
	try:
		if hatedfood in str(i):
			print("""The fucking %s is coming on %s, so don't book fucking hall then.\n""") % (hatedfood, i.find_all('h2')[0].find_all('a')[0].string)
		else:
			print("""All is clear on %s.\n""") % i.find_all('h2')[0].find_all('a')[0].string
	except:
		print("")



##Maybe I can do it functionally? Fuck that, it's 3:55am.


# def find_couscous(menu_html):
# 	if 'Cous' in str(menu_html):
# 		return menu_html.find_all('h2')[0].find_all('a')[0].string


# print map(find_couscous, find_menu(hallsoup))