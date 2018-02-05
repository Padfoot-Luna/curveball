"""
Core methods used by the Curveball Algorithm
"""


import random
from typing import Tuple


def trade_with_self_loop(index_node_1: int, neighbors_node_1: set, index_node_2: int, neighbors_node_2: set) \
        -> Tuple[Tuple[int, set], Tuple[int, set]]:
    """
    Trades neighbors between two given nodes allowing self loops

    :param index_node_1: index of the first node
    :param neighbors_node_1: the set of node 1's neighbors indexes
    :param index_node_2: index of the second node
    :param neighbors_node_2: the set of node 2's neighbors indexes
    :return: the newly created adjacency list lines for node 1 and node 2: (index_node_1, new_neighbors_node_1), (index_node_2, new_neighbors_node_2)
    """
    possible_trades_node_1 = neighbors_node_1 - neighbors_node_2
    possible_trades_node_2 = neighbors_node_2 - neighbors_node_1
    new_neighbors_node_1, new_neighbors_node_2 = exchange_neighbors(neighbors_node_1=neighbors_node_1,
                                                                    neighbors_node_2=neighbors_node_2,
                                                                    possible_trades_node_1=possible_trades_node_1,
                                                                    possible_trades_node_2=possible_trades_node_2)
    return (index_node_1, new_neighbors_node_1), (index_node_2, new_neighbors_node_2)


def trade_without_self_loop(index_node_1: int, neighbors_node_1: set, index_node_2: int, neighbors_node_2: set) \
        -> Tuple[Tuple[int, set], Tuple[int, set]]:
    """
    Trades neighbors between two given nodes preventing self loop

    :param index_node_1: index of the first node
    :param neighbors_node_1: the set of node 1's neighbors indexes
    :param index_node_2: index of the second node
    :param neighbors_node_2: the set of node 2's neighbors indexes
    :return: the newly created adjacency list lines for node 1 and node 2: (index_node_1, new_neighbors_node_1), (index_node_2, new_neighbors_node_2)
    """
    possible_trades_node_1 = neighbors_node_1 - neighbors_node_2 - {index_node_2}
    possible_trades_node_2 = neighbors_node_2 - neighbors_node_1 - {index_node_1}
    new_neighbors_node_1, new_neighbors_node_2 = exchange_neighbors(neighbors_node_1=neighbors_node_1,
                                                                    neighbors_node_2=neighbors_node_2,
                                                                    possible_trades_node_1=possible_trades_node_1,
                                                                    possible_trades_node_2=possible_trades_node_2)
    return (index_node_1, new_neighbors_node_1), (index_node_2, new_neighbors_node_2)


def exchange_neighbors(neighbors_node_1: set, neighbors_node_2: set, possible_trades_node_1: set,
                       possible_trades_node_2: set) -> Tuple[set, set]:
    """
    Creates new sets of neighbors for node 1 and node 2 by trading neighbors uniformly at random

    :param neighbors_node_1: the set of neighbors from node 1
    :param neighbors_node_2: the set of neighbors from node 2
    :param possible_trades_node_1: the set of neighbors that are allowed to be traded from node 1
    :param possible_trades_node_2: the set of neighbors that are allowed to be traded from node 2
    :return: The newly created sets of neighbors for node 1 and node2 : (new_neighbors_node_1, new_neighbors_node_2)
    """
    possible_trades = possible_trades_node_1 ^ possible_trades_node_2
    if possible_trades:
        trades_first_node = set(random.sample(possible_trades, len(possible_trades_node_1)))
        trades_second_node = possible_trades - trades_first_node
        new_neighbors_node_1 = (neighbors_node_1 - possible_trades_node_1) ^ trades_first_node
        new_neighbors_node_2 = (neighbors_node_2 - possible_trades_node_2) ^ trades_second_node
        return new_neighbors_node_1, new_neighbors_node_2
    return neighbors_node_1, neighbors_node_2
