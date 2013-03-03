#hat tip to http://stockrt.github.com/p/handling-html-forms-with-python-mechanize-and-BeautifulSoup/

import mechanize, cookielib, datetime, sys, re
from bs4 import BeautifulSoup

from send_email import send_email

def check_bookings(crsid, password):

	#initialise browser, set options
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	#br.set_handle_gzip(True) 		in tutorial, but throws an 'experimental' error
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	#open Raven and auth against user
	br.open('https://raven.cam.ac.uk/auth/login.html')
	br.select_form(nr=0)
	br.form['userid'] = crsid
	br.form['pwd'] = password
	br.submit()

	#go get the hall bookings
	br.open('http://www.mealbookings.cai.cam.ac.uk/')
	html = br.response().read()
	soup = BeautifulSoup(html)
	bookingrow = soup.find_all('tr')
	bookings = {}
	for i in bookingrow:
		if "View/Edit" in str(i):
			date = str(i.find_all('td')[0].string)
			date = re.sub("  ", " ", date) #remove double space from date string
			bookingtype = str(i.find_all('td')[1].string)
			bookings[date] = bookingtype

	#go fetch the current dates (today and tomorrow for now)
	#hat tip to http://stackoverflow.com/questions/904928/python-strftime-date-without-leading-0 for stripping 
	today = datetime.date.today().strftime("%A %-d %B %Y")
	tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%A %-d %B %Y")


	#make an alert message - a bit ugly but it works
	msgout = ""
	if today in bookings.keys():
		msgout += "You're booked in for " + bookings[today] + " today." + '\n'
	else:
		msgout += "Book in for today urgently!" +'\n'

	if tomorrow in bookings.keys():
		msgout += "You're booked in for " + bookings[tomorrow] + " tomorrow."
	else:
		msgout += "Book in for tomorrow!"
	return msgout


if len(sys.argv) != 3:
	print('Please provide <crsid> <password> arguments!')
	quit()

bookingsmessage = check_bookings(sys.argv[1], sys.argv[2])
print bookingsmessage

send_email('bc389@cam.ac.uk', "Bookings Status", bookingsmessage)