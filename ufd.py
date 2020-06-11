# UFD SCRAPE 

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'ultimateframedata.com' #note we can concatenate the /wario.php to the end of this to get a new URL for a char

Client = uReq(my_url)
home_page_html = Client.read()
Client.close()
main_page_soup = soup(home_page_html, "html.parser") # HTML PARSER


CharList = page_soup.findAll("div", {"class": "charactericon"})		#grabs 83 "character classes" (1 is "stats")

for l in CharList:				# this will display what we need to concat to the end of our original HTML link.
	print (l.a['href'])

