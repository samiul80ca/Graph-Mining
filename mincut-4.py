# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:15:19 2018

@author: Sami
"""



from random import randint
from collections import defaultdict

 ######################

def getGraph(filename):


    with open(filename, 'r') as f_in:
        G = defaultdict(list)
        for row in f_in:
            row = row.split()
            G[row[0]] = row[1 : ]
    return G

 ######################

def getVEPair(range):

    v = randint(1, range)
    e = randint(1, range)
    return v, e

 ######################

def removeVEPair(G, V, E):

    while E in G[V]:
        G[V].remove(E)
    return G
 ######################
def contractNodes(G, V, E):

    edges = G[E]
    for edge in edges:
         if edge != V:
            G[V].append(edge)
    return G
 ######################
def removeNode(G, V, E):

    del G[E]
    for Vertex in G:
        while E in G[Vertex]:
            G[Vertex].remove(E)
            if V != Vertex:
                G[Vertex].append(V)
    return G

 ######################

def kargerMinCut():

    minCut = []
    for i in range(0, 100):
        G = getGraph('data1.txt')
        while(len(G) > 2):
            v, e = getVEPair(8)
            V = str(v)
            E = str(e)
            keys = G.keys()
            if V in keys and E != V:
                if E in G[V]:
                    G = removeVEPair(G, V, E)
                    G = contractNodes(G, V, E)
                    G = removeNode(G, V, E)
                else:
                    continue
        print (G)
        for v in G:
            minCut.append(len(G[v]))
            break
    return minCut
 ######################

minCut = kargerMinCut()
print ('######################')
print (minCut)
print (min(minCut))