def size_adjacency_matrix(nb_nodes, element_size=1):
    """
    Computes the size of an adjacency matrix n*n bits

    :param element_size: the size in bits of each matrix element
    :param nb_nodes: the number of nodes in the graph
    :return: nb_nodes * nb_nodes * element_size
    """
    return nb_nodes * nb_nodes * element_size


def size_adjacency_list(degree_distribution, element_size=32):
    """
    Computes the size of an adjacency list [{indices_neighbors_1}, {indices_neighbors_2},...]

    :param degree_distribution: a map {degree: nb_nodes_with_such_degree}
    :param element_size: the size in bits of each node index (usually integer size)
    :return:
    """
    return sum((d * n for d, n in degree_distribution.items())) * element_size


def size_adjacency_map(degree_distribution, nb_nodes, element_size=32):
    """
    Computes the size of an adjacency map {index_node_1:{indices_neighbors_1}, index_node_2:{indices_neighbors_2},...}

    :param nb_nodes: the number of nodes in the graph
    :param degree_distribution: a map {degree: nb_nodes_with_such_degree}
    :param element_size: the size in bits of each node index (usually integer size)
    :return:
    """
    return (nb_nodes + sum((d * n for d, n in degree_distribution.items()))) * element_size
