from collections import defaultdict


def compute_cooccurrence_graph(adjacency_list):
    """

    :param adjacency_list:
    :return:
    """
    return {
        i: {
            j: cooccurrence_set_operation(i, j, adjacency_list)
            for j in range(i + 1, len(adjacency_list) + 1)
        }
        for i in range(1, len(adjacency_list))
    }


def cooccurrence_set_operation(index_node1, index_node2, adjacency_list):
    """
    Computes the cooccurrence between node1 and node2, i.e., the number of common neighbors

    :param index_node1:
    :param index_node2:
    :param adjacency_list:
    :return: the cooccurrence value (int)
    """
    neighbourhood_node1 = set(adjacency_list[index_node1])
    neighbourhood_node2 = set(adjacency_list[index_node2])
    return len(neighbourhood_node1 & neighbourhood_node2)


def cooccurrence_bipartite(adjacency_list):
    """

    :param adjacency_list:
    :return: a cooccurrence list for bipartite graphs
    """
    coocc = defaultdict(lambda: defaultdict(int))
    for i, n in adjacency_list.items():
        for j in n:
            for k in n:
                if k > j:
                    coocc[j][k] += 1
    return coocc
