import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def greedy_navigator(G, s, t):

	visited=[]	
	neighborsList=[]
	path=[s]
	i = s
	pt = [G.node[t]['xpos'], G.node[t]['ypos']]	

	while(i != t):

		pi = [G.node[i]['xpos'], G.node[i]['ypos']]			

		for j in G.neighbors(i):
			if(j not in visited):
				visited.append(j)
				
				if(j == t):
					neighbor = -1, j
				else:
					pj = [G.node[j]['xpos'], G.node[j]['ypos']]			
					neighbor = calculate_angle(pi, pj, pt), j

				neighborsList.append(neighbor)

		min_angle = min(neighborsList)
		i = min_angle[1]		
		path.append(i)

	return path

def calculate_angle(p1, p2, p3):
			
	v12 = np.array(p1) - np.array(p2)
	v13 = np.array(p1) - np.array(p3)

	angle = np.math.atan2(np.linalg.det([v12,v13]),np.dot(v12,v13))
	
	#return abs(np.degrees(angle))
	return abs(angle)

if __name__ == "__main__":

	G = nx.Graph()

	G.add_node(1, xpos=-1, ypos=-1)
	G.add_node(2, xpos=1, ypos=-1)
	G.add_node(3, xpos=0, ypos=0)
	G.add_node(4, xpos=0, ypos=1)
	G.add_node(5, xpos=0, ypos=2)

	G.add_edges_from([(1,3), (2,3), (3,4), (4,5)])

	nx.draw(G)

	plt.savefig("simple_graph.png")

	

	print greedy_navigator(G, 1, 5)

	
