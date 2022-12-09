import networkx as nx


new_Graph = nx.Graph()

new_Graph.add_node(1)
new_Graph.add_nodes_from([2, 3, 4, 5])
#new_Graph.add_edges_from([2, 3])
new_Graph.add_node(())
print(new_Graph)