from random import shuffle
from typing import List, Tuple

from curveball.core import trade_without_self_loop


def step(adjacency_list: List[Tuple[int, set]]) -> List[Tuple[int, set]]:
    """
    Runs one step

    :param adjacency_list: the graph adjacency list
    :return: a new adjacency list generated thanks to hte curveball algorithm
    """
    shuffle(adjacency_list)
    for i in range(1, len(adjacency_list), 2):
        node_1, neighbors_node_1 = adjacency_list[i - 1]
        node_2, neighbors_node_2 = adjacency_list[i]

        # trade their neighbors
        trade = trade_without_self_loop(index_node_1=node_1,
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
