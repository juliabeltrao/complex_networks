import pickle 
import argparse
from oracle_navigator import oracle_navigator
from greedy_navigator import greedy_navigator
from calc_dist import total_distance

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--navigator", choices=["oracle", "greedy"], help="Specifies the navigator used.")
parser.add_argument("-d", "--data", choices=["budapest", "chicago", "des_moines", "helsinki", "rome", "san_francisco", "san_jose"], help="Specifies the data set used.")
parser.add_argument("-s", "--source", nargs='+', type=int, help="Specifies source node")
parser.add_argument("-t", "--target", nargs='+', type=int, help="Specifies target node")
parser.add_argument("-o", "--output", help="If specified, results are saved to this file. Otherwise they are printed on the screen.")
args = parser.parse_args()

net_file = "networks_with_edges/" + args.data + "_100.pickle"
net = pickle.load(open(net_file))

source = tuple(args.source)
target = tuple(args.target)

if args.navigator == "oracle":
	path = oracle_navigator(net, source, target)
	dist = total_distance(net, path)

elif args.navigator == "greedy":
	path = greedy_navigator(net, source, target)
	dist = total_distance(net, path)

output = args.data + "\n" + "path: " + str(path) + "\n" + "total distance: " + str(dist) + "\n"

if args.output:
	f = open(args.output, 'a')
	f.write(output)
	#f.write(args.data + "\n")
	#f.write("path: " + path + "\n")
	#f.write("total distance: " + dist + "\n")
else:
	print output

