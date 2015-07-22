#!/usr/bin/env python
from random import gauss
from random import randint

debug = False
games = 100000 #rounded down to 10s
playercount = 100

grades={
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

class player(object):
	def __init__(self, player_id):
		self.id = player_id
		self.skill = gauss(1, 5)
		self.rank = 0
		self.exp = 0
		self.grade = 'C-'

	def __repr__(self):
        	return "Player %s, Skill level %s, Rank %s %s" % (self.id, self.skill, self.grade, self.exp)

	def win(self, points):
		self.exp += points
		if self.exp >= 100:
			self.exp = 30
			self.rank += 1
		if self.rank > 8:
			self.exp = 99
			self.rank = 8
		else:
			self.grade = grades[self.rank]
	def lose(self, points):		
		self.exp -= points
		if self.exp < 0:
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

if debug==True:
	for x in players:
		print x
else:
	print '%s players' % ( len(players) )


print
print '#################Playing Game#################'
print '%s Rounds' % (10*games)
print

games /= 10
for x in range(10*games):
	if x % games==0:
		print '%s Percent' % (x/games*10)
	for p in players:
		if randint(0,1)==1:
			p.win(10)
		else:
			p.lose(10)
print '100 Percent'

players=sorted(players, key=lambda player: (player.rank, player.exp, player.id))

if debug==True:
	for x in players:
		print x

print
print '##################Summary####################'
print

results = {}
results2 = {}

for x in range(9):
	results[x]=0

for x in range(1,9,3):
	results2[x]=0

for p in players:
	results[p.rank] += 1
	results2[(p.rank//3)*3+1] += 1

print 'Grade Results'
for x in results:
	print grades[x], results[x]
print

print 'Letter Results'
for x in results2:
	print grades[x], results2[x], float(results2[x])/playercount*100

print
print '####################Done#####################'
