import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from greedy_navigator import map_projection

def draw_network(network, output):
        
	#components = sorted(nx.connected_components(network), key = len)
	#largest_comp = components.pop()

	#edges = []
	#for e in network.edges():
	#	if e[0] in largest_comp and e[1] in largest_comp:
	#		edges.append(e)

	pos={}
	for n in network.nodes():
		pos[n] = np.array(map_projection(network.node[n]['lat'], network.node[n]['lon']))

	#nx.draw_networkx(network, pos=pos, with_labels=False, node_size=20)
	nx.draw_networkx_edges(network, pos=pos)
	plt.axis('off')
	
	if output:
		plt.savefig(output)
	else:
		plt.show()

	plt.close()
