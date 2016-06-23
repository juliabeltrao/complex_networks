#import pdb; pdb.set_trace()
import pickle

def count_singleton(G):

	singleton = 0
	for n in G.nodes():
		if len(G.neighbors(n)) == 0:
			singleton = singleton + 1

	return singleton

d = "networks_with_edges/"
cities_networks = ["des_moines_100.pickle", "budapest_100.pickle", "chicago_100.pickle", "helsinki_100.pickle", "rome_100.pickle", "san_francisco_100.pickle", "san_jose_100.pickle"]

for city in cities_networks:
	path = d + city
	network = pickle.load(open(path))
	N = network.number_of_nodes()
	N_single = count_singleton(network)
	print city
	print "Number of nodes: ", N
	print "Number of single nodes: ", N_single


