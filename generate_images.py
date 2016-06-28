import pickle
import draw_network as dn
import plot_graph as pg

networks = ["des_moines_100.pickle", "budapest_100.pickle", "chicago_100.pickle", "helsinki_100.pickle", "rome_100.pickle", "san_francisco_100.pickle", "san_jose_100.pickle"]

for net in networks:
	fi = "largest_components/" + net
	network = pickle.load(open(fi))
	fo = "images/networks/" + net.replace("pickle", "png")
	dn.draw_network(network, fo)
	fo = "images/graphs/" + net.replace("pickle", "png")
	pg.plot_graph(network, fo)
