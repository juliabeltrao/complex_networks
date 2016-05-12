import networkx as nx
import matplotlib.pyplot as plt
from greedy_navigator import greedy_navigator

def test1():

	G = nx.Graph()

	G.add_node(1, xpos=-1, ypos=-1)
	G.add_node(2, xpos=1, ypos=-1)
	G.add_node(3, xpos=0, ypos=0)
	G.add_node(4, xpos=0, ypos=1)
	G.add_node(5, xpos=0, ypos=2)

	G.add_edges_from([(1,3), (2,3), (3,4), (4,5)])

	nx.draw(G)

	plt.savefig("test1.png")
	plt.close()

	path = greedy_navigator(G, 1, 5)

	return path

def test2():

	G = nx.Graph()

	G.add_node(1, xpos=-1, ypos=-1)
	G.add_node(2, xpos=1, ypos=-1)
	G.add_node(3, xpos=0, ypos=0)
	G.add_node(4, xpos=0, ypos=1)
	G.add_node(5, xpos=0, ypos=2)
	G.add_node(6, xpos=-2, ypos=1)
	G.add_node(7, xpos=2, ypos=1)

	G.add_edges_from([(1,3), (2,3), (3,4), (4,5), (1,2), (1,6), (2,7), (3,6), (3,7), (4,6), (4,7), (6,5), (7,5)])

	nx.draw(G)

	plt.savefig("test2.png")
	plt.close()

	path = greedy_navigator(G, 1, 5)

	return path

def test3():

	G = nx.Graph()

	G.add_node(0, xpos=0, ypos=0)
	G.add_node(1, xpos=0, ypos=1)
	G.add_node(2, xpos=1, ypos=0)
	G.add_node(3, xpos=0, ypos=-1)
	G.add_node(4, xpos=-1, ypos=0)
	G.add_node(5, xpos=0, ypos=2)
	G.add_node(6, xpos=2, ypos=0)
	G.add_node(7, xpos=0, ypos=-2)
	G.add_node(8, xpos=-2, ypos=0)

	G.add_edges_from([(0,1), (0,2), (0,3), (0,4), (1,5), (2,6), (3,7), (4,8), (1,2), (2,3), (3,4), (4,1)])

	nx.draw(G)

	plt.savefig("test3.png")
	plt.close()

	path1 = greedy_navigator(G, 7, 5)
	path2 = greedy_navigator(G, 7, 8)

	return (path1, path2)	


if __name__ == "__main__":
	test3()
