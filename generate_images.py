import pickle
import draw_network as dn
import plot_graph as pg

def combined_graph(data_dict):
	

networks = ["des_moines_100.pickle", "budapest_100.pickle", "chicago_100.pickle", "helsinki_100.pickle", "rome_100.pickle", "san_francisco_100.pickle", "san_jose_100.pickle"]

combined_data = {}

for net in networks:
	fi = "largest_components/" + net
	network = pickle.load(open(fi))
	fo = "images/networks/" + net.replace("pickle", "pdf")
	dn.draw_network(network, fo)
	fo = "images/graphs/" + net.replace("pickle", "pdf")
	data = pg.plot_graph(network, fo)
	combined_data[net] = data

combined_graph(combined_data)	
