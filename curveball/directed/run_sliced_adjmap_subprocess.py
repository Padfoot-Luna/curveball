from multiprocessing.pool import Pool
from typing import Dict

from curveball.directed.run import step
from curveball.parutils import random_slice


def run(adjacency_list: Dict, nb_steps: int, nb_workers: int) -> Dict:
    """
    Runs a certain number of steps
    :param nb_workers: number of threads to work in parallel
    :param adjacency_list: the starting adjacency list
    :param nb_steps: the number of steps to run
    :return: a new adjacency list
    """
    with Pool(nb_workers) as pool:
        for _ in range(nb_steps):
            slices = random_slice(adjacency_list, nb_workers)
            adj_maps = pool.map(step, slices)
            adjacency_list = {k: v for d in adj_maps for k, v in d.items()}
    return adjacency_list
