import sys 
from mpi4py import MPI
import networkx as nx
import numpy

comm = MPI.COMM_WORLD


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
   
# Driver program 

G = nx.read_edgelist("twitter_combined.txt", create_using=nx.DiGraph(), nodetype=int)
# G = nx.read_edgelist("test_data_set.txt", create_using=nx.DiGraph(), nodetype=int)

A = nx.adjacency_matrix(G)

p = nx.shortest_path(G, source=214328887)
# p = nx.shortest_path(G, source=1)

shortest_path_list = []
for node in p.keys():
    shortest_path_list.append(len(p[node]) - 1)

print(shortest_path_list)

sum_of_shortest_paths = sum(shortest_path_list)

clo_cen_val = float(len(shortest_path_list) / sum_of_shortest_paths)

print(clo_cen_val)

# g = Graph(len(A.todense())) 

# g.graph = adj_list
   
# g.dijkstra(0)