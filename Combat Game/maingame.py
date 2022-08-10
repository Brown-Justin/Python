from player import *
import random

player1 = Player("Quinn", 100)
player2 = Player("Justin", 100)

player2.sayhi()
player1.sayhi()

def combat():
	player1attack = random.randint(0,10)
	print(str(player1.name) + ' just hit for '+ str(player1attack))
	player2attack = random.randint(0,10)
	print(str(player2.name) + ' just hit for '+ str(player2attack))

	player1.health = player1.health - player2attack
	print(str(player1.name) +' health = ' + str(player1.health))
	player2.health = player2.health - player1attack
	print(str(player2.name) +' health = ' + str(player2.health))

while (player1.health > 0 and player2.health > 0):
	combat()
else:
	print('combat is done')
