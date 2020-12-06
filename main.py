from mpi4py import MPI
import networkx as nx
from collections import Counter


def get_top_5_networkx(graph):
    cc = Counter(nx.closeness_centrality(graph))
    highest = cc.most_common(5)
    top = {}
    for i in highest:
        top.update({i[0]: i[1]})
    return top


def scatter(graph, nodes_list):
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    cc_values = {}
    for i in range(rank, len(nodes), size):
        # print("rank", rank, "processing node", nodes_list[i])
        cc_values.update(get_closeness_centrality(graph, nodes_list[i]))
    if rank != 0:
        comm.send(cc_values, dest=0)
    if rank == 0:
        for i in range(1, size):
            cc_values.update(comm.recv(source=i))
        print_to_file(cc_values)


def get_closeness_centrality(graph, source):
    return {source: nx.closeness_centrality(graph, source)}


def get_top_5_values(closeness_centrality):
    cc_counter = Counter(closeness_centrality)
    highest = cc_counter.most_common(5)
    top_5 = {}
    for i in highest:
        top_5.update({i[0]: i[1]})
    return top_5


def print_to_file(cc_values):
    output = open("output.txt", "w")
    output.write("Closeness centrality values\n")
    output.write("--------------------------------------\n")
    for n in cc_values.keys():
        output.write(str(n) + ": " + str(cc_values[n]) + "\n")
    output.write("\nTop 5 closeness centrality values\n")
    output.write("--------------------------------------\n")
    for n in get_top_5_values(cc_values).keys():
        output.write(str(n) + ": " + str(cc_values[n]) + "\n")
    output.close()


if __name__ == "__main__":
    ''' test '''
    # test = nx.read_edgelist("test.txt", create_using=nx.DiGraph(), nodetype=int)
    # nodes = list(test.nodes)
    # scatter(test, nodes)

    ''' test_data_set '''
    # test_data_set = nx.read_edgelist("test_data_set.txt", create_using=nx.DiGraph(), nodetype=int)
    # nodes = list(test_data_set.nodes)
    # scatter(test_data_set, nodes)

    ''' Facebook '''
    fb = nx.read_edgelist("facebook_combined.txt", create_using=nx.DiGraph(), nodetype=int)
    nodes = list(fb.nodes)
    scatter(fb, nodes)

    ''' Twitter '''
    # t = nx.read_edgelist("twitter_combined.txt", create_using=nx.DiGraph(), nodetype=int)
    # nodes = list(t.nodes)
    # scatter(t, nodes)

    ''' Wiki '''
    # w = nx.read_edgelist("Wiki-Vote.txt", create_using=nx.DiGraph(), nodetype=int)
    # nodes = list(w.nodes)
    # scatter(w, nodes)
