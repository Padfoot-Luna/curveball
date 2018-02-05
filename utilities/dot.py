def directed_graph_to_dot(adjacency_list, graph_name='graph_name'):
    """

    :param adjacency_list:
    :return: a dot representation of the graph
    >>> directed_graph_to_dot({})
    'digraph graph_name {\\n}'

    >>> directed_graph_to_dot({1: {2,3}, 2:{1}, 3:{1}})
    'digraph graph_name {\\n1 -> 2;\\n1 -> 3;\\n2 -> 1;\\n3 -> 1;\\n}'
    """
    dot_representation = 'digraph {} {{\n'.format(graph_name)
    edge = '->'
    for node, neighbours in adjacency_list.items():
        dot_representation += ''.join(['{} {} {};\n'.format(node, edge, n) for n in neighbours])
    dot_representation += '}'
    return dot_representation


def undirected_graph_to_dot(adjacency_list, graph_name='graph_name'):
    """

    :param adjacency_list:
    :return: a dot representation of the graph

    >>> undirected_graph_to_dot({})
    'graph graph_name {\\n}'

    >>> undirected_graph_to_dot({1: {2,3}, 2:{1}, 3:{1}})
    'graph graph_name {\\n1 -- 2;\\n1 -- 3;\\n}'

    >>> undirected_graph_to_dot({1: {2:{},3:{}}, 2:{1:{}}, 3:{1:{}}})
    'graph graph_name {\\n1 -- 2;\\n1 -- 3;\\n}'
    """
    dot_representation = 'graph {} {{\n'.format(graph_name)
    edge = '--'
    for node, neighbours in adjacency_list.items():
        dot_representation += ''.join(['{} {} {};\n'.format(node, edge, n) for n in neighbours if n >= node])
    dot_representation += '}'
    return dot_representation


if __name__ == "__main__":
    import doctest

    doctest.testmod()
