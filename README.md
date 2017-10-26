# yahtzee

Play one of your old favorites in your terminal!

REQUIREMENTS

	Python 3

DIRECTIONS

	Navigate to desired directory

	git init
	git clone https://github.com/cmclaug3/yahtzee.git
	python3 Yahtzee.py



TODO

SCOREBOARD

	allow duplicate keys
	allow delete (all except defaults)
	allow show entire scoreboard


ABOUT YAHTZEE

	basic intro
	phases of game


HOW TO PLAY

	during rolls (saving by position) / "a" and "0"
	after rolls (pick choice) / select from available


STRATEGY

	how different choice picks affect points



POINT BREAKDOWN

	Upper choices (1s, 2s, 3s, 4s, 5s, 6s)

		sum of totol dice matching choice

	Lower choices

		play - choice - points - stipulations

		3ok - 3 of a kind - sum of all dice - must have atleast three of same dice
		4ok - 4 of a kind - sum of all dice - must have atleast four of same dice
		fh - full house - 25 - three of one dice and two of another
		ss - small straight - 30 - alteast four of five dice in a numerical row
		ls - long straight - 40 - five dice in a numerical row
		y - yahtzee - 50 - all five dice the same
		w - wild - sum of all dice - NONE



BONUSES

	35 if upper choices total 63 or more

	100 for each successful yahtzee after primary

		if dice number showing yahtzee has been used in upper choices allow JOKER to be used for ss/ls/fh
		else has to be used elsewhere



KB SHORTCUTS