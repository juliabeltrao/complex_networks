import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from greedy_navigator import map_projection

def draw_network(network, output):
        
	components = sorted(nx.connected_components(network), key = len)
	largest_comp = components.pop()

	pos={}
	for n in largest_comp:
		pos[n] = np.array(map_projection(network.node[n]['lat'], network.node[n]['lon']))

	nx.draw_networkx(network, pos=pos, nodelist=largest_comp, node_size=100)
	
	plt.show()
	
	if output:
		plt.savefig(output)

	plt.close()
