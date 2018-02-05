import random
from typing import List, Tuple


def random_slice(adjacency_list: List[Tuple[int, set]], n: int) -> List[List[Tuple[int, set]]]:
    """
    Empties and slices an adjacency map into n slices.

    Each slice is a dictionary

    Each slice contains a subset of the adjacency map chosen UAR

    On average each slice will have the same length

    :param adjacency_list: (dict) an adjacency map (it will be destructed!)
    :param n: number of slices wanted
    :return: slices (list(dict)) a list of subsets of the adjacency map
    """
    slices = [[] for _ in range(n)]
    for node, neighbors in adjacency_list.items():
        slices[random.randint(0, n - 1)] += [(node, neighbors)]
    return slices
