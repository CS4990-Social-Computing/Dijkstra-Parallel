import sys 
from mpi4py import MPI
import networkx as nx

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

# For each node, it holds a reference to a list of nodes it's connected to
graph_dict = {}

# Holds { node : list[list of nodes 'node' is connected to] }
def add_to_dict(dict, n1):
    if n1 in dict:
        dict[n1].append(n2)
    else:
        dict[n1] = [n2]

g = nx.read_edgelist("test_data_set.txt", create_using=nx.DiGraph(), nodetype=int)

for n1, n2 in g.edges:
    add_to_dict(graph_dict, n1)

# Initalize adjacency list
graph_list = [[0 for x in range(len(graph_dict))] for x in range(len(graph_dict))] 

# Assign weights from node to each other node
for n in graph_dict.keys():
    for n2 in graph_dict[n]:
        graph_list[n-1][n2-1] = 1

print(graph_dict)
print(graph_list)

g = Graph(len(graph_dict)) 
g.graph = graph_list
g.dijkstra(0)

# g = Graph(9) 
# g.graph = [ [0, 4, 0, 0, 0, 0, 0, 8, 0], 
#             [4, 0, 8, 0, 0, 0, 0, 11, 0], 
#             [0, 8, 0, 7, 0, 4, 0, 0, 2], 
#             [0, 0, 7, 0, 9, 14, 0, 0, 0], 
#             [0, 0, 0, 9, 0, 10, 0, 0, 0], 
#             [0, 0, 4, 14, 10, 0, 2, 0, 0], 
#             [0, 0, 0, 0, 0, 2, 0, 1, 6], 
#             [8, 11, 0, 0, 0, 0, 1, 0, 7], 
#             [0, 0, 2, 0, 0, 0, 6, 7, 0] 
#         ]
   
# g.dijkstra(0)