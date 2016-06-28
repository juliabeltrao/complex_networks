import networkx as nx
import math 
import pickle

TORADIANS = 3.141592653589793 / 180.
EARTH_RADIUS = 6378137.

def preprocess(network_file):

	fi = open("networks_with_edges/" + network_file, 'rb')
	network = pickle.load(fi)

	largest_component = get_largest_component(network)
	
	add_weight(largest_component)

	fo = open("largest_components/" + network_file, 'wb')
	pickle.dump(largest_component, fo)

def get_largest_component(network):

	component_tuples=[]
	subgraphs = list(nx.connected_component_subgraphs(network))
	for graph in subgraphs:
		t = tuple((graph.number_of_nodes(), graph))
		component_tuples.append(t)

	largest_component_tuple = max(component_tuples)
	largest_component = largest_component_tuple[1]

	return largest_component


def add_weight(network):
	
	for e in network.edges():
		network[e[0]][e[1]]['dist'] = distance(network, e[0], e[1])
		
	#return network

def distance(network, n1, n2):
	lat1 = network.node[n1]['lat']
	lon1 = network.node[n1]['lon']
	lat2 = network.node[n2]['lat']
	lon2 = network.node[n2]['lon']

	dist = wgs84_distance(lat1, lon1, lat2, lon2)

	return dist	

def wgs84_distance(lat1, lon1, lat2, lon2):

	"""Distance (in meters) between two points in WGS84 coord system."""
	dLat = math.radians(lat2 - lat1)
	dLon = math.radians(lon2 - lon1)

	a = (math.sin(dLat / 
	2) * math.sin(dLat / 
	2) +
	math.cos(math.radians(lat1))
	 * math.cos(math.radians(lat2)) *
	math.sin(dLon
	 / 
	2) * math.sin(dLon / 
	2))

	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	d = EARTH_RADIUS * c

	return d

def wgs84_height(meters):
	return  meters/(EARTH_RADIUS * TORADIANS)

def wgs84_width(meters, lat):
	R2 = EARTH_RADIUS * cos(lat*TORADIANS)
	return meters/(R2 * TORADIANS)	


if __name__ == "__main__":
	cities_networks = ["des_moines_100.pickle", "budapest_100.pickle", "chicago_100.pickle", "helsinki_100.pickle", "rome_100.pickle", "san_francisco_100.pickle", "san_jose_100.pickle"]

	for cities in cities_networks:
		preprocess(cities)
