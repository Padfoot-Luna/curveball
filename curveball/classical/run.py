"""
Sequential implementation of the Curveball Algorithm for bipartite graphs
"""

from random import shuffle
from typing import Tuple, List

from curveball.core import trade_with_self_loop


def step(adjacency_list: List[Tuple[int, set]]) -> List[Tuple[int, set]]:
    """
    Runs one step of the Curveball Algorithm.

    :param adjacency_list: the graph adjacency list
    :return: a new adjacency list generated thanks to the curveball algorithm
    """
    shuffle(adjacency_list)
    for i in range(1, len(adjacency_list), 2):
        node_1, neighbors_node_1 = adjacency_list[i - 1]
        node_2, neighbors_node_2 = adjacency_list[i]

        # trade their neighbors
        trade = trade_with_self_loop(index_node_1=node_1,
                                     index_node_2=node_2,
                                     neighbors_node_1=neighbors_node_1,
                                     neighbors_node_2=neighbors_node_2)

        adjacency_list[i - 1] = trade[0]
        adjacency_list[i] = trade[1]
    return adjacency_list


def run(adjacency_list: List[Tuple[int, set]], nb_steps: int) -> List[Tuple[int, set]]:
    """
    Runs a certain number of steps

    :param adjacency_list: the starting adjacency list
    :param nb_steps: the number of steps to run
    :return: a new adjacency list
    """
    for _ in range(nb_steps):
        adjacency_list = step(adjacency_list)
    return adjacency_list
