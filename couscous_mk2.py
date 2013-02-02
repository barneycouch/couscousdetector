#A sweary couscous detector in 8 lines of Python.
import urllib, re
from bs4 import BeautifulSoup


hallsoup = BeautifulSoup(urllib.urlopen("http://caiusjcr.co.uk/hall").read())

def find_menu(soup):
	return soup.find_all('td', class_=re.compile('col*'))

for i in find_menu(hallsoup):
	try:
		if 'Cous' in str(i):
			print("""the fucking couscous is coming on %s, so don't book fucking hall then.\n""") % i.find_all('h2')[0].find_all('a')[0].string
		else:
			print("""all is clear on %s.\n""") % i.find_all('h2')[0].find_all('a')[0].string
	except:
		print("")



##Maybe I can do it functionally? Fuck that, it's 3:55am.


# def find_couscous(menu_html):
# 	if 'Cous' in str(menu_html):
# 		return menu_html.find_all('h2')[0].find_all('a')[0].string


# print map(find_couscous, find_menu(hallsoup))