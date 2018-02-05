import networkx as nx


def create_networkx_graph(adjacency_list):
    """
    Generates an undirected graph object (nx.Graph()) from a given adjacency list

    :param adjacency_list: an adjacency list
    :return: an undirected graph
    """
    graph = nx.Graph()
    graph.add_nodes_from(adjacency_list.keys())
    for node, neighbors in adjacency_list.items():
        graph.add_edges_from([(node, n) for n in neighbors])
    return graph


def create_networkx_digraph(adjacency_list):
    """
    Generates a directed graph object (nx.DiGraph()) from a given adjacency list

    :param adjacency_list: an adjacency list
    :return: a directed graph
    """
    digraph = nx.DiGraph()
    digraph.add_nodes_from(adjacency_list.keys())
    for node, neighbors in adjacency_list.items():
        digraph.add_edges_from([(node, n) for n in neighbors])
    return digraph


def is_isomorphic(g, graphs):
    """
    Checks whether g is isomorphic to at least one of the graphs contained in graphs

    :param g: a networkx graph object (nx.Graph class)
    :param graphs: a list of networkx graphs
    :return: true if g is isomorphic to at least one of the graphs contained in graphs
    """
    isomorphic = False
    i = 0
    while i < len(graphs) and not isomorphic:
        isomorphic = nx.is_isomorphic(g, graphs[i])
        i += 1
    return isomorphic
