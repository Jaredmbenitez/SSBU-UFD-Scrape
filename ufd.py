# UFD SCRAPE 

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup







my_url = input("Copy/Paste a character page link (ex 'https://ultimateframedata.com/chrom.php  '): \n")
Client = uReq(my_url)
character_page_html = Client.read()
Client.close()
character_page_soup = soup(character_page_html, "html.parser")






def printCharInfo(urlName):

	Move_Container = character_page_soup.findAll("div", {"class": "movecontainer"})

	for move in Move_Container:

		print("Move Name:" , move.find("div",{"class": "movename"}).text.strip())#Other: move.select(."movename")

		if move.select('.startup'):
			print("Startup Frames: ",move.find("div",{"class": "startup"}).text.strip())
		if move.select('.totalframes'):
			print("Total Frames: ",move.find("div",{"class": "totalframes"}).text.strip())
		if move.select('.activeframes'):
			print("Active Frames: " ,move.find("div",{"class": "activeframes"}).text.strip())

		if move.select('.landinglag'):
			print("Landing Lag: ", move.find("div",{"class": "landinglag"}).text.strip())


		if move.select('.basedamage'):
			print("Base Damage: ", move.find("div",{"class": "basedamage"}).text.strip(), '%')


		if move.select('.shieldlag'):	# Other : if move.find('shieldstun')!= None :	
			print("Sheild Lag: ", move.find("div",{"class": "shieldlag"}).text.strip())	
		if move.select('.shieldstun'):	
			print("Shield Stun: ",move.find("div",{"class": "shieldstun"}).text.strip())
		if move.select('.advantage'):
			print("Shield Advantage: ",move.find("div",{"class": "advantage"}).text.strip())
		print ("-----------------------------------------------------------")



printCharInfo(my_url)
#CharList = main_page_soup.findAll("div", {"class": "charactericon"})		#grabs 83 "character classes" (1 is "stats")

#for l in CharList:				# this will display what we need to concat to the end of our original HTML link.
	#print (l.a['href'])

