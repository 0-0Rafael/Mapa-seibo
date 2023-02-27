#Crear el archivo OSM de el seibo UWU
"""
import osmium
import requests

class ElSeiboHandler(osmium.SimpleHandler):
    def __init__(self):
        osmium.SimpleHandler.__init__(self)
        self.buffer = []

    def node(self, n):
        self.buffer.append(n)

    def way(self, w):
        self.buffer.append(w)

    def relation(self, r):
        self.buffer.append(r)

    def download_osm(self, bbox):
        api = 'http://api.openstreetmap.org/api/0.6/map?bbox='
        url = api + str(bbox['left']) + ',' + str(bbox['bottom']) + ',' + \
              str(bbox['right']) + ',' + str(bbox['top'])
        response = requests.get(url)
        osm_data = response.content
        return osm_data

    def write_to_file(self, osm_data, filename):
        with open(filename, 'wb') as f:
            f.write(osm_data)

    def apply_file(self, filename):
        self.apply_file(filename)

    def apply_buffer(self):
        self.osm_data = osmium.SimpleHandler().apply(self.buffer)
        self.buffer = []

# bounding box for El Seibo province
bbox = {'left': -69.8274, 'bottom': 18.4732, 'right': -69.8079, 'top': 18.481}

handler = ElSeiboHandler()
osm_data = handler.download_osm(bbox)
handler.write_to_file(osm_data, 'el_seibo.osm')

"""

#Crear el archivo de los grafos 
"""
import networkx as nx
import xml.etree.ElementTree as ET

tree = ET.parse('el_seibo.osm')
root = tree.getroot()

G = nx.Graph()

for node in root.findall(".//node"):
    G.add_node(node.get('id'), lat=float(node.get('lat')), lon=float(node.get('lon')))

for way in root.findall(".//way"):
    nodes = way.findall(".//nd")
    for i in range(len(nodes)-1):
        G.add_edge(nodes[i].get('ref'), nodes[i+1].get('ref'))

nx.write_graphml(G, 'grafo.graphml')
"""