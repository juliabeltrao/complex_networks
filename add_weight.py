import pickle
from calc_dist import wgs84_distance

def add_weight(network_file):

	#f = open(network_file)#, 'rwb')
	network = pickle.load(open(network_file))

	for e in network.edges():
		network[e[0]][e[1]]['dist'] = distance(network, e[0], e[1])
		
	#pickle.dump(network, f)

	return network

def distance(network, n1, n2):
	lat1 = network.node[n1]['lat']
	lon1 = network.node[n1]['lon']
	lat2 = network.node[n2]['lat']
	lon2 = network.node[n1]['lon']

	dist = wgs84_distance(lat1, lon1, lat2, lon2)

	return dist	
