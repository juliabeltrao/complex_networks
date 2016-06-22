#import pdb; pdb.set_trace()
import sys
import math
import random as rd
import networkx as nx
import matplotlib.pyplot as plt
from run_navigators import run_navigator

def plot_graph(network):

	print "Collecting data..."
	d1, d2 = collect_data(network)
	print "d1", d1
	print "\nd2", d2
	data = zip(d1, d2)
	data.sort()
	print "\ndata", data
	#sys.exit()
	oracle_dist, greedy_dist = zip(*data) 
	
	# plotting identity line
	x = [0, math.ceil(max(max(oracle_dist), max(greedy_dist)))]
	plt.plot(x, x, 'k--')

	# plotting oracle x greedy
	plt.xlabel("oracle distance")
	plt.ylabel("greedy distance")
	plt.plot(oracle_dist, greedy_dist, 'ro')
	plt.show()
	

def collect_data(network):

	oracle_dist=[]
	greedy_dist=[]
	print "Generating random pairs..."
	source, target = generate_pairs(network)

	print "Running navigators..."
	for pair in zip(source, target):
		oracle_dist.append(run_navigator(network, 'oracle', pair[0], pair[1], None))		
		greedy_dist.append(run_navigator(network, 'greedy', pair[0], pair[1], None))		
	
	return oracle_dist, greedy_dist

def generate_pairs(G):

	source=[]
	target=[]
	N = len(G.nodes())
	i=0

	while i < N/2:
		s = rd.randrange(0, N-1)
		t = rd.randrange(0, N-1)
		while (s == t or not nx.has_path(G, G.nodes()[s], G.nodes()[t])):
			t = rd.randrange(0, N-1)
		source.append(G.nodes()[s])	
		target.append(G.nodes()[t])
		i=i+1
		#print source
		#print target

	return source, target

