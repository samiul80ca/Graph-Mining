# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 21:05:51 2018

@author: Sami
"""
import networkx as nx
hep_graph = nx.read_gml('C:/Users/samiu/Desktop/8009 LAB/hep-th.gml')
hep_graph.remove_nodes_from(list(nx.isolates(hep_graph)))
gMatrix = nx.to_scipy_sparse_matrix(hep_graph)
nodeDictList = nx.to_dict_of_lists(hep_graph)
sparse_matrix = gMatrix.todense()

def weight(ax, u, v):
    return ax[u][v]


def adjacent(ax, u):
    lx = []
    for x in range(len(ax)):
        if ax[u][x] > 0 and x != u:
            lx.insert(0, x)
    return lx


def extract_min(qx):
    q = qx[0]
    qx.remove(qx[0])
    return q


def decrease_key(qx, kx):
    for i in range(len(qx)):
        for j in range(len(qx)):
            if kx[qx[i]] < kx[qx[j]]:
                s = qx[i]
                qx[i] = qx[j]
                qx[j] = s


def prim(vx, ax, r):
    u = 0
    v = 0

    px = [None]*len(vx)

    kx = [999999]*len(vx)

    qx = [0]*len(vx)
    for u in range(len(qx)):
        qx[u] = vx[u]

    kx[r] = 0
    decrease_key(qx, kx)

    while len(qx) > 0:
        u = extract_min(qx)

        adj = adjacent(ax, u)
        for v in adj:
            w = weight(ax, u, v)

            if qx.count(v) > 0 and w < kx[v]:
                px[v] = u
                kx[v] = w
                decrease_key(qx, kx)
    return px

ax = sparse_matrix

vx = hep_graph.nodes()
px = prim(vx, ax, 0)
print (px)