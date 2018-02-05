# -*- coding: utf-8 -*-
from multiprocessing.pool import Pool
from random import shuffle
from typing import List, Tuple

from curveball.classical.run import step


def parallel_step(adjacency_list: List[Tuple[int, set]], n: int, nb_workers: int, pool: Pool) -> List[Tuple[int, set]]:
    """
    Runs one step of the Curveball Algorithm in parallel.

    1. shuffles the adjacency list
    2. splits the adjacency list in `nb_workers` subsets of the adjacency_list
    3. calls the classical step function for  every worker on a given subset of the adjacency_list
    4. combines the results of the parallel workers (i.e., the subsets of the adjacency_list)

    :param nb_workers: number of parallel workers
    :param pool: a pool of processes
    :param n: the length of the adjacency list
    :param adjacency_list: the graph adjacency list
    :return: a new adjacency list generated thanks to the curveball algorithm
    """
    shuffle(adjacency_list)

    d = int(n / nb_workers)
    idx = [i * d for i in range(nb_workers)]
    idx.append(n)
    adjacency_lists = pool.map(step, [adjacency_list[idx[i]:idx[i + 1]] for i in range(nb_workers)])

    return [x for a in adjacency_lists for x in a]


def run(adjacency_list: List[Tuple[int, set]], nb_steps: int, nb_workers: int) -> List[Tuple[int, set]]:
    """
    Runs a certain number of steps
    :param nb_workers: number of threads to work in parallel
    :param adjacency_list: the starting adjacency list
    :param nb_steps: the number of steps to run
    :return: a new adjacency list
    """
    n = len(adjacency_list)
    with Pool(nb_workers) as pool:
        for _ in range(nb_steps):
            adjacency_list = parallel_step(adjacency_list, n, nb_workers, pool)
    return adjacency_list
