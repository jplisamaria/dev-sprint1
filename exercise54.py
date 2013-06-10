# This is where Exercise 5.4 goes
# Name: Lisa-Maria Mehta


def get_side(side):
	"""Solicits user input for sidelengths, and returns value as
	integer.  Exits program if user-entered value is not positive."""
	print side, '=',
	length =  raw_input ()
	if int(length) > 0:
		return int(length)
	else:
		print ('Not positive integer. Program exits.')
		quit()
		
def is_triangle(x,y,z):
	"""Checks to see if sides x, y, and z, can form a valid
	triangle."""
	if (x>=y+z) or (y>=x+z) or (z>=x+y):
		print "Not a valid triangle."
	else: 
		print "Yes, a valid triangle."


# ******************
# ** Main Porgram **
# ******************
print 'Please enter sidelengths of triangle as positive integers.'

#	------------------
#	Getting user input
x = (get_side ('x'))
y = (get_side ('y'))
z = (get_side ('z'))
#	------------------

is_triangle(x,y,z)
