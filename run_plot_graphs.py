import pickle
from generate_nodePairs import plot_graph
from draw_graph import draw_network

toy_networks = ["toy_lattice.pickle"]
cities_networks = ["des_moines_100.pickle"]

#for network in toy_networks:

#	f = "toy_networks/" + network
#	network = pickle.load(open(f))
#	plot_graph(network)
	#draw_network(network)

for network in cities_networks:
	
	f = "networks_with_weights/" + network
	network = pickle.load(open(f))
	plot_graph(network)
	
