#import pdb; pdb.set_trace()
import sys
import math
import numpy as np
import random as rd
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import binned_statistic
from oracle_navigator import oracle_navigator
from greedy_navigator import greedy_navigator

def plot_graph(network, output):

	#print "Collecting data..."
	d1, d2 = collect_data(network)
	#print "d1", d1
	#print "\nd2", d2
	data = zip(d1, d2)
	data.sort()
	#print "\ndata", data
	#sys.exit()
	oracle_dist, greedy_dist = zip(*data) 
	#oracle_dist = list(oracle_dist)
	#greedy_dist = list(greedy_dist)
	
	# plotting identity line
	xymax = math.ceil(max(max(oracle_dist), max(greedy_dist))) + 100
	x = [0, xymax]
	plt.plot(x, x, 'k--')

	# plotting oracle x greedy
	plt.xlabel("Oracle distance (meters)")
	plt.ylabel("Greedy distance (meters)")
	plt.plot(oracle_dist, greedy_dist, 'b.')
	plt.axis([0, xymax, 0, xymax])

	n_bins = 10
	bin_centers, _, _ = binned_statistic(np.array(oracle_dist), np.array(oracle_dist), statistic='mean', bins=n_bins)
	bin_averages, _, _ = binned_statistic(np.array(oracle_dist), np.array(greedy_dist), statistic='mean', bins=n_bins)
	bin_stdevs, _, _ = binned_statistic(np.array(oracle_dist), np.array(greedy_dist), statistic='std', bins=n_bins)
	#plt.plot(bin_centers, bin_averages, yerr=bin_stdevs, color='red', marker='o', ls='solid')
	plt.errorbar(bin_centers, bin_averages, bin_stdevs, color='red', marker='o', ls='solid')

	if output:
		plt.savefig(output)
	else:
		plt.show()
		
	plt.close()

	return (bin_centers, bin_averages, bin_stdevs)

def collect_data(network):

	oracle_dist=[]
	greedy_dist=[]
	#print "Generating random pairs..."
	source, target = generate_pairs(network)

	#print "Running navigators..."
	for pair in zip(source, target):
		oracle_dist.append(run_navigator(network, 'oracle', pair[0], pair[1], None))		
		greedy_dist.append(run_navigator(network, 'greedy', pair[0], pair[1], None))		
	
	return oracle_dist, greedy_dist

def run_navigator(network, navigator, source, target, output):
	
	if navigator == "oracle":
		path = oracle_navigator(network, source, target)

	elif navigator == "greedy":
		path = greedy_navigator(network, source, target)
	
	dist = total_distance(network, path)

	out = "path: " + str(path) + "\n" + "total distance: " + str(dist) + "\n"

	if output:
		f = open(output, 'a')
		f.write(out)

	return dist

def generate_pairs(G):

	source=[]
	target=[]

	#components = sorted(nx.connected_components(G), key = len)
	#largest_comp = list(components.pop())

	N = G.number_of_nodes()
	i=0

	while i < N:
		s = rd.randrange(0, N-1)
		t = rd.randrange(0, N-1)
		#while (s == t or not nx.has_path(G, G.nodes()[s], G.nodes()[t])):
		while (s == t):
			t = rd.randrange(0, N-1)
		source.append(G.nodes()[s])	
		#source.append(largest_comp[s])	
		target.append(G.nodes()[t])
		#target.append(largest_comp[t])
		i=i+1
		#print source
		#print target

	return source, target

def total_distance(G, path):

	dist = 0
	n1 = path[0]

	for n2 in path[1:]:
		#d = wgs84_distance(G.node[n1]['lat'], G.node[n1]['lon'], G.node[n2]['lat'], G.node[n2]['lon']) 
		d = G[n1][n2]['dist']
		dist = dist + d
		n1 = n2

	return dist

