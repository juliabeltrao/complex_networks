#import pdb; pdb.set_trace()
import networkx as nx
import numpy as np
import math

EARTH_RADIUS = 6378137.0
PI = 3.14159265359

# performs a greedy navigation in the network represented by graph G 
# from source node s to target node t
def greedy_navigator(G, s, t):

	# list to keep track of which nodes were visited 
	visited=[]	
	# list to keep track of the path found by the navigator
	path=[]

	i = s

	# coordinates of the target node
	#pt = [G.node[t]['lon'], G.node[t]['lat']]	
	pt = map_projection(G.node[t]['lat'], G.node[t]['lon'])	

	# until target node is reached
	while(i != t):

		# list to keep track of the neighbours of the current node i
		neighborsList=[]
		# coordinates of the current node
		#pi = [G.node[i]['lon'], G.node[i]['lat']]			
		pi = map_projection(G.node[i]['lat'], G.node[i]['lon'])			

		# for all neighbors of the current node
		for j in G.neighbors(i):
			# if neighbor j has not been visited 
			if(j not in visited):
				# mark neighbor j as visited
				#visited.append(j)
			
				# if neighbor j is the target node t	
				# if(j == t):
					#neighbor = 0, j
				# else if j is not t
				# else:
					# coordinates of neighbor node j
					#pj = [G.node[j]['lon'], G.node[j]['lat']]			
				pj = map_projection(G.node[j]['lat'], G.node[j]['lon'])			
					# calculate angle between the vectors vij and vit
				neighbor = calculate_angle(pi, pj, pt), j

				# add neighbor j to list of neighbors of i
				neighborsList.append(neighbor)

		if(i not in visited):
			visited.append(i)

		if len(neighborsList):
			# add this neighbor to path
			path.append(i)
			# retrieve the neighbor with the smallest angle
			min_angle = min(neighborsList)
			# continue the search from this neighbor
			i = min_angle[1]		
		else:
			i = path.pop()

	path.append(t)
	
	return path

def calculate_angle(p1, p2, p3):
	
	# vector defined by points p1 and p2
	v12 = np.array(p1) - np.array(p2)
	# vector defined by points p1 and p3
	v13 = np.array(p1) - np.array(p3)

	# calculate angle between vectors v12 and v13
	angle = np.math.atan2(np.linalg.det([v12,v13]),np.dot(v12,v13))
	
	# return absolute value of the angle
	return abs(angle)

def map_projection(lat, lon):

	x = EARTH_RADIUS * math.radians(lon)
	y = EARTH_RADIUS * math.log(math.tan((PI/4.0) + (math.radians(lat)/2.0)))

	proj = [x, y]

	return proj
