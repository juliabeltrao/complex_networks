import pickle
import math
import matplotlib.pyplot as plt
import draw_network as dn
import plot_graph as pg

def combined_graph(data_dict):
	name_dict = dict([("budapest_100.pickle",("Budapest", 'red','<')), ("chicago_100.pickle", ("Chicago", 'blue','s')), ("helsinki_100.pickle",("Helsinki", 'red','o')), ("rome_100.pickle",("Rome", 'red','>')), ("san_francisco_100.pickle",("San Francisco", 'blue','v')), ("san_jose_100.pickle",("San Jose", 'blue','^'))])
	
	xlocalmax = []
	ylocalmax = []
	xlocalmin = []
	ylocalmin = []

	for k, v in data_dict.iteritems():
		x = v[0]
		y = v[1]		
		e = v[2]

		xlocalmin.append(min(x))
		ylocalmin.append(min(e))
		xlocalmax.append(max(x))
		ylocalmax.append(max(e))
		#ylocalmax.append(max(max(x), max(y), max(e)))

		plot_info = name_dict[k]	
		plt.errorbar(x, y, yerr=e, label=plot_info[0], color=plot_info[1], marker=plot_info[2], ls='solid')
		plt.legend(loc='lower right')

	# plotting identity line
	xmin = math.ceil(min(xlocalmin))
	ymin = math.ceil(min(ylocalmin))
	xmax = math.ceil(max(xlocalmax))
	ymax = math.ceil(max(ylocalmax))
	#xy = max(abs(xymin), xymax)
	x = [0, xmax]
	plt.plot(x, x, 'k--')
	#plt.axis([0, xmax, ymin, ymax])

	plt.show()

combined_data = {}
networks = ["des_moines_100.pickle", "budapest_100.pickle", "chicago_100.pickle", "helsinki_100.pickle", "rome_100.pickle", "san_francisco_100.pickle", "san_jose_100.pickle"]

for net in networks:
	fi = "largest_components/" + net
	network = pickle.load(open(fi))
	#fo = "images/networks/" + net.replace("pickle", "pdf")
	#dn.draw_network(network, fo)
	fo = "images/graphs/" + net.replace("pickle", "pdf")
	data = pg.plot_graph(network, fo)
	if net != "des_moines_100.pickle":
		combined_data[net] = data

combined_graph(combined_data)	
