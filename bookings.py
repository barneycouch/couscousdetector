from bs4 import BeautifulSoup

html = open("bookings_example.html").read()

soup = BeautifulSoup(html)

for i in soup.find_all('tr'):
	if "View/Edit" in str(i):
		print i
		print '\n'