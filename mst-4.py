# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 00:48:07 2018

@author: Sami
"""
import networkx as nx
hep_graph = nx.read_gml('C:/Users/samiu/Desktop/8009 LAB/hep-th.gml')
hep_graph.remove_nodes_from(list(nx.isolates(hep_graph)))
gMatrix = nx.to_scipy_sparse_matrix(hep_graph)
#graph_dict = nx.to_dict_of_lists(hep_graph)
sparse_matrix = gMatrix.todense()
def prim(graph, root):
    assert type(graph)==dict

    nodes = list(graph)
    nodes.remove(root)
    
    visited = [root]
    path = []
    next = None

    while nodes:
        distance = float('inf') 
        for s in visited:
            for d in graph[s]:
                if d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next = d
        path.append((pre, next))
        visited.append(next)
        nodes.remove(next)

    return path


if __name__ == '__main__':
#    """   
    graph_dict = {  "s1":{"s1": 0, "s2": 2, "s10": 3, "s12": 4, "s5":3},
                    "s2":{"s1": 1, "s2": 0, "s10": 4, "s12": 2, "s5":2},
                    "s10":{"s1": 2, "s2": 6, "s10": 0, "s12":3, "s5":4},
                    "s12":{"s1": 3, "s2": 5, "s10": 2, "s12":0,"s5":2},
                    "s5":{"s1": 3, "s2": 5, "s10": 2, "s12":4,"s5":0},
    }
#    """
#    graph_dict = nx.to_dict_of_lists(hep_graph)
    path = prim(graph_dict, 's1')
    print (path)