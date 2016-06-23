import pickle
import networkx as nx
from generate_nodePairs import plot_graph
from draw_graph import draw_network

toy_networks = ["toy_lattice.pickle"]
cities_networks = ["des_moines_100.pickle", "budapest_100.pickle", "chicago_100.pickle", "helsinki_100.pickle", "rome_100.pickle", "san_francisco_100.pickle", "san_jose_100.pickle"]

#for network in toy_networks:

	#f = "toy_networks/" + network
	#network = pickle.load(open(f))
	#draw_network(network, None)

for city in cities_networks:
	fi = "networks_with_edges/" + city
	network = pickle.load(open(fi))
	fo = "images/" + city.replace("pickle", "png")
	draw_network(network, fo)
