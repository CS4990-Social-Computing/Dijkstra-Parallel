import sys 
from mpi4py import MPI
import networkx as nx
import numpy

comm = MPI.COMM_WORLD

'''
class Graph(): 
   
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
   
    def printSolution(self, dist): 
        print ("Vertex tDistance from Source") 
        for node in range(self.V): 
            print (node, "t", dist[node]) 
   
    def minDistance(self, dist, sptSet): 
        min = sys.maxsize 

        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
   
        return min_index 


    def dijkstra(self, src): 
   
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
   
        for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
    
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                    dist[v] = dist[u] + self.graph[u][v] 
   
        self.printSolution(dist) 
'''


def get_closeness_centrality(graph, source):
    p = nx.shortest_path(graph, source)
    shortest_path_list = []
    for node in p.keys():
        shortest_path_list.append(len(p[node]) - 1)
    clo_cen_val = len(shortest_path_list) / sum(shortest_path_list)
    return clo_cen_val


def all_closeness_centrality(graph):
    cc = {}     # {source: value}
    for node in list(graph):
        cc.update({node: get_closeness_centrality(graph, node)})
    return cc


# Driver program
# G = nx.read_edgelist("twitter_combined.txt", create_using=nx.DiGraph(), nodetype=int)
G = nx.read_edgelist("test_data_set.txt", create_using=nx.DiGraph(), nodetype=int)

# A = nx.adjacency_matrix(G)

# test, source = 1
# twitter, source = 214328887
print(all_closeness_centrality(G))


# g = Graph(len(A.todense()))
# g.graph = adj_list
# g.dijkstra(0)
