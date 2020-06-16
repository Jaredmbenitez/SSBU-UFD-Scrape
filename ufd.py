# UFD SCRAPE 

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup




main_page_url = 'https://ultimateframedata.com'
myClient = uReq(main_page_url)
main_page_html = myClient.read()
myClient.close()
main_page_soup = soup(main_page_html, "html.parser")
#####################################################################

subs = input('Enter a character name: ')

character_name_list = main_page_soup.findAll("div",{"class": "charactericon"})
hrefList = [i.a['href'] for i in character_name_list]	## list of all '\chrom.php, \pacman.php, etc'
newList = [j for j in hrefList if subs in j]	## contains a list of elements containing our substring

print(newList)





##################################CHARACTER PAGE SECTION ##########################
character_url = "https://ultimateframedata.com" + newList[0]
Client = uReq(character_url)
character_page_html = Client.read()
Client.close()
character_page_soup = soup(character_page_html, "html.parser")

###################################################################################









def printCharInfo(urlName):

	Move_Container = character_page_soup.findAll("div", {"class": "movecontainer"})
	
	for move in Move_Container:
		
		
		print("Move Name:" , move.select(".movename")[0].text.strip())#Other: move.select(."movename")

		if move.select('.startup'):
			print("Startup Frames: ",move.select(".startup")[0].text.strip())
		if move.select('.totalframes'):
			print("Total Frames: ",move.select(".totalframes")[0].text.strip())
		if move.select('.activeframes'):
			print("Active Frames: " ,move.select(".activeframes")[0].text.strip())

		if move.select('.landinglag'):
			print("Landing Lag: ", move.select(".landinglag")[0].text.strip())


		if move.select('.basedamage'):
			print("Base Damage: ", move.select(".basedamage")[0].text.strip(), '%')


		if move.select('.shieldlag'):	# Other : if move.find('shieldstun')!= None :	
			print("Sheild Lag: ",move.select(".shieldlag")[0].text.strip())	
		if move.select('.shieldstun'):	
			print("Shield Stun: ",move.select(".shieldstun")[0].text.strip())
		if move.select('.advantage'):
			print("Shield Advantage: ",move.select(".advantage")[0].text.strip())
		print ("-----------------------------------------------------------")

		

printCharInfo(character_url)


#CharList = main_page_soup.findAll("div", {"class": "charactericon"})		#grabs 83 "character classes" (1 is "stats")

#for l in CharList:				# this will display what we need to concat to the end of our original HTML link.
	#print (l.a['href'])

