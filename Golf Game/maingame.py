from player import *
import random
import time

#create player objects 
player1 = Player("Quinn", 0)
player2 = Player("Matt", 0)
player3 = Player("Ed", 0)
player4 = Player("Isaac", 0)
coursepar = 0

#play golf
def playgolf():
	global coursepar
	numberofholes = 1
	while numberofholes < 19:
		#every loop represents one holes of golf played
		print("Hole Number: " + str(numberofholes))
		
		#first we will establish the par of the current hole, for keeping score
		par = random.randint(3,5)
		print("par for this hole is: " + str(par))

		#-----------------------
		#player1
		#-----------------------

		#then each player will take a turn rolling for a swing. 
		player1swing = random.randint(2,8)
		print(str(player1.name) + ' took ' + str(player1swing) + ' number of strokes to finish the hole')

		#now we will declare a variable to calculate the players score for this round
		player1rs = player1swing - par

		#then use this variable to update the total course score stored in the player object
		player1.score = player1.score + player1rs

		#print to console to show its working
		print(str(player1.name) + " shot a " + str(player1rs) + " their score is now" + str(player1.score))
		
		#-----------------------
		#player 2
		#-----------------------

		player2swing = random.randint(2,8)
		print(str(player2.name) + ' took ' + str(player2swing) + ' number of strokes to finish the hole')
		player2rs = player2swing - par
		player2.score = player2.score + player2rs
		print(str(player2.name) + " shot a " + str(player2rs) + " their score is now" + str(player2.score))

		#-----------------------
		#player 3
		#-----------------------

		player3swing = random.randint(2,8)
		print(str(player3.name) + ' took ' + str(player3swing) + ' number of strokes to finish the hole')
		player3rs = player3swing - par
		player3.score = player3.score + player3rs
		print(str(player3.name) + " shot a " + str(player3rs) + " their score is now" + str(player3.score))

		#-----------------------
		#player 4
		#-----------------------

		player4swing = random.randint(2,8)
		print(str(player4.name) + ' took ' + str(player4swing) + ' number of strokes to finish the hole')
		player4rs = player4swing - par
		player4.score = player4.score + player4rs
		print(str(player4.name) + " shot a " + str(player4rs) + " their score is now" + str(player4.score))

		#loop iteration update
		numberofholes = numberofholes + 1

		#keep track of the total par for the course the players played on
		coursepar = par + coursepar
		time.sleep(1)

	else:
		print("The round has ended.")
		currentwinner = player1.score
		if player2.score < currentwinner:
			currentwinner = player2.score
		if player3.score < currentwinner:
			currentwinner = player3.score
		if player4.score < currentwinner:
			currentwinner = player4.score

		print("scores:" + '\n' + str(player1.name) + " : " + str(player1.score) + '\n' + 
			str(player2.name) + " : " + str(player2.score) + '\n' +
			str(player3.name) + " : " + str(player3.score) + '\n' +
			str(player4.name) + " : " + str(player4.score))

		print('course par:' + str(coursepar))
		print(str(currentwinner))

playgolf()


