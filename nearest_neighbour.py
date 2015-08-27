a = (raw_input()).split(' ')
row = int(a[0])
col = int(a[1])
destination = []
source = []
basemap = [['-' for i in range(row)] for j in range(col)]
def main():
	for i in range(row):
		basemap[i] = (raw_input()).split(' ')
	for i in range(row):
		for j in range(col):
			if basemap[i][j] == 'd':
				destination = [[i,j]]
				basemap[i][j] = 1
			elif basemap[i][j] == 's':
			 	source.append([i,j])
				basemap[i][j] = 1
			elif basemap[i][j] == 'w':
				basemap[i][j] = 0
			else:
				basemap[i][j] = 1
				
	for i in source:
		while i[0] == destination[0] and i[1] == destination[1]:
			navigator_obj = position(i,destination[0])
			print navigator_obj
			print navigator_obj.diagonal
			
			
	
def position(source,destination):
	direction = ""
	xdiff = destination[0]-source[0]
	ydiff = destination[1]-source[1]
	diagonal = min(xdiff,ydiff)
	if xdiff > 0:
		direction = direction+"S"
	elif xdiff < 0:
		direction = direction+"N"
	else:
		direction = direction+""
	 
	if ydiff > 0:
		direction = direction+"E"
	elif ydiff < 0:
		direction = direction+"W"
	else:
		direction = direction+""
	print str(source)+" to "+str(destination)+" in "+direction
	aja = adjacent(source)
	navigator_pass = navigator(aja,xdiff,ydiff,diagonal)
	return navigator_pass
	
def adjacent(point):
	aja = {}
	aja.update({'N':   rangecheck((point[0]-1,point[1]))   })
	aja.update({'S':   rangecheck((point[0]+1,point[1]))   })
	aja.update({'E':    rangecheck((point[0],point[1]+1))  })
	aja.update({'W':   rangecheck((point[0],point[1]-1))  })
	aja.update({'NE':   rangecheck((point[0]-1,point[1]+1))  })
	aja.update({'NW':   rangecheck((point[0]-1,point[1]-1))   })
	aja.update({'SE':   rangecheck((point[0]+1,point[1]+1))   })
	aja.update({'SW':   rangecheck((point[0]+1,point[1]-1))   })
	return aja

def rangecheck(point):
	if point[0]<0 or point[1]<0 or point[0]>=row or point[1]>=col:
		return
	if basemap[point[0]][point[1]] == 0:
		return
	else:
		return point
class navigator:
	def __init__(self,moves,xdiff,ydiff,diagonal):
        	self.moves = moves
        	self.xdiff = xdiff
		self.ydiff = ydiff
		self.diagonal = diagonal
if __name__ == '__main__':
    main()
