def toString(adjacency_list):
    """
    This function is used to stringify an adjacency matrix in order to compare and count them
    :param adjacency_list:
    :return: a unique string representing the adjacency list

    >>> toString({})
    ''

    >>> toString({1:{2,3},3:{1},2:{1,3}})
    '1: [2, 3] 2: [1, 3] 3: [1]'

    >>> toString({1:{3,2,1},2:{1,3},3:{1}})
    '1: [1, 2, 3] 2: [1, 3] 3: [1]'
    """
    return ' '.join(['{}: {}'.format(k, str(sorted(adjacency_list[k]))) for k in sorted(adjacency_list)])


def to_unique_string(adjacency_list):
    """
    This function is used to stringify an adjacency list in order to compare and count them
    :param adjacency_list:
    :return: a unique string representing the adjacency list

    >>> to_unique_string([])
    '[]'

    >>> to_unique_string([(1,{2,3}),(2,{1,3}),(3,{1})])
    '[(1, (2, 3)), (2, (1, 3)), (3, (1,))]'

    >>> to_unique_string([(3,{1}),(1,{2,3}),(2,{1,3})])
    '[(1, (2, 3)), (2, (1, 3)), (3, (1,))]'

    >>> to_unique_string([(1,{3,2,1}),(2,{1,3}),(3,{1})])
    '[(1, (1, 2, 3)), (2, (1, 3)), (3, (1,))]'
    """
    return str(sorted([(node, tuple(neighbors)) for node, neighbors in adjacency_list]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
