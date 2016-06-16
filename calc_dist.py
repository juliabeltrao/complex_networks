import networkx as nx
from math import sqrt

TORADIANS = 3.141592653589793 / 180.
EARTH_RADIUS = 6378137.

def total_distance(G, path):

	dist = 0
	n1 = path[0]

	for n2 in path[1:]:
		d = wgs84_dist(G.node[n1]['lat'], G.node[n1]['lon'], G.node[n2]['lat'], G.node[n2]['lon']) 
		dist = dist + d
		n1 = n2

	return dist

def wgs84_distance(lat1, lon1, lat2, lon2):

	"""Distance (in meters) between two points in WGS84 coord system."""
	dLat = math.radians(lat2 - lat1)
	dLon = math.radians(lon2 - lon1)

	a
	 = (math.sin(dLat / 
	2) * math.sin(dLat / 
	2) +
	math.cos(math.radians(lat1))
	 * math.cos(math.radians(lat2)) *
	math.sin(dLon
	 / 
	2) * math.sin(dLon / 
	2))

	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	d = EARTH_RADIUS * c

	return d


def wgs84_height(meters):
	return  meters/(EARTH_RADIUS * TORADIANS)

def wgs84_width(meters, lat):
	R2 = EARTH_RADIUS * cos(lat*TORADIANS)
	return meters/(R2 * TORADIANS)	
