import networkx as nx

def oracle_navigator(G, s, t):

	return nx.shortest_path(G, s, t)
