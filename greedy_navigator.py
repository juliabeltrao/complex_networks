import networkx as nx
import numpy as np

# performs a greedy navigation in the network represented by graph G 
# from source node s to target node t
def greedy_navigator(G, s, t):

	# list to keep track of which nodes were visited 
	visited=[s]	
	# list to keep track of the path found by the navigator
	path=[s]

	i = s

	# coordinates of the target node
	pt = [G.node[t]['xpos'], G.node[t]['ypos']]	

	# until target node is reached
	while(i != t):

		# list to keep track of the neighbours of the current node i
		neighborsList=[]
		# coordinates of the current node
		pi = [G.node[i]['xpos'], G.node[i]['ypos']]			

		# for all neighbors of the current node
		for j in G.neighbors(i):
			# if neighbor j has not been visited 
			if(j not in visited):
				# mark neighbor j as visited
				visited.append(j)
			
				# if neighbor j is the target node t	
				if(j == t):
					neighbor = -1, j
				# else if j is not t
				else:
					# coordinates of neighbor node j
					pj = [G.node[j]['xpos'], G.node[j]['ypos']]			
					# calculate angle between the vectors vij and vit
					neighbor = calculate_angle(pi, pj, pt), j

				# add neighbor j to list of neighbors of i
				neighborsList.append(neighbor)

		# retrieve the neighbor with the smallest angle
		min_angle = min(neighborsList)
		# continue the search from this neighbor
		i = min_angle[1]		
		# add this neighbor to path
		path.append(i)

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
