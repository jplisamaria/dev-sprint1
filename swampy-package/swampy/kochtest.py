# Koch Test.  I've changed length to 100, and the statement to 
# l < 30 to better see the curve when you run the code.



import math
from TurtleWorld import * 		
world = TurtleWorld()						


def koch (t, l):
	print "Beginning Koch call,",
	print "l =",l
	if l < 30:
		fd (t, l)
		print "Drew segment of length   ", l
		return  #I got this from the example in the book
	n = l/3.0
	koch (t, n)
	print "First Koch call complete"
	print "     l =",l
	lt (t, 60)
	koch (t, n)
	print "Second Koch call complete"
	print "     l =",l
	rt (t, 120)
	koch (t, n)
	print "Third Koch call complete"
	print "     l =",l
	lt (t, 60)
	koch (t, n)
	print "Fourth Koch call complete"
	print "     l =",l


# ******************
# ** Main Porgram **
# ******************
bob = Turtle()
length = 100
bob.delay = 0.001

koch (bob, length) 

wait_for_user()	