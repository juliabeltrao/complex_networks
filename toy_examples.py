# This file defines some toy examples based on real cities

import networkx as nx
import pickle
import math
import sys 

R= 6378137.0
PI = 3.14159265359

def toy_moscow(alg, s, t):

	G = nx.Graph()

	# Inner Ring
	G.add_node(1, lon=0, lat=inv_projection(1))
	G.add_node(2, lon=-0.7/R, lat=inv_projection(0.7))
	G.add_node(3, lon=-1/R, lat=inv_projection(0))
	G.add_node(4, lon=-0.7/R, lat=inv_projection(-0.7))
	G.add_edges_from([(1,2), (2,3), (3,4), (4,1)])

	# Intermediate Ring
	G.add_node(1, lon=0, lat=inv_projection(3))
	G.add_node(3, lon=-3/R, lat=inv_projection(0))
	G.add_node(3, lon=0, lat=inv_projection(-3))
	G.add_node(1, lon=0, lat=inv_projection(-3))

	# Outter Ring

	# Connections between rings
	
	
def toy_us_grid_city():

	G = nx.Graph()

	G.add_node(1, lon=0, lat=inv_projection(1))
	G.add_node(2, lon=0, lat=inv_projection(2))
	G.add_node(3, lon=0, lat=inv_projection(3))
	G.add_node(4, lon=0, lat=inv_projection(4))
	G.add_node(5, lon=0, lat=inv_projection(5))

	l=1/R
	G.add_node(6, lon=l, lat=inv_projection(0))
	G.add_node(7, lon=l, lat=inv_projection(1))
	G.add_node(8, lon=l, lat=inv_projection(2))
	G.add_node(9, lon=l, lat=inv_projection(3))
	G.add_node(10, lon=l, lat=inv_projection(4))
	G.add_node(11, lon=l, lat=inv_projection(5))
	G.add_node(12, lon=l, lat=inv_projection(6))
	G.add_edges_from([(6,7), (7,8), (8,9), (9,10), (10,11), (11,12)])

	l=2/R
	G.add_node(13, lon=l, lat=inv_projection(0))
	G.add_node(14, lon=l, lat=inv_projection(1))
	G.add_node(15, lon=l, lat=inv_projection(2))
	G.add_node(16, lon=l, lat=inv_projection(3))
	G.add_node(17, lon=l, lat=inv_projection(4))
	G.add_node(18, lon=l, lat=inv_projection(5))
	G.add_node(19, lon=l, lat=inv_projection(6))
	G.add_edges_from([(13,14), (14,15), (15,16), (16,17), (17,18), (18,19)])

	l=3/R
	G.add_node(20, lon=l, lat=inv_projection(0))
	G.add_node(21, lon=l, lat=inv_projection(1))
	G.add_node(22, lon=l, lat=inv_projection(2))
	G.add_node(23, lon=l, lat=inv_projection(3))
	G.add_node(24, lon=l, lat=inv_projection(4))
	G.add_node(25, lon=l, lat=inv_projection(5))
	G.add_node(26, lon=l, lat=inv_projection(6))
	G.add_edges_from([(20,21), (21,22), (22,23), (23,24), (24,25), (25,26)])

	l=4/R
	G.add_node(27, lon=l, lat=inv_projection(0))
	G.add_node(28, lon=l, lat=inv_projection(1))
	G.add_node(29, lon=l, lat=inv_projection(2))
	G.add_node(30, lon=l, lat=inv_projection(3))
	G.add_node(31, lon=l, lat=inv_projection(4))
	G.add_node(32, lon=l, lat=inv_projection(5))
	G.add_node(33, lon=l, lat=inv_projection(6))
	G.add_edges_from([(27,28), (28,29), (29,30), (30,31), (31,32), (32,33)])

	l=5/R
	G.add_node(34, lon=l, lat=inv_projection(0))
	G.add_node(35, lon=l, lat=inv_projection(1))
	G.add_node(36, lon=l, lat=inv_projection(2))
	G.add_node(37, lon=l, lat=inv_projection(3))
	G.add_node(38, lon=l, lat=inv_projection(4))
	G.add_node(39, lon=l, lat=inv_projection(5))
	G.add_node(40, lon=l, lat=inv_projection(6))
	G.add_edges_from([(34,35), (35,36), (36,37), (37,38), (39,40), (40,41)])

	l=6/R
	G.add_node(41, lon=l, lat=inv_projection(1))
	G.add_node(42, lon=l, lat=inv_projection(2))
	G.add_node(43, lon=l, lat=inv_projection(3))
	G.add_node(44, lon=l, lat=inv_projection(4))
	G.add_node(45, lon=l, lat=inv_projection(5))

	G.add_edges_from([(1,7), (7,14), (14,21), (21,28), (28,35), (35,41)])
	G.add_edges_from([(2,8), (8,15), (15,22), (22,29), (29,36), (36,42)])
	G.add_edges_from([(3,9), (9,16), (16,23), (23,30), (30,37), (37,43)])
	G.add_edges_from([(4,10), (10,17), (17,24), (24,31), (31,38), (38,44)])
	G.add_edges_from([(5,11), (11,18), (18,25), (25,32), (32,39), (39,45)])

	f = open("toy_networks/toy_lattice.pickle", 'wb')

	pickle.dump(G, f)

def inv_projection(y):

	return math.degrees((PI/2.0)-(2.0*math.atan(math.exp(-y/R))))
