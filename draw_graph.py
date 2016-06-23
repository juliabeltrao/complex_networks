import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from greedy_navigator import map_projection

def draw_network(network, output):
        
	plt.figure()
	pos={}
	for n in network.nodes():
		pos[n] = np.array(map_projection(network.node[n]['lat'], network.node[n]['lon']))

	nx.draw(network, pos)
	
	plt.show()

	if output:
		plt.savefig(output)
	else:
		plt.show()
