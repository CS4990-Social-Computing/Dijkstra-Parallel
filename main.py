import sys 
from mpi4py import MPI
import networkx as nx
import numpy
from collections import Counter

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
    sum_shortest_path = sum(shortest_path_list)
    if sum_shortest_path <= 0:
        return 0
    clo_cen_val = (graph.number_of_nodes() - 1) / sum_shortest_path
    return clo_cen_val


def all_closeness_centrality(graph):
    cc = {}  # {source: value}
    # i = 1
    for node in list(graph):
        # print(i, "node(s) checked")
        cc.update({node: get_closeness_centrality(graph, node)})
        # i += 1
    return cc


def get_top_5_values(graph):
    cc = all_closeness_centrality(graph)
    k = Counter(cc)
    highest = k.most_common(5)
    top = {}
    for i in highest:
        top.update({i[0]: i[1]})
    return top


''' Driver program '''
i = 1
# print("creating graph...")
# G = nx.read_edgelist("twitter_combined.txt", create_using=nx.DiGraph(), nodetype=int)
# G = nx.read_edgelist("test_data_set.txt", create_using=nx.DiGraph(), nodetype=int)
G = nx.read_edgelist("test.txt", create_using=nx.DiGraph(), nodetype=int)

# A = nx.adjacency_matrix(G)
# print(A.todense())

# print(all_closeness_centrality(G))
print(get_top_5_values(G))

# g = Graph(len(A.todense()))
# g.graph = adj_list
# g.dijkstra(0)
