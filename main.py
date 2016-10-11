import requests
from BeautifulSoup import BeautifulSoup
import datetime

today = datetime.datetime.today().strftime('%Y-%m-%d')
format = 'modern' 
url = 'http://magic.wizards.com/en/articles/archive/mtgo-standings/competitive-' + format +'-constructed-league-' + str(today)

class Deck:
	def __init__(self):
		self.main = []
		self.side = []
		self.archetype = 'unknown'
		
	def addToMain(self, card):
		self.main.append(card)
		
	def addToSide(self, card):
		self.side.append(card)
	
	def printDeck(self):
		print 'Deck: ' + self.archetype
		print 'Main'
		for card in self.main:
			print card.getQuantity() + ' ' + card.getName()
		print 'Side'
		for card in self.side:
			print card.getQuantity() + ' ' + card.getName()
	
class Card:
	def __init__(self):
		self.name = 'unknown'
		self.quantity = 0
		self.color = 'unknown'
		self.subtype = 'unknown'
		
	
	def setName(self, name):
		self.name = name
		
	def setQuantity(self, quantity):
		self.quantity = quantity
		
	def setColor(self, color):
		self.color = color	
		
	def setSubType(self, subtype):
		self.subtype = subtype
	
	def getSubType(self):
		return self.subtype
	
	def getName(self):
		return self.name
	
	def getQuantity(self):
		return self.quantity
		

def getDecks(url):
	deckbox = []
	response = requests.get(url)
	html = response.content

	soup = BeautifulSoup(html)
	decklists = soup.findAll('div', {'class':['deck-list-text']})

	i = 0
	for item in decklists:
		d = Deck()
		main = item.find('div', {'class':['sorted-by-overview-container sortedContainer']})
		side = item.find('div', {'class':['sorted-by-sideboard-container  clearfix element']})
		#find all the cards in the main deck

		for card in main.findAll('span', {'class':['row']}):
			c = Card()
			c.setQuantity(card.find('span', {'class':['card-count']}).text)
			c.setName(card.find('span', {'class':['card-name']}).text)
			d.addToMain(c)
		#find all the cards in the sideboard
		for card in side.findAll('span', {'class':['row']}):
			c = Card()
			c.setQuantity(card.find('span', {'class':['card-count']}).text)
			c.setName(card.find('span', {'class':['card-name']}).text)
			d.addToSide(c)
		d.printDeck()
		print ''
		i += 1


#%%%%%%%%%%%%%%%%%%%%%%%%#
# START OF MAIN SCRIPT
#%%%%%%%%%%%%%%%%%%%%%%%%#

getDecks(url)


