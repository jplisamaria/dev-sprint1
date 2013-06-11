# This is where Exercise 5.6 goes
# Name: Lisa-Maria Mehta



import math
from TurtleWorld import * 		
world = TurtleWorld()						


def koch (t, l):
	"""defines a Koch curve with length l."""
	if l < 30:
		fd (t, l)
		return  #I got this from the example in the book
	n = l/3.0
	koch (t, n)
	lt (t, 60)
	koch (t, n)
	rt (t, 120)
	koch (t, n)
	lt (t, 60)
	koch (t, n)

def snowflake (t, l):
	"""Draws 3 Koch curves in a row to make a 
	snowflake."""
	for i in range (3):
		koch (bob, length)
		rt (bob, 120)


# ******************
# ** Main Porgram **
# ******************
bob = Turtle()
length = 300
bob.delay = 0.001
 
snowflake (bob, length)

wait_for_user()	