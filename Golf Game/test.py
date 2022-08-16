from player import *
import random
import time
from operator import attrgetter

#create player objects 
playerlist = []

playerlist.append( Player("Quinn", 0))
playerlist.append( Player("Matt", 0))
playerlist.append( Player("Ed", 0))
playerlist.append( Player("Isaac", 0))

#play golf
def playgolf():
	coursepar = 0
	numberofholes = 1
	while numberofholes < 10:

		#every loop represents one holes of golf played
		print("Hole Number: " + str(numberofholes))
		
		#first we will establish the par of the current hole, for keeping score
		par = random.randint(3,5)
		print("Par for this hole is: " + str(par))

		for golfer in playerlist:
			golferswing = random.randint(2,8)
			print( str(golfer.name) + " took " + str(golferswing) + " to complete the hole ", sep = ' ')
			golferrs = golferswing - par
			golfer.score = golfer.score + golferrs
			print(str(golfer.name) + " shot a " + str(golferrs) + " their score is now" + str(golfer.score))
			#time.sleep(1)
		coursepar = par + coursepar
		numberofholes = numberofholes + 1
	else:
		print("The round has ended.")
		min_attr = min(playerlist, key=attrgetter('score'))
		print('The lowest score was: ' + str(min_attr.name) + ' with a score of: ' + str(min_attr.score))
		print('Total par for the course was: ' + str(coursepar))


playgolf()