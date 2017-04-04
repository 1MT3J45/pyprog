import math
def dist(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	square = dx**2 + dy**2
	result = math.sqrt(square)
	print result
dist(1,2,4,6)
	
