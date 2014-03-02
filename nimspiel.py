from random import randint

class Player:
	
	number = -1

	def __init__(self, number):
		self.number = number

	def draw(self, game):
		x = game.sticks

		d = randint(1,3)
		if (x-1)%4==0:
			d=1
		elif (x-2)%4==0:
			d=2
		elif (x-3)%4==0:
			d=3
		print("Spieler " + `self.number` + " zieht " + `d`)
		game.draw(d)
		

class NimSpiel:

	sticks = 0
	maxPlayer = None
	minPlayer = None
	currentPlayer = None

	def __init__(self, numberOfSticks, minPlayer, maxPlayer):
		self.sticks = numberOfSticks
		self.minPlayer = minPlayer
		self.maxPlayer = maxPlayer
		self.currentPlayer = maxPlayer

	def draw(self, drawSticks):
		self.sticks-=drawSticks

	def switchPlayer(self):
		if self.currentPlayer is self.maxPlayer:
			self.currentPlayer = self.minPlayer
		else:
			self.currentPlayer = self.maxPlayer

	def nextRound(self):
		
		self.currentPlayer.draw(self)
		
		if self.sticks==0:
			print("Spieler " + `self.currentPlayer.number` + " gewinnt.")
			return False

		self.switchPlayer()
		return True	
	
	def printSticks(self):
		print("Es verbleiben " + `self.sticks` + " Streichhoelzer")

print("Hello, Nimmspiel!")
player1 = Player(1)
player2 = Player(2)
game = NimSpiel(401, player2, player1)

while (game.nextRound()):
	game.printSticks()
	
	


