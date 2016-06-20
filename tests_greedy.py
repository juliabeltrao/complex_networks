import sys
import math
import networkx as nx
import matplotlib.pyplot as plt
from greedy_navigator import greedy_navigator
from oracle_navigator import oracle_navigator

R= 6378137.0
PI = 3.14159265359

def test1(alg, s, t):

	G = nx.Graph()

	G.add_node(1, lon=-1/R, lat=inv_projection(-1))
	G.add_node(2, lon=1/R, lat=inv_projection(-1))
	G.add_node(3, lon=0/R, lat=inv_projection(0))
	G.add_node(4, lon=0/R, lat=inv_projection(1))
	G.add_node(5, lon=0/R, lat=inv_projection(2))

	G.add_edges_from([(1,3), (2,3), (3,4), (4,5)])

	nx.draw(G)

	plt.savefig("test1.png")
	plt.close()

	if(alg == "greedy"):
		path = greedy_navigator(G, s, t)
	elif(alg == "oracle"):
		path = oracle_navigator(G, s, t)
	else:
		sys.stderr.write("Algorithms supported are: greedy and oracle.")
		sys.exit(1)

	#path = greedy_navigator(G, 1, 5)

	return path

def test2(alg, s, t):

	G = nx.Graph()

	G.add_node(1, lon=-1/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(-1/-R))))
	G.add_node(2, lon=1/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(-1/-R))))
	G.add_node(3, lon=0/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(0/-R))))
	G.add_node(4, lon=0/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(1/-R))))
	G.add_node(5, lon=0/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(2/-R))))
	G.add_node(6, lon=-2/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(1/-R))))
	G.add_node(7, lon=2/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(1/-R))))

	G.add_edges_from([(1,3), (2,3), (3,4), (4,5), (1,2), (1,6), (2,7), (3,6), (3,7), (4,6), (4,7), (6,5), (7,5)])

	nx.draw(G)

	plt.savefig("test2.png")
	plt.close()

	if(alg == "greedy"):
		path = greedy_navigator(G, s, t)
	elif(alg == "oracle"):
		path = oracle_navigator(G, s, t)
	else:
		sys.stderr.write("Algorithms supported are: greedy and oracle.")
		sys.exit(1)

	#path = greedy_navigator(G, 1, 5)

	return path

def test3(alg, s, t):

	G = nx.Graph()

	G.add_node(0, lon=0/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(0/-R))))
	G.add_node(1, lon=0/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(1/-R))))
	G.add_node(2, lon=1/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(0/-R))))
	G.add_node(3, lon=0/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(-1/-R))))
	G.add_node(4, lon=-1/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(0/-R))))
	G.add_node(5, lon=0/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(2/-R))))
	G.add_node(6, lon=2/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(0/-R))))
	G.add_node(7, lon=0/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(-2/-R))))
	G.add_node(8, lon=-2/R, lat=(PI/2.0)-(2.0*math.atan(math.exp(0/-R))))

	G.add_edges_from([(0,1), (0,2), (0,3), (0,4), (1,5), (2,6), (3,7), (4,8), (1,2), (2,3), (3,4), (4,1)])

	nx.draw(G)

	plt.savefig("test3.png")
	plt.close()

	if(alg == "greedy"):
		path = greedy_navigator(G, s, t)
	elif(alg == "oracle"):
		path = oracle_navigator(G, s, t)
	else:
		sys.stderr.write("Algorithms supported are: greedy and oracle.")
		sys.exit(1)

	#path1 = greedy_navigator(G, 7, 5)
	#path2 = greedy_navigator(G, 7, 8)

	return path	

def inv_projection(y):
	return math.degrees((PI/2.0)-(2.0*math.atan(math.exp(-y/R))))
