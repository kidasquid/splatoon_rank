# splatoon_rank
A Monte Carlo simulator for the Splatoon Rank System

Usage:

    python splatoon_rank.py

Sample output:


	#############Initializing Players#############
	
	10000 players
	
	#################Playing Game#################
	
	10000 Rounds, 100000000 Total Games
	Skill Based == False, 0 Point Rank Down == False
	
	##################Summary####################
	
	
	Wins 49996021
	Loses 50003979
	
	Grade Results
	Letter	Count	Percent
	C-	0	0.0%
	C	17	0.2%
	C+	109	1.1%
	B-	344	3.4%
	B	925	9.3%
	B+	1228	12.3%
	A-	1667	16.7%
	A	2311	23.1%
	A+	3399	34.0%
	
	Letter Level Results
	Letter	Count	Percent
	C	126	1.3%
	B	2497	25.0%
	A	7377	73.8%
	
	####################Done#####################

Sample output from `python splatoon_rank_extended_s.py` (includes the S/S+ ranks and [Version 2.2](http://splatoonwiki.org/wiki/Version_2.2.0) point rules):

	#############Initializing Players#############
	
	10000 players
	
	#################Playing Game#################
	
	10000 Rounds, 100000000 Total Games
	Skill Based == False, 0 Point Rank Down == False
	
	##################Summary####################
	
	
	Wins 50006094
	Loses 49993906
	
	Grade Results
	Letter  Count   Percent
	C-      2       0.02%
	C       10      0.1%
	C+      61      0.61%
	B-      203     2.03%
	B       484     4.84%
	B+      629     6.29%
	A-      881     8.81%
	A       1196    11.96%
	A+      1577    15.77%
	S       4606    46.06%
	S+      351     3.51%
	
	Letter Level Results
	Letter  Count   Percent
	C       73      0.73%
	B       1316    13.16%
	A       3654    36.54%
	S       4957    49.57%
	
	####################Done#####################
