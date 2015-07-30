#!/usr/bin/env python
from random import gauss

# debug level of output
# 0 = summaries
# 1 = show players before and after
# 2 = show individual game results
debuglevel = 0

# game stats
rounds = 10000 #games each player plays
playercount = 10000 #players not grouped yet

# proposed change, where 0 is the rank down point
proposal = False

# skill based rounds are
# player skill level of skillspread stdev
# plus a random number of opponentspread stdev
# if the sum is more than the average of the two, 0, the player wins
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
	9:'S',
	10:'S+',}
letters = {
	1:'C',
	4:'B',
	7:'A',
	10:'S',}
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
	9:8,
	10:8,
}

class player(object):
	def __init__(self, player_id):
		self.id = player_id
		if skillbased == True:
			self.skill = gauss(0, skillspread)
		else:
			self.skill = 0
		self.rank = 0
		self.exp = 0
		self.grade = 'C-'

	def __repr__(self):
		return "Player %s, Skill level %s, Rank %s %s" % (self.id, self.skill, self.grade, self.exp)

	def win(self, modifier=0):
		self.exp += winpoints[self.rank] + modifier
		if self.exp >= 100:
			self.exp = 30
			self.rank += 1
		if self.rank == 11:
			self.exp = 99
			self.rank = 10
		self.grade = grades[self.rank]

	def lose(self, modifier=0):		
		self.exp -= 10 + modifier
		if self.exp < 0 or ( self.exp == 0 and proposal == True ):
			self.exp = 70
			self.rank -= 1
		if self.rank < 0:
			self.rank = 0
			self.exp = 0
			self.grade = 'C-'
		self.grade = grades[self.rank]


print
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
print '%s Rounds, %s Total Games' % (rounds, rounds*playercount)
print 'Skill Based == %s, 0 Point Rank Down == %s' % (skillbased, proposal) 

wins = 0
loses = 0
for x in range(rounds):
	for p in players:
		opponent = gauss(0, opponentspread)
		if p.skill + opponent > 0:
			p.win()
			wins += 1
			if debuglevel >= 2:
				print p.skill + opponent, 'win'
		else:
			p.lose()
			loses += 1
			if debuglevel >= 2:
				print p.skill + opponent, 'lose'

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

for x in range(11):
	resultsg[x]=0

for x in range(1,11,3):
	resultsl[x]=0

for p in players:
	resultsg[p.rank] += 1
	resultsl[ (p.rank//3) *3 +1 ] += 1

print
print 'Wins %s' % wins
print 'Loses %s' % loses
print
print 'Grade Results'
print 'Letter	Count	Percent'
for x in sorted(key for (key,value) in resultsg.items()):
	print '	'.join(map(str,[ grades[x], resultsg[x], round(float(resultsg[x]) / playercount * 100., 2) ]))+'%'
print

print 'Letter Level Results'
print 'Letter	Count	Percent'
for x in sorted(key for (key,value) in resultsl.items()):
	print '	'.join(map(str,[ letters[x], resultsl[x], round(float(resultsl[x]) / playercount * 100., 2) ]))+'%'

print
print '####################Done#####################'
print
