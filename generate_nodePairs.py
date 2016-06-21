#import pdb; pdb.set_trace()
import random as rd
import networkx as nx
import matplotlib.pyplot as plt
from run_navigators import run_navigator

def plot_graph(network):

	data = zip(collect_data(network))
	data.sort()
	
	# plotting identity line
	plt.plot(x, x)

	# plotting oracle x greedy
	oracle_dist, greedy_dist = zip(*data) 
	plt.plot()
	

def collect_data(netowrk):

	oracle_dist=[]
	greedy_dist=[]
	source, target = generate_pairs(network)

	for pair in zip(source, target):
		oracle_dist.append(run_navigator(network, 'oracle', pair[0], pair[1], None))		
		greedy_dist.append(run_navigator(network, 'greedy', pair[0], pair[1], None))		
	
	return oracle_dist, greedy_dist

def generate_pairs(G):

	source=[]
	target=[]
	N = len(G.nodes())
	i=0

	while i < 5:
		s = rd.randrange(0, N-1)
		t = rd.randrange(0, N-1)
		while s == t:
			t = rd.randrange(0, N-1)
		source.append(G.nodes()[s])	
		target.append(G.nodes()[t])
		i=i+1

	return source, target

