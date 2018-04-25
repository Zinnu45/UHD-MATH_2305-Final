"""
Created on Tue Apr 24 19:54:40 2018

@author: david
"""
from Weighted_Graph import *

G = Weighted_Graph('example.txt')
G.draw()


def cost(G, e):
    return G.edge_dict()[e]

def tree_one(v):
    return ({v}, [])

T = tree_one(1)
print('Initial tree is ', T)

def incident_edges(G, T):
    temp_edges = []
    E = G.edge_set()
    for e in E:
        for v in T[0]:
            if v in e and e not in T[1]:
                temp_edges.append(e)
    return temp_edges

print('Incident edges to T: ', incident_edges(G, T))

def valid_incident_edges(G, T):
    temp_edges = []
    possible_edges = incident_edges(G, T)
    for e in possible_edges:
        if e[0] not in T [0] or e[1] not in T[0]:
            temp_edges.append(e)
    return temp_edges

def min_incident_edge(G, T):
    edges = incident_edges(G,T)
    min_edge = edges[0]
    
    for e in edges:
        if cost(G,e) < cost(G, min_edge):
            min_edge = e
        return min_edge