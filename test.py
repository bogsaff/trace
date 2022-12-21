import networkx as nx
import matplotlib.pyplot as plt
import json
from networkx.readwrite.json_graph import node_link_data
from networkx import convert_node_labels_to_integers
import requests

meshconfig = r = requests.get("http://meshconfig.nrp-nautilus.io/a2a").json()

new_Graph = nx.Graph()

# f = plt.figure()
# nx.draw(new_Graph, ax=f.add_subplot(111))
# f.savefig("graph.png")
#print(new_Graph)

for el in meshconfig['groups']['latency_a2a']['addresses']:
    #print(el['name'])
    new_Graph.add_node(el['name'], ip=meshconfig['addresses'][el['name']]['address'])

for el in meshconfig['groups']['latency_a2a']['addresses']:
    for el2 in meshconfig['groups']['latency_a2a']['addresses']:
        if el['name'] != el2['name']:
            new_Graph.add_edge(el['name'], el2['name'])


f1=open('graph.json', 'w+')
#f1.write(json.dumps(node_link_data(convert_node_labels_to_integers(new_Graph, label_attribute="name"))))
f1.write(json.dumps(node_link_data(new_Graph)))
f1.close()