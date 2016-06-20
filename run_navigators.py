import pickle 
from oracle_navigator import oracle_navigator
from greedy_navigator import greedy_navigator
from calc_dist import total_distance

def run_navigator(network, navigator, source, target, output):
	
	if navigator == "oracle":
		path = oracle_navigator(network, source, target)

	elif navigator == "greedy":
		path = greedy_navigator(network, source, target)
	
	dist = total_distance(network, path)

	out = "\n" + "path: " + path + "\n" + "total distance: " + dist + "\n"

	if output:
		f = open(output, 'a')
		f.write(out)
		#f.write(args.data + "\n")
		#f.write("path: " + path + "\n")
		#f.write("total distance: " + dist + "\n")
	else:
		print out

if __name__ = "__main__":

	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("-n", "--navigator", choices=["oracle", "greedy"], help="Specifies the navigator used.")
	parser.add_argument("-d", "--data", choices=["budapest", "chicago", "des_moines", "helsinki", "rome", "san_francisco", "san_jose"], help="Specifies the data set used.")
	parser.add_argument("-s", "--source", nargs="+", type=int, help="Specifies source node")
	parser.add_argument("-t", "--target", nargs="+", type=int, help="Specifies target node")
	parser.add_argument("-o", "--output", help="If specified, results are saved to this file. Otherwise they are printed on the screen.")
	args = parser.parse_args()

	net_file = "networks_with_edges/" + args.data + "_100.pickle"
	net = pickle.load(open(net_file))

	run_navigator(net, args.navigator, tuple(args.source), tuple(args.target), args.output)
	
