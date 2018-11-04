# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 01:17:00 2018

@author: Sami
"""
#"""
graph_dict = {  "a":{"b": 1, "d": 1, "e":1 },
                "b":{"a": 1, "c": 1},
                "c":{"b": 1, "d": 1},
                "d":{"a": 1, "c": 1, "f":1 },
                "e":{"a": 1, "f":1 },
                "f":{"d": 1, "e":1}
                }
"""

import networkx as nx
hep_graph = nx.read_gml('C:/Users/samiu/Desktop/8009 LAB/hep-th.gml')
hep_graph.remove_nodes_from(list(nx.isolates(hep_graph)))
gMatrix = nx.to_scipy_sparse_matrix(hep_graph)
graph_dict = nx.to_dict_of_lists(hep_graph)
sparse_matrix = gMatrix.todense()
"""
g = {}
edges = {}
mst = []
#n = int(input(('Enter the number of nodes: ')))
n = 7610
for i in graph_dict:
    g[i] = 15751
src = input('Enter the source node: ')
edges[src] = 'None'
g[src] = 0
#print(g)
while g:
    #print('Map:  ',g)
    extract_min = list(min(zip(g.values(), g.keys())))
    #extract_min = list(min(zip(g.values(), list(g))))
    print(extract_min)
    minimum_value  = extract_min[0]
    minimum_node = extract_min[1]
    print('Minimum-->',minimum_node)
    #if edges[minimum_node]!='None':
     #   mst.append(edges[minimum_node])
   # neighbours = [i for i in graph_dict[minimum_node].keys()]
    neighbours = [i for i in range(len(list(graph_dict[minimum_node])))]
    print('neighbours ',neighbours )
    for nei in neighbours:
        print('nei: ',nei)
        if nei in g.keys():
            if graph_dict[minimum_node][nei] < g[nei]:
                g[nei] = graph_dict[minimum_node][nei]
                edges[nei] = (minimum_node, nei)
    g.pop(minimum_node)


print('Minimum spanning tree: ',mst)