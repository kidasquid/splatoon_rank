#!/usr/bin/env python
from random import gauss
from random import randint

# debug level of output
# 0 = summaries
# 1 = show players before and after
# 2 = show individual game results
# progress shows percentage, rounded to 10, for runtime
debuglevel = 0
progress = False

# game stats
rounds = 10000 #rounded down to 10s
playercount = 10000 #players not grouped yet

# proposed change, where 0 is the rank down point
proposal = False

# skill based rounds are
# player skill level of skillspread stdev
# plus a random number of opponentspread stdev
# if the sum is more than the average of the two, 10, the player wins
# more skilled players win more often
# opponentspread greather than 1 represents a sample of players of a specific spread
# rather than whole population of players
skillbased = False
skillspread = 2
opponentspread = 1



# grades dictionary
grades = {
	0:'C-',
	1:'C',
	2:'C+',
	3:'B-',
	4:'B',
	5:'B+',
	6:'A-',
	7:'A',
	8:'A+',
}

winpoints = {
	0:20,
	1:15,
	2:12,
	3:12,
	4:10,
	5:10,
	6:10,
	7:10,
	8:10,
}

class player(object):
	def __init__(self, player_id):
		self.id = player_id
		self.skill = gauss(0, skillspread)
		self.rank = 0
		self.exp = 0
		self.grade = 'C-'

	def __repr__(self):
		return "Player %s, Skill level %s, Rank %s %s" % (self.id, self.skill, self.grade, self.exp)

	def win(self):
		self.exp += winpoints[self.rank]
		if self.exp >= 100:
			self.exp = 30
			self.rank += 1
		if self.rank > 8:
			self.exp = 99
			self.rank = 8
		else:
			self.grade = grades[self.rank]
	def lose(self):		
		self.exp -= 10
		if ( self.exp <= 0 and proposal == True ) or ( self.exp < 0 and proposal == False ):
			self.exp = 70
			self.rank -= 1
		if self.rank < 0:
			self.rank = 0
			self.exp = 0
			self.grade = 'C-'
		else:
			self.grade = grades[self.rank]



print '#############Initializing Players#############'
print

players=[]
for x in range(playercount):
	players.append( player(x) )

if debuglevel >= 1 :
	for x in players:
		print x
else:
	print '%s players' % ( len(players) )


print
print '#################Playing Game#################'
print
print '%s Rounds, %s Total Games' % (rounds/10*10, rounds/10*10*playercount)
print 'Skill Based == %s, 0 Point Rank Down == %s' % (skillbased, proposal) 
if progress == True:
	print

rounds /= 10
wins = 0
loses = 0
for x in range(10*rounds):
	if ( x - 1 ) % rounds-1==0 and progress == True:
		print '%s Percent Done' % (x/rounds*10)
	for p in players:
		opponent = gauss(0, opponentspread)
		if p.skill + opponent >= 0 and skillbased == True:
			p.win()
			wins += 1
			if debuglevel >= 2:
				print p.skill + opponent, 'win'
		elif p.skill + opponent < 0 and skillbased == True:
			p.lose()
			loses += 1
			if debuglevel >= 2:
				print p.skill + opponent, 'lose'


		elif randint(0,1) == 1 and skillbased == False:
			p.win()
			wins += 1
			if debuglevel >= 2:
				print 'random win'
		else:

			p.lose()
			loses += 1
			if debuglevel >= 2:
				print 'random lose'

if debuglevel >= 1 :
	print
	print '############Post-play Players################'
	print

	players = sorted( players, key = lambda player: 
			( player.rank, player.exp, player.skill, player.id ) 		)

	for x in players:
		print x

print
print '##################Summary####################'
print

resultsg = {}
resultsl = {}

for x in range(9):
	resultsg[x]=0

for x in range(1,9,3):
	resultsl[x]=0

for p in players:
	resultsg[p.rank] += 1
	resultsl[ (p.rank//3) *3 +1 ] += 1

print
print 'Wins %s' % wins
print 'Loses %s' % loses
print
print 'Grade Results'
for x in resultsg:
	print grades[x], resultsg[x], round( float(resultsg[x]) / playercount * 100, 0), 'Percent'
print

print 'Letter Results'
for x in resultsl:
	print grades[x], resultsl[x], round( float(resultsl[x]) / playercount * 100, 0), 'Percent'

print
print '####################Done#####################'
print
